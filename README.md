<h1 align="center"> Notion-Email Integration </h1>

### Introduction

Fetch data from notion database and send daily reminders to gmail

### Installation & Usage

##### Install the required packages
```bash
git clone https://github.com/yydderf/notion-mail.git
cd notion-mail
mkdir venv
python3 -m venv venv
python3 -m pip install -r requirements.txt
```

##### Direct Execution
```bash
source venv/bin/activate
python3 worker.py
```

##### Cron

> [!WARNING]
> Execute directly to generate `token.json` before using cron

Edit cronjobs
```bash
crontab -e
```

Append the following line to the file
```bash
0 10 * * * cd /path/to/the/project && venv/bin/python3 worker.py
```
(Refer to [Crontab guru](https://crontab.guru/) for cron schedule expressions)


### Configuration
- Get Credentials from Google and store `credentials.json` to the root directory
(refer to [Google OAuth](https://developers.google.com/workspace/guides/configure-oauth-consent))
- Get Secret from Notion and store the secret in `.env`
(refer to [Notion Integration](https://www.notion.so/my-integrations))
- Get Database ID from Notion and store the ID in `.env`
(refer to [Notion Database ID](https://developers.notion.com/reference/retrieve-a-database))
- Set up the _sender_, the _receiver_ and the _title_ of the email
```bash
NOTION_TOKEN=<your-notion-secret-token>
DATABASE_ID=<your-notion-database-id>

EMAIL_FROM=<email-sender-address>
EMAIL_TO=<email-receiver-address>
EMAIL_TITLE=<email-title>
```
