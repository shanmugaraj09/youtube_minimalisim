from flask import Flask, render_template, request, redirect, url_for
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os
import pickle
import datetime

app = Flask(__name__)

# OAuth 2.0 scopes and credentials file
SCOPES = ['https://www.googleapis.com/auth/youtube.readonly']
CREDENTIALS_FILE = 'client_secret_995726212542-5tpsma59t3smen7pq8m1lueh8e88410l.apps.googleusercontent.com.json'  # Replace with your downloaded JSON file

def get_authenticated_service():
    credentials = None
    # Load existing credentials from the token.pickle file
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            credentials = pickle.load(token)

    # Check if credentials are valid
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            # Refresh expired credentials
            credentials.refresh(Request())
        else:
            # Perform manual authentication for the first time
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
            credentials = flow.run_local_server(port=0)
        # Save the new credentials for future use
        with open('token.pickle', 'wb') as token:
            pickle.dump(credentials, token)

    return build('youtube', 'v3', credentials=credentials)

@app.route('/')
def index():
    try:
        youtube = get_authenticated_service()
        # Get the list of subscription channels
        subscriptions = youtube.subscriptions().list(
            part='snippet',
            mine=True,
            maxResults=50
        ).execute()

        channels = [
            {'channelId': item['snippet']['resourceId']['channelId'], 'title': item['snippet']['title']}
            for item in subscriptions['items']
        ]

        channel_id = request.args.get('channel_id')
        filter_option = request.args.get('filter', '1month')

        # Determine the date range based on the filter
        if filter_option == '1week':
            start_date = (datetime.datetime.utcnow() - datetime.timedelta(days=7)).isoformat("T") + "Z"
        elif filter_option == '1month':
            start_date = (datetime.datetime.utcnow() - datetime.timedelta(days=30)).isoformat("T") + "Z"
        else:
            start_date = (datetime.datetime.utcnow() - datetime.timedelta(days=30)).isoformat("T") + "Z"

        videos = []
        if channel_id:
            # Fetch videos from the selected channel
            search_response = youtube.search().list(
                part='snippet',
                channelId=channel_id,
                publishedAfter=start_date,
                type='video',
                order='date',
                maxResults=10
            ).execute()

            videos = [
                {
                    'title': item['snippet']['title'],
                    'videoId': item['id']['videoId'],
                    'thumbnail': item['snippet']['thumbnails']['medium']['url'],
                    'publishedAt': item['snippet']['publishedAt']
                }
                for item in search_response['items']
            ]

        return render_template('index.html', channels=channels, videos=videos, filter_option=filter_option)
    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
