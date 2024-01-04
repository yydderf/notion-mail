import os
from dotenv import load_dotenv
from notion_client import Client, APIErrorCode, APIResponseError
from datetime import datetime
from pprint import pprint

load_dotenv()

today = datetime.now().strftime("%Y-%m-%d")
filter = {
    "and": [
        {
        "property": "完成",
        "checkbox": {
            "equals": False
            }
        },
        {
        "property": "Date",
        "date": {
            "equals": today
            }
        }
    ]
}

def query(notion_client: Client, filter: dict) -> dict:
    json_data = {}
    try:
        my_page = notion_client.databases.query(
            **{
                "database_id": os.environ["DATABASE_ID_JAC"],
                "filter": {
                    "and": [
                        {
                            "property": "完成",
                            "checkbox": {
                                "equals": False
                                }
                            },
                        {
                            "property": "Date",
                            "date": {
                                "equals": today
                                }
                            }
                        ]
                }
            }
        )
        # pprint(my_page)
        json_data = my_page
    except APIResponseError as e:
        if e.code == APIErrorCode.ObjectNotFound:
            print("Object Not Found")
        else:
            print(e)
    return json_data
