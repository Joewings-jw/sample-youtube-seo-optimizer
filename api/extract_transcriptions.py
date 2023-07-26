import re
import googleapiclient.discovery

from api.settings import *
from api.utils import *
youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=key)



def extract_video_id(youtube_url):
    # Use regular expression to extract the video ID from the URL
    pattern = r"(?<=v=)[^&]+"
    match = re.search(pattern, youtube_url)
    if match:
        return match.group(0)
    else:
        return None

def extract_transcriptions(youtube_url):
    if not validate_youtube_url(youtube_url):
        print("Invalid YouTube URL. Please provide a valid YouTube video URL.")
        return []

    video_id = extract_video_id(youtube_url)
    if video_id:
        try:
            # Use the YouTube Data API to fetch the video's caption tracks
            captions_response = youtube.captions().list(
                part="snippet",
                videoId=video_id
            ).execute()

            # Check if there are any caption tracks available
            items = captions_response.get("items")
            if not items:
                print("No captions found for this video.")
                return []

            # Extract the transcriptions from the response
            transcriptions = []
            for caption in items:
                if "snippet" in caption and "text" in caption["snippet"]:
                    transcriptions.append(caption["snippet"]["text"])

            return transcriptions

        except Exception as e:
            print(f"An error occurred: {e}")
            return []
    else:
        print("Invalid YouTube URL. Could not extract video ID.")
        return []

