import os

import requests
import json
from decouple import config


def prompt_chat_gpt(message_content, model="gpt-3.5-turbo"):
    openai_api_key = os.environ.get("OPENAI_API_KEY")

    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {openai_api_key}"
    }

    data = {
        "model": model,
        "messages": [{"role": "user", "content": message_content}],
        "temperature": 0.7
    }

    response = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
    return response.json()
