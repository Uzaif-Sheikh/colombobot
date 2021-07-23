from flask import Flask, app, request
import requests
from pymessenger.bot import Bot

ACCESS_TOKEN = "EAANuV13vMV8BAEIvZAzOoJbNU4ytZCQYiyp6L8yOdlZCLtZAOBYcZCjzq8FMjJAvSX6FZBU8tOFbsq4FE5aZAN8ZB3VsoBCjmZC5AUD0PNoa16vkSGPqtFfZCqgn3Syj32hiOQbzlmxJoLRcJzItTSvH4ntRd6HMZCibFdMNvnFYLKTByxMEOaKXJUFPU5MmnHSFF2XJVUVZBptTVwZDZD"

VERIFY_TOKEN = "colombo_house_token"

bot = Bot(ACCESS_TOKEN)

greetings = ["hi","hello","yo","oi","hey"]



"add test"

app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
def check_message():
    if request.method == "GET":
        print(request.args.get("hub.verify_token"))
        if request.args.get("hub.verify_token") == VERIFY_TOKEN:
            print(request.args.get("hub.challenge"))
            return request.args.get("hub.challenge")
        else:
            return "Hello, Sorry"

    else:
        data = request.get_json()
        message = data['entry'][0]['messaging'][0]['message']
        sender_id = data['entry'][0]['messaging'][0]['sender']['id']

        try: 
            message['text']
        except KeyError:
            response = webhook_2(sender_id)
            return response

        if message['text'].lower() in greetings:
            response = webhook_1(sender_id)
            return response
        elif message['text'].lower() == "help":
            response = webhook_3(sender_id)
            return response
        else:
            response = webhook_2(sender_id)
            return response

        return "200"


# @app.route("/", methods=['POST'])
# def webhook_handle():
#     output = request.get_json()
#     print(output)
#     return 'ok'


# @app.route("/", methods=['POST'])
# def check_message():
#     data = request.get_json()
#     message = data['entry'][0]['messaging'][0]['message']
#     sender_id = data['entry'][0]['messaging'][0]['sender']['id']

#     try: 
#         message['text']
#     except KeyError:
#         response = webhook_2(sender_id)
#         return response

#     if message['text'].lower() in greetings:
#         response = webhook_1(sender_id)
#         return response
#     elif message['text'].lower() == "help":
#         response = webhook_3(sender_id)
#         return response
#     else:
#         response = webhook_2(sender_id)
#         return response

#     return 'ok'


def webhook_1(sender_id):
    request_body = {
                'recipient': {
                    'id': sender_id
                },
                'message': {"text":"hello!"}
            }
    response = requests.post('https://graph.facebook.com/v5.0/me/messages?access_token='+ACCESS_TOKEN,json=request_body).json()
    return response

def webhook_2(sender_id):
    message = """Sorry, I don't understand :( You can use the "help" command to find out more."""
    request_body = {
                'recipient': {
                    'id': sender_id
                },
                'message': {"text":message}
            }
    response = requests.post('https://graph.facebook.com/v5.0/me/messages?access_token='+ACCESS_TOKEN,json=request_body).json()
    return response

def webhook_3(sender_id):
    message = """https://www.facebook.com/groups/237630147901074"""
    request_body = {
                'recipient': {
                    'id': sender_id
                },
                'message': {"text":message}
            }
    response = requests.post('https://graph.facebook.com/v5.0/me/messages?access_token='+ACCESS_TOKEN,json=request_body).json()
    return response

if __name__ == "__main__":
    app.run()   