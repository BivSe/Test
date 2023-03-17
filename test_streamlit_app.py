from fastapi.testclient import TestClient
from streamlit_app import app
# import streamlit_app


client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 422
# assert response.json() == {"Key": "True"}
