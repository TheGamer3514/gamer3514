# Gamer3514

A small package that does stuff

## Installation

```bash
pip install gamer3514
```

## Usage

### Api
```python
from gamer3514 import api
#NSFW Detection
api.detectnsfw(imageurl, apikey)
#Profanity Check
api.profanitycheck(text, apikey)
#Text To Braille
api.texttobraille(text)
#Random Number
api.randomnumber(length)
#Random Topic
api.randomtopic()
#Random Cat Image
api.cat(filepath, apikey)
#Random Cat Gif
api.catgif(filepath, apikey)
#Random Dog Image
api.dog(filepath, apikey)
#Donald Tweet
api.donaldtweet(filepath, text)
```

### Utils
```python
from gamer3514 import utils
#Get Random Number
utils.randomnumber()
#Generate Random Password
utils.genpassword(length)
```

### Random Stuff (No Category)
```python
from gamer3514 import randomstuff
#Huricane Speed To Category
randomstuff.hurricanecategory(speed)
#Random Number (Yes Again)
randomstuff.randomnumber()
#Screen Time Percentage
randomstuff.screentime(hours)
#Get Percentage
randomstuff.getpercentage(number, percentage)
#File Spam
randomstuff.filespam(filepath, sentence, amount)
#Print Spam
randomstuff.printspam(sentence, amount)
#Nice Print
randomstuff.niceprint(sentence)
```

## Resources

- [Discord server](https://discord.gg/3qvpkgWSbF)
- [Free hosting](https://sillydev.co.uk)
- Contact me: gamer@sillydev.co.uk