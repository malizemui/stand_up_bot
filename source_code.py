import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import schedule
import time

# Set your Slack bot token
SLACK_BOT_TOKEN = 'your_slack_bot_token'

# Set the channel where the stand-up meetings will be scheduled
CHANNEL_ID = 'your_channel_id'

# Set the time for the stand-up meetings in HH:MM format
MEETING_TIME = '10:00'

def send_standup_message(channel_id):
    try:
        client = WebClient(token=SLACK_BOT_TOKEN)
        response = client.chat_postMessage(
            channel=channel_id,
            text='It\'s time for the stand-up meeting! Please share your updates.'
        )
        print(f"Stand-up message sent to channel {channel_id}")
    except SlackApiError as e:
        print(f"Error sending stand-up message: {e.response['error']}")

def schedule_standup_meeting():
    schedule.every().day.at(MEETING_TIME).do(send_standup_message, channel_id=CHANNEL_ID)

def main():
    # Schedule the stand-up meeting
    schedule_standup_meeting()

    # Run the scheduling loop
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
