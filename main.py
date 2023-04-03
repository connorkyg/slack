import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from slack_bolt import App

# Slack App 설정
SLACK_APP_TOKEN = os.environ["SLACK_APP_TOKEN"]
SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]
SLACK_CHANNEL_ID = os.environ["SLACK_CHANNEL_ID"]

# Slack 클라이언트 생성
client = WebClient(token=SLACK_BOT_TOKEN)

# Slack App 생성
app = App(token=SLACK_APP_TOKEN)


# Slack 메시지 전송 함수
def send_slack_message(message):
    try:
        response = client.chat_postMessage(
            channel=SLACK_CHANNEL_ID,
            text=message
        )
        print(f"Slack Message Sent: {message}")
    except SlackApiError as e:
        print("Error sending message: {}".format(e))


# 작업이 끝나면 Slack 메시지 전송
send_slack_message("작업이 완료되었습니다.")
