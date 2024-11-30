import requests

def test_web_endpoint():
    """
    Test if the Flask web server is running.
    """
    response = requests.get("http://localhost:5000/")
    assert response.status_code == 200
