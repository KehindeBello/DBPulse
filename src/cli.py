import asyncio
from core.monitor import server_status
from models.models import MonitorPayload
from core.config import settings


def create_test_payload():
    return {
        "channel_id": "local-test",
        "return_url": "http://localhost:8000/test",  # This won't be used in local mode
        "settings": [
            {
                "label": "db_uri",
                "type": "text",
                "required": True,
                "default": settings.DB_URI,
            }
        ],
    }


async def main():
    print("DBPulse Local Monitoring Tool")
    print("-----------------------------")

    try:
        while True:
            await server_status(create_test_payload(), local_mode=True)
            print(f"\nWaiting {settings.TIME_INTERVAL} seconds before next check...")
            await asyncio.sleep(settings.TIME_INTERVAL)
    except KeyboardInterrupt:
        print("\nMonitoring stopped")


if __name__ == "__main__":
    asyncio.run(main())
