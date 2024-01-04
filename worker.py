import os
from dotenv import load_dotenv
from notion_client import Client
from models.models import Event
from helper.notion import query
from helper.mail   import gmail_send_message
from datetime import datetime

load_dotenv()

notion = Client(auth=os.environ["NOTION_TOKEN"])

emoji_map = {
    "Remind": "⏰",
    "Meeting / Event": "🔥",
}

if __name__ == "__main__":
    data = query(notion, filter)
    results = data["results"]
    task_list = {}
    message = ""
    for result in results:
        title = result["properties"]["Tasks"]["title"][0]["plain_text"]
        time  = result["properties"]["Date"]["date"]["start"]
        isotime = datetime.fromisoformat(time).strftime("%H:%M")
        type_ = result["properties"]["類型"]["select"]
        type_color = type_["color"]
        type_name = type_["name"]
        if task_list.get(type_name, []) == []:
            task_list[type_name] = []
        task_list[type_name].append(Event(title=title, time=isotime))

    for event_type, event_list in task_list.items():
        message += "{} {} ({})\n".format(emoji_map.get(event_type, '✨'), event_type, len(event_list))
        for event in event_list:
            message += "- {} | {}\n".format(event.time, event.title)
        message += "\n"
    gmail_send_message(message)
