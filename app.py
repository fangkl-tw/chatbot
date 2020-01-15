from flask import Flask, request, abort
from linebot import(LineBotApi, WebhookHandler)
from linebot.exceptions import(InvalidSignatureError)
from linebot.moudels import(MessageEvent, TextMessage,
                            TextSendMessage, ImageSendMessage)

app = Flask(__name__)
line_bot_api = LineBotApi('kcaVVRCi+NcmbK5Z1H19jylD4D9XZHeai27F+x8eoxhUkOaNjyYOT/C8vi2lcGNqMHgetSQaDez3IppqnP/GYEvCeYmH5AQe5Omfl2Ul9Z3G6ec9vdW1xDojwfMeL6EqbvTyvRkHFSyUmcBuItFvEgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('f02ef69c805e6d7b87c733516159a760')

@app.route("/callback",methods=['POST'])
def callback():

def hndle_message(event):
    message = TextSendMessage(text='hello!')
    line_bot_api.reply_message(
        event.reply_token,message)
