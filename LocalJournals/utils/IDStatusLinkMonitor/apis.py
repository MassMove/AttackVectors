import requests
import json

def spy_on_web(tag, token):
    api_link = 'https://api.spyonweb.com/v1/analytics/{analytics_code}?access_token={access_token}'
    request = api_link.format(analytics_code=tag, access_token=token, limit="100", start="0")
    response = requests.get(request)
    json_data = json.loads(response.text)
    return json_data


def publicwww(search_id, key):
    search_id = '"' + search_id + '"' 
    api_link = 'https://publicwww.com/websites/{search_id}/?export=csvu&key={api_key}'
    link = api_link.format(search_id=search_id, api_key=key)
    response = requests.get(link)

    rows = []
    for line in response.text.split("\n"):
        stripped = line.strip()
        if stripped is not None and stripped != "" :
            rows.append(line)
    return rows
