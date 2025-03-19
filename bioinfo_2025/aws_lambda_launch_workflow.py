import os
from datetime import datetime
import subprocess
import shutil
import stat
import requests
import json 
import boto3
from base64 import b64decode


BASE_URL = os.environ['BASE_URL']
DOMAIN = os.environ['DOMAIN']
WFL_ID = os.environ['WFL_ID']
WFL_NAME = os.environ['WFL_NAME']
VOLUME_NAME = os.environ['VOLUME_NAME']
#PASS_ENCRYPTED = os.environ['PASS']
PASS = os.environ['PASS']

# decrypt password
'''
PASS = boto3.client('kms').decrypt(
    CiphertextBlob=b64decode(PASS_ENCRYPTED),
    EncryptionContext={'LambdaFunctionName': os.environ['AWS_LAMBDA_FUNCTION_NAME']}
)['Plaintext'].decode('utf-8')
'''

def run_simple_command(cmd):
    stderr = subprocess.PIPE
    proc = subprocess.Popen(cmd, shell=True, 
    stdout=stderr, 
    stderr=stderr, 
    text=True)
    comm = proc.communicate()
    if proc.returncode != 0:
        print(comm)

    if not comm[0]:
        return ""
    return comm[0].rstrip()


def get_token(BASE_URL, DOMAIN):
    
    value = run_simple_command('echo -n $USER:{} | base64'.format(PASS))
    print(value)
    

    shasson_test_cid = 'b5661e09-f5df-4fb0-8c7f-3045d1bcd929'
    goal_consortium_cid = '64b6fc73-6af9-4c45-ba98-112191a3f139'
    goal_consortium_demo_cid = 'f5a327df-93e1-4694-bd4b-a2103b87cc98'
    url = '{}/v1/tokens?domain={}&cid={}'.format(BASE_URL, DOMAIN, goal_consortium_demo_cid)

    headers = {
        "Accept": "application/json",
        "Authorization": "Basic {}".format(value)
    }
    print(url)
    response = requests.request("POST", url, headers=headers)
    print(response)
    json_response = response.json()
    
    token = json_response['access_token']
    print(token)
    return token



def get_all_fastqs_in_project(token):
    url = '{}/v1/files?volume.name={}&pageSize=100'.format(BASE_URL, VOLUME_NAME)
    print(url)
    
    headers = {
        "Accept": "application/json",
        "Authorization": "Bearer {}".format(token)
    }
    
    response = requests.request("GET", url, headers=headers)
    items = response.json()['items']

    fastq_list = []
    for item in items:
        if 'fastq.gz' in item['name']:
            print(item['name'])
            fastq_list.append(item['name'])
            
    print(response.status_code)
    return fastq_list
 
 

def get_sample_name_and_read(file_name):
    prefix = ''
    read_number = 1
    if 'R1' in file_name:
        prefix = file_name.split('R1')[0].strip('_').strip('.')
    else:
        prefix = file_name.split('R2')[0].strip('_').strip('.')
        read_number = 2
    return prefix, read_number
    
    
    
def get_paired_samples(fastq_list):
    fastq_dict = dict()
    for file_name in fastq_list:
        sample_name, read_number = get_sample_name_and_read(file_name)
        if sample_name not in fastq_dict:
            per_sample_dict = dict()
            if read_number == 1:
                per_sample_dict['r1'] = file_name
            else:
                per_sample_dict['r2'] = file_name
            fastq_dict[sample_name] = per_sample_dict
        else:
            per_sample_dict = fastq_dict[sample_name]
            if read_number == 1:
                per_sample_dict['r1'] = file_name
            else:
                per_sample_dict['r2'] = file_name
            fastq_dict[sample_name] = per_sample_dict
            
    return fastq_dict
            
    

