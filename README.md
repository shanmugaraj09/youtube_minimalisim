# youtube_minimalisim

This project to create a webpage connected to youtube acccount api and show videos only my subscription channel of last 1 month .
in the webpage we should be able to play the video.
the webpage will be localhost 
this projecct created to not to get distracted by youtube video recommentations ads etc

points to remember
when downloaded to local system , place the json of the client oth for connecting to youtube
after running the script.py , access the http://127.0.0.1:5000/
first time we have to manually authenticate after that there be pickle file creaated and it will automatic later that 



--------------------------------------------------
System Components
User Interface (Web Page):

Built using HTML templates rendered by Flask.
Contains:
A sidebar to list subscribed channels.
A video filter dropdown (e.g., last 1 week, last 1 month).
A main content area to display videos and their details (title, embed player, upload date).
Backend (Flask App):

Powered by Python and the Flask framework.
Interacts with the YouTube Data API to fetch subscriptions and videos.
Handles routing, template rendering, and passing data between the UI and the YouTube API.
YouTube Data API:

Provides data about user subscriptions and videos.
Requires OAuth 2.0 authentication for access to user-specific data.
Authentication and Credentials:

Uses OAuth 2.0 to authenticate the user and obtain access to their YouTube account.
Stores credentials in a token.pickle file for reuse.
System Flow
1. User Requests the Web Page
Action: The user visits the home page of the Flask app (http://127.0.0.1:5000/).
Backend:
Checks if a channel_id is provided in the query string (e.g., /?channel_id=...).
Fetches the list of subscribed channels using the YouTube API (subscriptions.list endpoint).
Passes the list of channels to the HTML template for rendering the sidebar.
2. User Selects a Channel
Action: The user clicks a channel link in the sidebar.
Backend:
Receives the channel_id and the selected filter (e.g., 1week or 1month) via the query string.
Determines the date range (publishedAfter) based on the filter option.
Fetches videos uploaded by the selected channel within the specified date range using the YouTube API (search.list endpoint).
Passes the video details (title, video ID, thumbnail, upload date) to the template.
3. Filter Videos by Time Period
Action: The user changes the filter option (e.g., "Last 1 Week").
Backend:
Receives the filter and channel_id via the query string.
Adjusts the date range accordingly.
Fetches videos that match the new criteria.
Renders the updated video list on the web page.
4. Video Playback and Information Display
Action: The user views the video list on the web page.
Frontend:
Each video is displayed with:
Embedded YouTube player (iframe) for direct playback.
Title and upload date below the video player.
The embedded player includes parameters to minimize distractions, such as related video suggestions.
5. Authentication Handling
First Run:
If no token.pickle exists, the app prompts the user to authenticate via a browser-based OAuth 2.0 flow.
Saves the credentials to token.pickle for future use.
Subsequent Runs:
Loads credentials from token.pickle.
Automatically refreshes expired tokens using the refresh token.
System Flow Summary
User Authentication:

Authenticate with OAuth 2.0 and store credentials for future use.
Fetch Subscriptions:

Query the YouTube API to list channels the user is subscribed to.
Fetch Videos:

Query the YouTube API to get videos from the selected channel within the specified date range.
Render Web Page:

Display channels in the sidebar.
Show videos with embedded players, titles, and upload dates in the main content area.
User Interaction:

Users can select channels and apply filters without re-authenticating.