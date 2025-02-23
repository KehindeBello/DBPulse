from fastapi import APIRouter, Request

router = APIRouter()


@router.get("/integration.json")
async def get_integration_json(request: Request):
    base_url = str(request.base_url).rstrip("/")
    return {
        "data": {
            "date": {"created_at": "2025-02-22", "updated_at": "2025-02-22"},
            "descriptions": {
                "app_name": "DBPulse",
                "app_description": "Monitor your MongoDB instace",
                "app_logo": "https://dbpulse.s3.us-east-1.amazonaws.com/dbPulse1.png",
                "app_url": base_url,
                "background_color": "#2ee65c",
            },
            "is_active": True,
            "integration_type": "interval",
            "integration_category": "Monitoring & Logging",
            "key_features": [
                "Uptime monitoring",
                "Active connections",
                "Disk space usage",
            ],
            "author": "Kehinde Bello",
            "settings": [
                {
                    "label": "db_uri",
                    "type": "text",
                    "required": True,
                    "default": "mongodb://localhost:27017/testdbPulse",
                },
                {
                    "label": "interval",
                    "type": "text",
                    "required": True,
                    "default": "* * * * *"
                },
            ],
            "tick_url": f"{base_url}/api/tick",
        }
    }