def launch_workflow_run(token, sample_name, fastq_forward, fastq_reverse): 
    url = '{}/v1/workflows/{}/versions/{}:launch'.format(BASE_URL, WFL_ID, WFL_NAME)

    print(url)
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer {}".format(token)
    }
    
    input = {
        "UChicago_job1_dataProcessing__sample_name": sample_name,
        "Input": {
            "class": "File",
            "location": "gds://goalconsortiumdemo/GOAL_1005Genes_200bp.bed?tenantId=tid:YXdzLXVzLXBsYXRmb3JtOjEwMDAwNTgxOmFhZTc0OTliLTEyMzQtNDU3NS04MWI0LTYyOWEwZGY2NDliMg"
        },
        "Input_2": {
            "class": "File",
            "location": "gds://goalconsortiumdemo/mask_forward.bed?tenantId=tid:YXdzLXVzLXBsYXRmb3JtOjEwMDAwNTgxOmFhZTc0OTliLTEyMzQtNDU3NS04MWI0LTYyOWEwZGY2NDliMg"
        },
        "Input_3": {
            "class": "File",
            "location": "gds://goalconsortiumdemo/mask_reverse.bed?tenantId=tid:YXdzLXVzLXBsYXRmb3JtOjEwMDAwNTgxOmFhZTc0OTliLTEyMzQtNDU3NS04MWI0LTYyOWEwZGY2NDliMg"
        },
        "Input_4": {
            "class": "File",
            "location": "gds://goalconsortiumdemo/Large_Panel_CodingExons_Refseq_6pbPadded_Clinical.bed?tenantId=tid:YXdzLXVzLXBsYXRmb3JtOjEwMDAwNTgxOmFhZTc0OTliLTEyMzQtNDU3NS04MWI0LTYyOWEwZGY2NDliMg"
        },
        "Input_5": {
            "class": "File",
            "location": "gds://goalconsortiumdemo/LargePanel_Clinical_Excluded.bed?tenantId=tid:YXdzLXVzLXBsYXRmb3JtOjEwMDAwNTgxOmFhZTc0OTliLTEyMzQtNDU3NS04MWI0LTYyOWEwZGY2NDliMg"
        },
        "Input_6": {
            "class": "File",
            "location" : "gds://goalconsortiumdemo/Large_Panel_DNClist.txt?tenantId=tid:YXdzLXVzLXBsYXRmb3JtOjEwMDAwNTgxOmFhZTc0OTliLTEyMzQtNDU3NS04MWI0LTYyOWEwZGY2NDliMg"
        },
        "ref": {
            "class": "File",
            "location": "gds://goalconsortiumdemo/new_genome.fa?tenantId=tid:YXdzLXVzLXBsYXRmb3JtOjEwMDAwNTgxOmFhZTc0OTliLTEyMzQtNDU3NS04MWI0LTYyOWEwZGY2NDliMg"
        },
        "forward": {
            "class": "File",
            "location": fastq_forward#"gds://goalconsortium/GM12878-FFPE-2020-PAN.R1.fastq.gz?tenantId=tid:YXdzLXVzLXBsYXRmb3JtOjEwMDAwNTgxOmFhZTc0OTliLTEyMzQtNDU3NS04MWI0LTYyOWEwZGY2NDliMg"
        },
        "reverse": {
            "class": "File",
            "location": fastq_reverse#"gds://goalconsortium/GM12878-FFPE-2020-PAN.R2.fastq.gz?tenantId=tid:YXdzLXVzLXBsYXRmb3JtOjEwMDAwNTgxOmFhZTc0OTliLTEyMzQtNDU3NS04MWI0LTYyOWEwZGY2NDliMg"
        },
        "uchicago_job2_full__depth": 1000000,
        "uchicago_job2_full__skip_base": 0
    }
    
    '''
    engineparams = {
        "outputDirectory": "gds://path"
    }'''
    
    data = { 
        "name": "uchicago_launch_from_lambda_{}".format(sample_name),
        "input": input
        #"engineParameters": engineparams
    }
    
    response = requests.request("POST", url, headers=headers, data = json.dumps(data))
    wfr_id = response.json()['id']

    print(wfr_id)
    print(response.status_code)
    return wfr_id


def lambda_handler(event, context):
    
    token = get_token(BASE_URL, DOMAIN)
    print(token)
    
    #project_name_lowercase = PROJECT_NAME.lower().replace('_','')

    fastq_list = get_all_fastqs_in_project(token)
    fastq_dict = get_paired_samples(fastq_list)


    #track workflow run IDs
    wfr_ids_dict = dict()
    
    # for now just run for a single sample pair
    i=0
    for sample_name, fastqs_dict in fastq_dict.items():

        i+=1
        if i > 1: break
        fastq_file_r1_path = ''
        fastq_file_r2_path = ''
        for read_number, fastq_file in fastqs_dict.items():
            fastq_file_path = 'gds://{}/{}'.format(VOLUME_NAME, fastq_file)
            if read_number=='r1':  fastq_file_r1_path = fastq_file_path
            else: fastq_file_r2_path = fastq_file_path
  
        print(sample_name)
        print(fastq_file_r1_path)
        print(fastq_file_r2_path)
        #wfr_id = launch_workflow_run(token, sample_name, fastq_file_r1_path, fastq_file_r2_path)
        wfr_id = 'wfr.1fd8678530034c77a6d755cb8eb14d87'
        wfr_ids_dict[sample_name] = wfr_id

    print(fastq_dict)
    print(wfr_ids_dict)


    return {
        'token': token,
        'wfr_ids': wfr_ids_dict
    }
