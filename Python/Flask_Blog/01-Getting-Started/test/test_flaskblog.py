import pytest
from flaskblog import app

@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config["TESTING"] = True  # Enable testing 
    client = app.test_client()
    return client

def test_homepage(client):
    """Test if the homepage loads successfully."""
    response = client.get("/")
    assert response.status_code == 200  # Expecting HTTP 200 OK
    assert b"<h1>Home Page</h1>" in response.data  # Check if "Welcome" is in the response

def test_about_page(client):
    """Test if the About page loads correctly."""
    response = client.get("/about")
    assert response.status_code == 200
    assert b"About" in response.data
