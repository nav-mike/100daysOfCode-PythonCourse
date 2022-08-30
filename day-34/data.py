import requests
import html

# https://opentdb.com/api.php?amount=10&type=boolean


def api_question_data() -> list:
    response = requests.get("https://opentdb.com/api.php", params={"amount": 10, "type": "boolean"})
    response.raise_for_status()
    data = response.json()["results"]
    result = []
    for item in data:
        item["question"] = html.unescape(item["question"])
        result.append(item)
    return result


question_data = api_question_data()
