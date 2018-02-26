from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import time
import datetime

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_ahoy_reply():
    """Respond to incoming messages with a friendly SMS."""
    # Start our response

    number = request.form['From']
    message_body = request.form['Body']
    #Write texts to file.
    file = open("testfile.txt","a+")
    file.write(str(datetime.datetime.now()) + ", " + number + ", " + message_body + "\n")
    # file.write(datetime.datetime.now() +  ", " + number + ", " + message_body + "\n")
    file.close()

    """ New Sorting Logic"""
    KeyWords = ('test', 'testing', 'Tokyo')
    if any(s in message_body for s in KeyWords):
        resp = MessagingResponse()
        resp.message("From: " + number + " Message: " + message_body  )
    else:
        resp= MessagingResponse()
        #resp.message("ERROR")
        print("Message did not match any keywords")
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
