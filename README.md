# Manchester United Twitter Bot 🤖
[![PyPI Version](https://img.shields.io/pypi/v/tweepy?label=PyPI)](https://pypi.org/project/tweepy/)
[![Python Versions](https://img.shields.io/pypi/pyversions/tweepy?label=Python)](https://pypi.org/project/tweepy/)
[![Twitter API v2](https://img.shields.io/endpoint?url=https%3A%2F%2Ftwbadges.glitch.me%2Fbadges%2Fv2)](https://developer.twitter.com/en/docs/twitter-api)
[![Twitter API v2](https://img.shields.io/twitter/follow/FabrizioUTDBot?style=social)](https://twitter.com/FabrizioUTDBot)

This project is a continuation of the Fabrizio Romano BOT (https://github.com/abmoh95/Fabrizio_Romano_ManUTD_Bot). This project will live tweet about Manchester United Live Scores, fixtures and game events.


## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
This bot parses information from an API, the free tier allows a user to make 100 requests every 24h. The requested information is then saved into a json file whereby the twitter followers get live updates about ongoing Manchester United games. Among the updates include; Goals, Substitutions, Yellow and Red Cards. 

Since the API allows 100 requests for its free tier program, a slight delay (max 2 min) has been included into the script to allow the requests to span throughout a whole game.

If the desired outcome is more frequent requests, a web scraping solution, Sofascore, might be a better option unless the preferance is buying thier extension package.
	
## Technologies
Project is created with:
* Python-3.8
* Twitter developer account
* Insomnia API - Webscraping 
* Twitter API V2
* Google Cloud Platform (either Google Function or in my case Google Cloud VM).

	
## Setup
To run this project, install it locally:

```
$ sudo apt update
$ sudo apt install python3-pip
$ pip3 install tweepy
$ python3 football_UTD_twitter.py
```
Links
-----

- [Tweepy documentation](https://tweepy.readthedocs.io/en/latest/)
- [Google Cloud Platform](https://cloud.google.com/)
- [Twitter API Documentation](https://developer.twitter.com/en/docs/twitter-api)
- [Sofascore](https://www.sofascore.com/football/livescore)
- [API-FOOTBALL (3.9.2)](https://www.api-football.com/documentation-v3)
- [Insomnia rest](https://insomnia.rest/)
