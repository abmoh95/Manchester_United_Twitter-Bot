import sys
import tweepy
import time
import datetime
import schedule
import authen_Keys.BOT_config as BOT_config
import json
import http.client
from urllib import response
from pprint import pprint
import csv
import textwrap
import math

import football_UTD_logic


ACCESS_KEY = BOT_config.ACCESS_KEY
ACCESS_SECRET = BOT_config.ACCESS_SECRET
CONSUMER_KEY = BOT_config.CONSUMER_KEY
CONSUMER_SECRET = BOT_config.CONSUMER_SECRET


client = tweepy.Client(bearer_token=BOT_config.BEARER_TOKEN,
                       access_token=ACCESS_KEY,
                       access_token_secret=ACCESS_SECRET,
                       consumer_key=CONSUMER_KEY,
                       consumer_secret=CONSUMER_SECRET)


# authentication
auth = tweepy.OAuthHandler(BOT_config.CONSUMER_KEY, BOT_config.CONSUMER_SECRET)
auth.set_access_token(BOT_config.ACCESS_KEY, BOT_config.ACCESS_SECRET)

api = tweepy.API(auth)


def check_If_gameToday():
    #print("Checking game today")
    if football_UTD_logic.check_Games_Today() != False:
        gameTime, fixture_ID = football_UTD_logic.check_Games_Today()
        gameTimeInit_seconds = (gameTime.hour * 3600) + \
            (gameTime.minute * 60) + (gameTime.second)
        print(gameTimeInit_seconds)
        time_now = datetime.datetime.now().time()
        time_now_sec = (time_now.hour * 3600) + \
            (time_now.minute * 60) + (time_now.second)

        # Wait 20 min (1200 [s]) before gametime for lineup to be available
        timeleftUntilGame = gameTimeInit_seconds - 1200 - time_now_sec
        print(timeleftUntilGame)
        if timeleftUntilGame > 0:
            time.sleep(timeleftUntilGame)
            home_Lineup, away_Lineup = football_UTD_logic.split_lineup(fixture_ID=fixture_ID)
        else:
            home_Lineup, away_Lineup = football_UTD_logic.split_lineup(fixture_ID=fixture_ID)
        str_1 = ""
        str_1 = ' '.join(home_Lineup)
        check_file_content(str_1)
        str_2 = ""
        str_2 = ' '.join(away_Lineup)
        check_file_content(str_2)
        InGameEvents(gameTime=gameTime, fixture_ID=fixture_ID)

    else:
        #print("No game today")
        return None, None


def InGameEvents(gameTime, fixture_ID):
    event_LIST = []

    gameTimeInit_seconds = (gameTime.hour * 3600) + \
        (gameTime.minute * 60) + (gameTime.second)
    time_now = datetime.datetime.now().time()
    time_now_sec = (time_now.hour * 3600) + \
        (time_now.minute * 60) + (time_now.second)
    timeleftUntilGame = gameTimeInit_seconds - time_now_sec
    if timeleftUntilGame > 0:
        time.sleep(timeleftUntilGame)
    print()
    teamInfo = football_UTD_logic.parse_teaminfo()
    Kickoff_str = f"\U0001f514 KICK OFF {teamInfo} \U0001f514"
    ans = check_file_content(Kickoff_str)
    if ans == False:
        print(
            f"\U0001f514 KICK OFF {datetime.datetime.now().date()} \U0001f514")

    for i in range(120):
        event_LIST, game_Status_short, game_Status_long = football_UTD_logic.game_Events(
            fixture_ID=fixture_ID)
        if (event_LIST == None) and (game_Status_long == None) and (game_Status_short == None):
            return

        for i in event_LIST:
            ans = check_file_content(i)
            if ans == True:
                continue

        ans = check_game_Status(game_Status_short)
        #print(f"game status: {ans} {game_Status_short}")
        if (ans == False) or (ans == None):
            time.sleep(120)
        else:
            break
    match_result, tournament = football_UTD_logic.team_info()
    fullTime_str_ = f"\U0001f514 {game_Status_long} {tournament} {match_result} \U0001f514"
    print(fullTime_str_)
    if game_Status_long == None:
        return
    ans = check_file_content(fullTime_str_)
    return


'''
TBD : Time To Be Defined NS : Not Started 1H : First Half, Kick Off 
HT : Halftime 2H : Second Half, 2nd Half Started ET : Extra Time P : Penalty In Progress 
FT : Match Finished AET : Match Finished After Extra Time PEN : Match Finished After Penalty 
BT : Break Time (in Extra Time) SUSP : Match Suspended INT : Match Interrupted 
PST : Match Postponed CANC : Match Cancelled ABD : Match Abandoned AWD : Technical Loss 
WO : WalkOver LIVE : In Progress *
'''


