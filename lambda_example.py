        import json
        import requests

        import string
        import random

        import json

        def lambda_handler(event, context):
            
            message = json.loads(event['Records'][0]['Sns']['Message'])
            
            project_id = message['projectId']
            analysis_id = message['payload']['id']
            
            url = 'https://ica.illumina.com/ica/rest/api/projects/' + \
            project_id + '/analyses/' + analysis_id + '/outputs'
            headers = {
                'X-API-Key': '${API-KEY}',
                'accept': 'application/vnd.illumina.v3+json'
            }

            response = requests.get(url, headers=headers)
            json_data_slice = response.json()['items'][0]['data'][0]['children']
            
            for json_obj in json_data_slice:
                if json_obj.get('name') == 'test.txt':
                    file_id = json_obj['dataId']                   

            # some variables
            
            activation_code_detail_id = '6375eb43-e865-4d7c-a9e2-2c153c998a5c'
            analysis_storage_id = "6e1b6c8f-f913-48b2-9bd0-7fc13eda0fd0"
            pipeline_id = "fd540bf8-67f1-4506-99e9-c89cc9a98fdd"
            user_reference = 'CallLambda' + ''.join(random.choices(string.ascii_uppercase + \
            string.digits, k=6))
            
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
                "inputs": [
                {
                    "parameterCode": "file",
                    "dataIds": [
                    file_id
                    ]
                }
                ]
            }
            }
                 
            url_pipeline2 = 'https://ica.illumina.com/ica/rest/api/projects/' + \ 
            project_id + '/analysis:nextflow'
            headers_pipeline2 = {
                'X-API-Key': '${API-KEY}',
                'accept': 'application/vnd.illumina.v3+json',
                'Content-Type': 'application/vnd.illumina.v3+json'
            }
            
            response_start = requests.post(url_pipeline2, data=json.dumps(payload), headers=headers_pipeline2)

            # Check the response status code
            if response_start.status_code == 201:
                # POST request successful
                response_data = response_start.json()
                return {
                    'statusCode': 201,
                    'body': response_data
                }
            else:
                # POST request failed
                return {
                    'statusCode': response_start.status_code,
                    'body': 'Error: Failed'
                }