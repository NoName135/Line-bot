from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, StickerSendMessage
)

app = Flask(__name__)

line_bot_api = LineBotApi('FP8Zvq0gzH549WPaGuwPdinFPX/RzQf/FrAsBUokhK6SY5MvW8dy0AlwoqUASVHFvorOgydFurzYbbFy5PmWd4hFq6+b6UXwlrLYR/i7lqNeVj7WNV0Az7Jzl/Svpqra84RONKHPgT5nEQLX0mCygQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('c371683b41c043480708130fc12ebcba')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text

    re = '哩公蝦小挖跨謀'

    if '變態' in msg:
        sticker_message = StickerSendMessage(
            package_id='11537',
            sticker_id='52002763'
        )
        line_bot_api.reply_message(
            event.reply_token,
            sticker_message)
        return
    elif '警察' in msg:
        sticker_message = StickerSendMessage(
            package_id='11538',
            sticker_id='51626511'
        )
        line_bot_api.reply_message(
            event.reply_token,
            sticker_message)
        return

    if msg in ['hi', 'Hi', '嗨']:
        re = 'Hi, 我是愛蘿莉的簡歪信'
    elif msg == '你是誰':
        re = '我是蘿莉控'
    elif ['蘿莉', '羅莉'] in msg:
        re = '我好興奮阿!!!'

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=re))


if __name__ == "__main__":
    app.run()