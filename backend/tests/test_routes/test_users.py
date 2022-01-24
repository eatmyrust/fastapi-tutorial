import json

def test_create_user(client):
    data = {'username': 'testusername', 'email': 'testemail@test.com', 'password': '123456'}
    response = client.post('/user/', json.dumps(data))
    assert response.status_code == 200
    assert response.json()['email'] == 'testemail@test.com'
    assert response.json()['is_active'] == True