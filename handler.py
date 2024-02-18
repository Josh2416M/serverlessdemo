import json
def hello(event, context):
    if event.get('httpMethod') == 'POST':
        body = event.get('body')
        if body:
            body = json.loads(body)
            if body.get('type') == 'url_verification':
                challenge = body.get('challenge')
                return {
                    "statusCode": 200,
                    "headers": {
                        "Content-Type": "text/plain"
                    },
                    "body": challenge
                }
    return {
        "statusCode": 400,
        "body": "Bad Request"
    }
