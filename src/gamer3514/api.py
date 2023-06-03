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
def texttobraille(text: str):
    """
    Convert text to braille.\n
    Parameters:\n
    • text: The text you want to convert\n\n
    """
    url=f"https://api.sillychat.tech/texttobraille?text={text}"
    response = requests.get(url)
    if response.status_code == 200:
        result = json.loads(response.text)
        if result[0]['Error'] == 'True':
            raise Exception(result[0]['ErrorInfo'])
        else:
            return result[0]['Braille']
    raise Exception("Unknown error occured, please contact support")
def randomnumber(length: int):
    """
    Generate a random number.\n
    Parameters:\n
    • length: The length of the number you want to generate\n\n
    """
    url=f"https://api.sillychat.tech/randomnumber?length={length}"
    response = requests.get(url)
    if response.status_code == 200:
        result = json.loads(response.text)
        if result[0]['Error'] == 'True':
            raise Exception(result[0]['ErrorInfo'])
        else:
            return result[0]['number']
    raise Exception("Unknown error occured, please contact support")
def randomtopic():
    """
    Generate a random topic.
    """
    url=f"https://api.sillychat.tech/randomtopic"
    response = requests.get(url)
    if response.status_code == 200:
        result = json.loads(response.text)
        if result[0]['Error'] == 'True':
            raise Exception(result[0]['ErrorInfo'])
        else:
            return result[0]['topic']
    raise Exception("Unknown error occured, please contact support")
