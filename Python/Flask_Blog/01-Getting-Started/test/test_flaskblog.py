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
    
def test_about_page2(client):
    """Test if the About page loads correctly."""
    response = client.get("/about")
    assert response.status_code == 200
    assert b"Page" in response.data
def test_about_page3(client):
    """Test if the About page loads correctly."""
    response = client.get("/about")
    assert response.status_code == 200
    assert b"About Page" in response.data
    
def Test_expextaion_about_page(client):
    response = client.get("/about")
    assert response.status_code == 200
    assert b"About" not in response.data
    
    def faulty_function():
        if b"About" in response.data:
            raise ValueError("Intentional error for testing")

    with pytest.raises(ValueError, match="Intentional error for testing"):
        faulty_function()
        
def test_fail_intentionally(client):
    """This test is designed to fail."""
    response = client.get("/about")
    assert response.status_code == 404  
    
def test_fail_in_response_data(client):
    """This test will fail because 'Nonexistent Text' is not in the response."""
    response = client.get("/about")
    assert b"Nonexistent Text" in response.data  # This will fail
#tests added   