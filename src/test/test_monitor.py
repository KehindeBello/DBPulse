from test import client

def test_monitor_endpoint():
    payload = {
        "channel_id": "test-channel",
        "return_url": "http://example.com/webhook",
        "settings": [
            {
                "label": "db_uri",
                "type": "text",
                "required": True,
                "default": "mongodb://localhost:27017/testdb",
            }
        ],
    }

    response = client.post("/api/tick", json=payload)
    assert response.status_code == 202
    assert response.json() == {"status": "accepted"}


def test_integration_json():
    response = client.get("/api/integration.json")
    assert response.status_code == 200
    data = response.json()["data"]
    assert "descriptions" in data
    assert "settings" in data
