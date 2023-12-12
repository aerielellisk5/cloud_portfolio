# import json

# print('Loading function')

# def lambda_handler(event, context):
#     transactionResponse = {}
#     transactionResponse['message'] = 'This is working from lambda'
    
#     responseObject = {}    
#     responseObject['statusCode'] = 200
#     responseObject['headers'] = {}
#     responseObject['headers']['Content-Type'] = 'application/json'
#     responseObject['body'] = json.dumps(transactionResponse)
    
#     return responseObject

import json

print('Loading function')

def lambda_handler(event, context):
    transactionResponse = {}
    transactionResponse['message'] = 'This is working from lambda part 2'
    
    responseObject = {}    
    responseObject['statusCode'] = 200
    responseObject['headers'] = {}
    responseObject['headers']['Content-Type'] = 'application/json'
    responseObject['body'] = json.dumps(transactionResponse)
    
    return responseObject