from app import app

def test_home():
    tester = app.test_client()
    response = tester.get('/name/Mansi')
    assert response.status_code == 200
    assert b"Hello Mansi" in response.data
