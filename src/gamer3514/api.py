import requests
import json
def detectnsfw(imageurl: str, apikey: str):
    """
    Detect NSFW content in images.\n
    Parameters:\n
    • imageurl: The url of the image you want to scan\n
    • apikey: Your API key. You can get one at https://api.sillychat.tech\n\n

    """
    url=f"https://api.sillychat.tech/detectnsfw?url={imageurl}&key={apikey}"
    response = requests.get(url)
    if response.status_code == 200:
        result = json.loads(response.text)
        try:
            result['data']
            return result
        except:
            raise Exception(result[0]['ErrorInfo'])
    else:
        raise Exception("Unknown error occured, please contact support")
def profanitycheck(text: str, apikey: str):
    """
    Check if a text contains profanity.\n
    Parameters:\n
    • text: The text you want to scan\n
    • apikey: Your API key. You can get one at https://api.sillychat.tech\n\n
    """
    url=f"https://api.sillychat.tech/profanitycheck?key={apikey}&text={text}"
    response = requests.get(url)
    if response.status_code == 200:
        result = json.loads(response.text)
        if result[0]['Error'] == 'True':
            raise Exception(result[0]['ErrorInfo'])
        else:
            return result[0]['Profanity']
    raise Exception("Unknown error occured, please contact support")