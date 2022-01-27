import json

def test_create_job(client):
    data = {
        "title": "SDE 1 Yahoo",
        "company": "Testhoo",
        "company_url": "https://www.testhoo.com",
        "location": "NY, USA",
        "description": "Testing",
        "date_posted": "2022-07-20"
        }

    response = client.post("/job/create-job", json.dumps(data))
    assert response.status_code == 200