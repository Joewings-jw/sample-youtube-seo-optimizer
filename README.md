# Youtube SEO Optimizer

 simple API - which can be hosted on Heroku.

## How to Run Locally

To run the application locally, follow these steps:

1. Create and activate a virtual environment for the project.

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

2. Install the required dependencies

```bash
pip install -r requirements.txt
```

3. Copy the .env.example file to .env and set the appropriate values.

```bash
cp .env.example .env
```

4. Set the environment variables and start the Flask app.\

```bash
export FLASK_ENV=development
export FLASK_APP=index
flask run

```

## Routes

### `/api/`

- Method: GET
- Description: Renders the index page (test.page.html).

### `/api/youtube_seo_optimizer`

- Method: POST
- Description: Optimizes SEO for a YouTube video using its transcriptions.
- Request Body: JSON object with the following key-value pair:

```json
{
    "url": "https://www.youtube.com/watch?v=YOUR_VIDEO_ID"
}
```

- Response: JSON object with the optimized text:

```json
{
    "optimized_text": "Optimized SEO text for the YouTube video."
}
```

## Form template

![Alt Text](images/form_without_data.png)

## File input success with sample SEO optmizations 

![Alt Text](images/form_data.png)


### Error Handling

If there is an error during the optimization process, the API will return an error response with an appropriate message. The possible error messages are:

- "File not found.": Returned when the YouTube URL is missing or not provided.
- "Request to YouTube API failed": Returned when there is an issue with the YouTube Data API request.
- "OpenAI API request failed": Returned when there is an issue with the OpenAI API request.
- "An error occurred": Returned when an unexpected error occurs during the optimization process.

## How the `/youtube_seo_optimizer` Route Works

1. When a POST request is made to `/youtube_seo_optimizer`, the function `youtube_seo_optimizer()` is called.

2. The YouTube URL is extracted from the request JSON, and if it is missing, the API returns a 404 error response with the message "File not found."

3. The function `extract_transcriptions()` is called to extract transcriptions from the YouTube video using the YouTube Data API or other libraries.

4. The function `optimize_seo_with_chatgpt()` is called to optimize SEO using the extracted transcriptions with the help of OpenAI's GPT service.

5. The optimized text is returned as a JSON response with the key "optimized_text."

6. If there are any errors during the process, appropriate error responses are returned with the respective error messages.

## Note

- Replace `your_secret_key` with your desired secret key for the Flask app.
- Replace `your_openai_api_key` with your actual OpenAI API key.
- The application uses Flask-CORS to enable Cross-Origin Resource Sharing, allowing the application to be accessed from different domains. Ensure that CORS is set up correctly based on your deployment requirements.

Please make sure to set the required environment variables before running the application. Additionally, consider deploying the application on a server or a cloud platform to make it accessible to others.


## TESTS

The tests include:

1. test_youtube_seo_optimizer_success: This test checks if the /youtube_seo_optimizer endpoint returns a successful response with optimized text when provided with a valid YouTube URL.

2. test_youtube_seo_optimizer_missing_url: This test checks if the /youtube_seo_optimizer endpoint returns a 404 error response with the message "File not found." when the YouTube URL is missing or not provided in the request.

**The third test, test_youtube_seo_optimizer_invalid_url, is commented out and not implemented. This is because the actual API call to the YouTube Data API is not being made in the application, and there is no functionality to handle an invalid URL. Therefore, this test case needs to be further discussed and implemented based on the specific requirements and logic for handling invalid URLs.**

```bash
import pytest
from application import app
import openai

from settings import *

@pytest.fixture(autouse=True)
def set_openai_api_key():
    openai.api_key = openai_api_key

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

        

def test_youtube_seo_optimizer_success(client):
    youtube_url = 'https://www.youtube.com/watch?v=YA5aBupkuPU&ab_channel=GTCoding'
    data = {'url': youtube_url}
    response = client.post('/youtube_seo_optimizer', json=data)

    assert response.status_code == 200
    assert 'optimized_text' in response.json
    assert isinstance(response.json['optimized_text'], str)

def test_youtube_seo_optimizer_missing_url(client):
    response = client.post('/youtube_seo_optimizer', json={})
    
    assert response.status_code == 404
    assert 'error' in response.json
    assert response.json['error'] == 'File not found.'

# def test_youtube_seo_optimizer_invalid_url(client):
#     youtube_url = 'https://www.invalidurl.com'
#     data = {'url': youtube_url}
#     response = client.post('/youtube_seo_optimizer', json=data)
    
#     assert response.status_code == 500
#     assert 'error' in response.json
#     assert 'Request to YouTube API failed' in response.json['error']

```

## Running Tests

To run the tests, navigate to the `api/` directory and use the following command:
```bash
cd api/
pytest test_app.py
```

