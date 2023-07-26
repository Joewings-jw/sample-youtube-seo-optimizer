import re

def validate_youtube_url(youtube_url):
    # Regular expression to validate a YouTube video URL
    pattern = r"^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+$"
    return re.match(pattern, youtube_url)