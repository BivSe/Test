from fastapi.testclient import TestClient
from streamlit_app import tests
# import streamlit_app

app = tests("Проверка")
client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Key": "True"}
