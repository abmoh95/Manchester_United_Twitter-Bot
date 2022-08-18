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

Since the API allows 100 requests for its free tier program, a slight delay (max 2 min) has been included into the script to allow the requests to span throughout the whole game.

If the desired outcome is more frequent requests, a web scraping solution such as Sofascore might be a better option unless the preferance is buying the API providers extension package.

Unlike the previous bot which is hosted on Google cloud this bot is hosted on Amazon Web Services using their free tier EC2 product.
	
## Technologies
Project is created with:
* Python-3.8
* Twitter developer account
* Insomnia API - Webscraping 
* Twitter API V2
* Amazon Web Services (either Google Function or in my case Google Cloud VM).

	
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
- [Amazon Web Services](https://aws.amazon.com/free/?all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc&awsf.Free%20Tier%20Categories=categories%23compute&trk=4b76a70e-625f-48c4-b90e-cc5a1eadff15&sc_channel=ps&sc_campaign=acquisition&sc_medium=ACQ-P|PS-GO|Brand|Desktop|SU|Compute|EC2|ND|EN|Text|EU&s_kwcid=AL!4422!3!495059227888!e!!g!!amazon%20web%20services%20ec2&ef_id=Cj0KCQjwxveXBhDDARIsAI0Q0x3APuT3I2ySxDivnBSbT1cTHC-vazMmSsGTh5BVsS6onq66FJEs5XgaAoEQEALw_wcB:G:s&s_kwcid=AL!4422!3!495059227888!e!!g!!amazon%20web%20services%20ec2&awsf.Free%20Tier%20Types=*all)
- [Twitter API Documentation](https://developer.twitter.com/en/docs/twitter-api)
- [Sofascore](https://www.sofascore.com/football/livescore)
- [API-FOOTBALL (3.9.2)](https://www.api-football.com/documentation-v3)
- [Insomnia rest](https://insomnia.rest/)
