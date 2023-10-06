from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_send_email_valid():
    response = client.post(
        url='/send_email',
        json={
            'to': 'beksei7@gmail.com',
            'subject': 'anySubject',
            'message': 'anyMessage'
        }
    )
    assert response.status_code == 200


def test_send_email_invalid_address():
    response = client.post(
        url='/send_email',
        json={
            'to': 'wrongEmail',
            'subject': 'anySubject',
            'message': 'anyMessage'
        }
    )
    assert response.status_code == 422


def test_send_email_invalid_body():
    response = client.post(
        url='/send_email',
        json={
            'subject': 'anySubject',
            'body': 'anyMessage',
            'receiver': 'anyReceiver'
        }
    )
    assert response.status_code == 422