def check_game_Status(game_Status):
    endgame = ['FT', 'AED', 'PEN', 'PST', 'CANC',
               'ABD', 'AWD', 'WO', 'SUSP', 'INT']
    if game_Status in endgame:
        #print("Game status: " + game_Status)
        return True
    elif game_Status == None:
        return None
    else:
        #print("Game status: " + game_Status)
        return False


def check_file_content(str_):
    with open('GameInfo.txt', 'r') as oo:
        if str_ in oo.read():
            return True

    with open('GameInfo.txt', 'a+') as oo:
        #print(str_)
        c = oo.write(str_ + "\n")
        #create_tweet(str_=str_)
        return False


def wait_until(end_datetime):
    while True:
        diff = (end_datetime - datetime.now()).total_seconds()
        if diff < 0:
            return       # In case end_datetime was in past to begin with
        time.sleep(diff/2)
        if diff <= 0.1:
            return


def update_gameSchedule():
    football_UTD_logic.ManUtd_Schedule()


def clear_event_file():
    with open('GameInfo.txt', 'w') as f:
        f.close()


# Algo provided by link below. With a few modifications to work with this project.
# https://stackoverflow.com/questions/67553176/how-to-possibly-tweet-more-than-280-chars-so-if-string-280-print-first-280-c

tweets = [
        'Four score and seven years ago our fathers brought forth upon this continent, a new nation, conceived in Liberty, '
        'and dedicated to the proposition that all men are created equal. Now we are engaged in a great civil war, '
        'testing whether that nation, or any nation so conceived and so dedicated, can long endure. We are met on a '
        'great battle-field of that war. We have come to dedicate a portion of that field, as a final resting place for those '
        'who here gave their lives that that nation might live. It is altogether fitting and proper that we should '
        'do this. But, in a larger sense, we can not dedicate—we can not consecrate—we can not hallow—this ground. '
        'The brave men, living and dead, who struggled here, have consecrated it, far above our poor power to add or detract. '
        'The world will little note, nor long remember what we say here, but it can never forget what they did here. '
        'It is for us the living, rather, to be dedicated here to the unfinished work which they who fought here have '
        'thus far so nobly advanced. It is rather for us to be here dedicated to the great task remaining before us—that '
        'from these honored dead we take increased devotion to that cause for which they gave the last full measure of '
        'devotion—that we here highly resolve that these dead shall not have died in vain—that this nation, under God, '
        'shall have a new birth of freedom—and that government of the people, by the people, for the people, shall '
        'not perish from the earth. —Abraham Lincoln']

twitter_handle = ['@ManUtd']

def create_tweet(str_):
    str_1 = [str_]
    try:
        for handle in twitter_handle:
            handle_length = len(handle)
            for tweet in str_1:
                # obtain length of tweet, which is 1471 characters
                tweet_length = len(tweet)

                # check length
                if tweet_length <= 280:
                    original_tweet = api.update_status(status=tweet)
                    
                elif tweet_length >= 280:
                    # divided tweet_length / 280
                    # You might consider adjusting this down
                    # depending on how you want to format the
                    # tweet.
                    tweet_length_limit = tweet_length / 280

                    # determine the number of tweets
                    # math.ceil is used because we need to round up
                    tweet_chunk_length = tweet_length / \
                        math.ceil(tweet_length_limit) + handle_length

                    # chunk the tweet into individual pieces
                    tweet_chunks = textwrap.wrap(tweet,  math.ceil(
                        tweet_chunk_length), break_long_words=False)

                    # iterate over the chunks
                    for x, chunk in zip(range(len(tweet_chunks)), tweet_chunks):
                        if x == 0:
                            print(f'{handle} 1 of {len(tweet_chunks)} {chunk}')
                            original_tweet = api.update_status(
                                status=chunk)
                        else:
                            print(f'{handle} {x+1} of {len(tweet_chunks)} {chunk}')
                            reply1_tweet = api.update_status(status=chunk,
                                                            in_reply_to_status_id=original_tweet.id,
                                                            auto_populate_reply_metadata=True)
                            original_tweet = reply1_tweet
    except Exception as e:
        print(f"Exception create tweet: {e}")


schedule.every().day.at("02:30").do(clear_event_file)

schedule.every().day.at("02:35").do(update_gameSchedule)

schedule.every().day.at("03:00").do(check_If_gameToday)

while True:
    schedule.run_pending()
    time.sleep(10)