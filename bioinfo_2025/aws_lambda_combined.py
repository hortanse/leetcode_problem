import json
import requests
import string
import random
import os
from datetime import datetime
import boto3
from base64 import b64decode

# Environment variables
BASE_URL = os.environ['BASE_URL']
DOMAIN = os.environ['DOMAIN']
WFL_ID = os.environ['WFL_ID']
WFL_NAME = os.environ['WFL_NAME']
VOLUME_NAME = os.environ['VOLUME_NAME']
PASS = os.environ['PASS']

def get_token(BASE_URL, DOMAIN):
    value = run_simple_command('echo -n $USER:{} | base64'.format(PASS))
    
    goal_consortium_demo_cid = 'f5a327df-93e1-4694-bd4b-a2103b87cc98'
    url = '{}/v1/tokens?domain={}&cid={}'.format(BASE_URL, DOMAIN, goal_consortium_demo_cid)

    headers = {
        "Accept": "application/json",
        "Authorization": "Basic {}".format(value)
    }
    
    response = requests.request("POST", url, headers=headers)
    json_response = response.json()
    return json_response['access_token']

def run_simple_command(cmd):
    stderr = subprocess.PIPE
    proc = subprocess.Popen(cmd, shell=True, stdout=stderr, stderr=stderr, text=True)
    comm = proc.communicate()
    return "" if not comm[0] else comm[0].rstrip()

def launch_workflow_run(token, sample_name, file_id): 
    # Setup workflow parameters
    activation_code_detail_id = '6375eb43-e865-4d7c-a9e2-2c153c998a5c'
    analysis_storage_id = "6e1b6c8f-f913-48b2-9bd0-7fc13eda0fd0"
    pipeline_id = "fd540bf8-67f1-4506-99e9-c89cc9a98fdd"
    user_reference = 'CallLambda' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    
    payload = {
        "userReference": user_reference,
        "pipelineId": pipeline_id,
        "tags": {
            "technicalTags": [],
            "userTags": []
        },
        "activationCodeDetailId": activation_code_detail_id,
        "analysisStorageId": analysis_storage_id,
        "analysisInput": {
            "inputs": [{
                "parameterCode": "file",
                "dataIds": [file_id]
            }]
        }
    }

    url = '{}/v1/workflows/{}/versions/{}:launch'.format(BASE_URL, WFL_ID, WFL_NAME)
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer {}".format(token)
    }
    
    response = requests.post(url, json=payload, headers=headers)
    return response.json()['id'] if response.status_code == 201 else None

def lambda_handler(event, context):
    # 1. Process SNS message
    message = json.loads(event['Records'][0]['Sns']['Message'])
    project_id = message['projectId']
    analysis_id = message['payload']['id']
    
    # 2. Get authentication token
    token = get_token(BASE_URL, DOMAIN)
    
    # 3. Get file information from ICA
    url = f'{BASE_URL}/v1/projects/{project_id}/analyses/{analysis_id}/outputs'
    headers = {
        'X-API-Key': '${API-KEY}',
        'accept': 'application/vnd.illumina.v3+json'
    }
    
    response = requests.get(url, headers=headers)
    json_data_slice = response.json()['items'][0]['data'][0]['children']
    
    # 4. Find the target file
    file_id = None
    for json_obj in json_data_slice:
        if json_obj.get('name') == 'test.txt':
            file_id = json_obj['dataId']
            break
    
    if not file_id:
        return {
            'statusCode': 404,
            'body': 'Error: Target file not found'
        }
    
    # 5. Launch the workflow
    wfr_id = launch_workflow_run(token, f"analysis_{analysis_id}", file_id)
    
    if wfr_id:
        return {
            'statusCode': 201,
            'body': {
                'workflow_run_id': wfr_id,
                'message': 'Workflow launched successfully'
            }
        }
    else:
        return {
            'statusCode': 500,
            'body': 'Error: Failed to launch workflow'
        } 