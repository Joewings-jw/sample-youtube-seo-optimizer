from flask import Flask, request, jsonify, render_template
import requests
import openai

from api.utils import validate_youtube_url

#uncomment these two services to test out with their corresonding API keys
# from api.extract_transcriptions import extract_transcriptions
# from api.openai_services import optimize_seo_with_chatgpt

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('test.page.html')

@app.route('/youtube_seo_optimizer', methods=['POST'])
def youtube_seo_optimizer():
    youtube_url = request.json.get('url')

    if not youtube_url:
        return jsonify({'error': 'File not found.'}), 404

    if not validate_youtube_url(youtube_url):
        print('YOut', youtube_url)
        return jsonify({'error': 'Invalid YouTube URL. Please provide a valid YouTube video URL.'}), 400

    try:
        # Extract transcriptions from the video using YouTube Data API or other libraries

        #uncomment to implement with YouTube data API 
        #transcriptions = extract_transcriptions(youtube_url)

        transcriptions = dummy_extract_transcriptions(youtube_url)

        # Use ChatGPT to optimize SEO

        #uncomment to implement with ChatGPT services 
        #optimized_text = optimize_seo_with_chatgpt(transcriptions)

        optimized_text = dummy_optimize_seo_with_chatgpt(transcriptions)

        response_data = {
            'optimized_text': optimized_text
        }

        return jsonify(response_data), 200

    except requests.exceptions.RequestException as e:
        return jsonify({'error': 'Request to YouTube API failed'}), 500

    except openai.OpenAIError as e:
        return jsonify({'error': 'OpenAI API request failed'}), 500

    except Exception as e:
        return jsonify({'error': 'An error occurred'}), 500
    
    


# Dummy function to simulate YouTube API response
def dummy_extract_transcriptions(youtube_url):
    if "test_video_id" in youtube_url:
        # Simulated YouTube API response with dummy transcriptions
        return [
            "This is the transcription of the first part of the video.",
            "And this is the transcription of the second part of the video."
        ]
    else:
        print("Invalid YouTube URL. Could not extract video ID.")
        return []


# Dummy function to simulate ChatGPT optimization
def dummy_optimize_seo_with_chatgpt(transcriptions):
    optimized_text = """
    Disclaimer: The following SEO optimization guide is a simulated example for demonstration purposes only. For actual SEO optimization, use real data from the YouTube Data API and ChatGPT API.

    Explore key strategies to improve your website's SEO:

    1. Conduct thorough keyword research to find high-traffic, low-competition keywords.
    2. Create valuable and engaging content to attract visitors and earn backlinks.
    3. Optimize meta titles, descriptions, and headings with target keywords.
    4. Ensure a user-friendly website structure and fast loading speed.
    5. Leverage social media presence to boost search engine rankings.
    6. Monitor SEO performance using tools like Google Analytics.

    Implement these SEO strategies for long-term success and increased website visibility.
    """
    return optimized_text