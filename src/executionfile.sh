#!/bin/bash
echo Manchester United Live score updates and game events!
git clone git@github.com:abmoh95/Manchester_United_Twitter-Bot.git
pip install schedule
pip install tweepy
pip install emoji

python3 football_UTD_twitter.py