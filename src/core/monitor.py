from typing import Dict, Any
import requests
from pymongo import MongoClient
from models.models import MonitorPayload


def format_uptime_message(uptime_seconds):
    days = uptime_seconds // (24 * 3600)
    remaining_hours = (uptime_seconds % (24 * 3600)) // 3600
    remaining_minutes = (uptime_seconds % 3600) // 60
    remaining_seconds = uptime_seconds % 60

    parts = []
    if days > 0:
        parts.append(f"{days} {'day' if days == 1 else 'days'}")
    if remaining_hours > 0:
        parts.append(f"{remaining_hours} {'hour' if remaining_hours == 1 else 'hours'}")
    if remaining_minutes > 0:
        parts.append(
            f"{remaining_minutes} {'minute' if remaining_minutes == 1 else 'minutes'}"
        )
    if remaining_seconds > 0:
        parts.append(
            f"{remaining_seconds} {'second' if remaining_seconds == 1 else 'seconds'}"
        )

    message = "Uptime: " + ", ".join(parts)
    return message


async def server_status(payload: MonitorPayload, local_mode=False) -> Dict[str, Any]:
    try:
        db_uri = next(
            (s["default"] for s in payload["settings"] if s["label"] == "db_uri"), None
        )
        if not db_uri:
            raise ValueError("Database URI not found in settings")

        database = db_uri.split("/")[-1]

        client = MongoClient(db_uri)
        db = client[database]
        server_status = db.command("serverStatus")
        print(f"Server Status: {server_status}")
        if not server_status:
            raise Exception("Failed to retrieve server status")

        # Uptime
        uptime_seconds = server_status["uptime"]

        # Connections
        current_connections = server_status["connections"]["current"]
        available_connections = server_status["connections"]["available"]

        # Operation counters
        opcounters = server_status["opcounters"]
        query_count = opcounters["query"]
        update_count = opcounters["update"]
        insert_count = opcounters["insert"]
        delete_count = opcounters["delete"]

        message = (
            f"🚀 {format_uptime_message(uptime_seconds)}\n"
            f"🔗 Connections: {current_connections} / {available_connections} available\n"
            f"🖥️ Memory Usage: {server_status['mem']['resident']} MB / {server_status['mem']['virtual']} MB\n"
            "\n📊 Operation Counters:\n"
            + "\n".join(
                [
                    f"   📌 Queries: {query_count}",
                    f"   ✏️ Updates: {update_count}",
                    f"   📥 Inserts: {insert_count}",
                    f"   🗑️ Deletes: {delete_count}",
                ]
            )
        )

        data = {
            "message": message,
            "username": "dbPulse",
            "event_name": "Database Status",
            "status": "success",
        }
        print(data)
        # Post data to telex
        if not local_mode:
            requests.post(payload["return_url"], json=data)
    except Exception as e:
        error_msg = f"MongoDB server status failed: {str(e)}"
        print(error_msg)

        # Notify of failure
        if not local_mode:
            try:
                requests.post(
                    payload["return_url"],
                    json={
                        "message": error_msg,
                        "username": "dbPulse",
                        "event_name": "Database Status",
                        "status": "error",
                    },
                )
            except Exception as e:
                print(f"Failed to send error notification: {str(e)}")
        return {"error": error_msg}
