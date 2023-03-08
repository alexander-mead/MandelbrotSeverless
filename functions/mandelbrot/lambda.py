import json

def handler(event, context):
    print("Event:", event)
    print("Context:", context)
    
    response = {"message": "Request received."}
    return {
        "statusCode": 200,
        "body": json.dumps(response),
    }