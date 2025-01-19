import yt_dlp

def download_video(url, download_path='.'):
    try:
        # Set download options
        ydl_opts = {
            'outtmpl': f'{download_path}/%(title)s.%(ext)s',  # Save with video title
            'quiet': False,  # Show progress information
        }

        # Create yt-dlp object and download video
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        print(f"Download complete! Video saved to {download_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Hardcoded YouTube video URL
    video_url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'  # Replace with your desired video URL
    
    # Optional: You can change the path to save the video to a specific folder
    download_directory = '.'  # '.' means current directory, change if you want a different path

    # Call the download function
    download_video(video_url, download_directory)
