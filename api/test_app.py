import pytest
from index import app
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
    youtube_url = 'https://www.youtube.com/watch?v=5lDsg7KLeZI&ab_channel=GurobiOptimization'
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