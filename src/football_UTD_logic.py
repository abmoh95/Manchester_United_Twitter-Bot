import json
import http.client
from tkinter import E
from turtle import home
from urllib import response
from pprint import pprint
import csv
import datetime
import time
import BOT_config

emoji_dict = {"Time": '\U0001f551', "Yellow-Bell" : '\U0001f514', "Red Card" : '\U0001f7e5',
         "Yellow Card" : '\U0001f7e8', "Goal" : '\u26bd', "Substitutions" : '\U0001f504'}

def team_info():
    try:
        f = open('gameEvents.json')
        data = json.load(f)
        str_ = ""
        for team in data["response"]:
            tournament = team["league"]["name"]
            homeTeam = team["teams"]["home"]["name"]
            homeTeam_score = team["goals"]["home"]
            awayTeam_score = team["goals"]["away"]
            awayTeam = team["teams"]["away"]["name"]
            str_ = f"Hometeam: {homeTeam} [{homeTeam_score}] - Awayteam: {awayTeam} [{awayTeam_score}]"
            return str_, tournament
    except Exception as e:
        print(f"team_info {e}")
        return None, None

def ManUtd_Schedule():
    for i in range(3):
        print(f"MAN UTD SCHEDULE : i-value: {i}")
        headers = {
        'x-rapidapi-host': "v3.football.api-sports.io",
        'x-rapidapi-key': BOT_config.x_rapidapi_key
        }
        conn = http.client.HTTPSConnection("v3.football.api-sports.io")
        try:
            conn.request(
                "GET", f"/fixtures?team=75&season={datetime.date.today().year}&timezone=Europe/Stockholm", headers=headers)

            res = conn.getresponse()
            json_data = res.read()
            json_data = json_data.decode("utf-8")

            Json_file = json.loads(json_data)
            
            #check if we have proper response 
            if Json_file["results"] == 0:
                raise Exception

            # Ensure ascii = false removes unicode characters such as \u010d
            with open('UTD_schedule.json', 'w') as outf:
                json.dump(Json_file, outf, indent=4, ensure_ascii=False)

            with open('football_schedule.csv', 'w') as outfile:
                f = open("UTD_schedule.json")
                data = json.load(f)
                for item in data["response"]:
                    homeTeam = item["teams"]["home"]["name"]
                    awayTeam = item["teams"]["away"]["name"]
                    league = item["league"]["name"]
                    venue = item["fixture"]["venue"]["name"]
                    city = item["fixture"]["venue"]["city"]
                    fixtureID = item["fixture"]["id"]
                    game_Date_Time = item["fixture"]["date"].split('T')
                    gameDate = game_Date_Time[0]
                    gameTime = game_Date_Time[1]
                    writer = csv.writer(outfile)
                    jason_data = [league, homeTeam, awayTeam,
                                venue, city, fixtureID, gameDate, gameTime]
                    writer.writerow(jason_data)
            return
        except Exception as e:
            print(f"Man UTD schedule - {e}")
            continue
    print("Schedule is not retrievable at this moment")
    return

def parse_teaminfo():
    str_ = ""
    try:
        with open('football_schedule.csv') as outfile:
            reader = csv.reader(outfile)
            for i in reader:
                t = datetime.date.today()
                t = t.strftime('%Y-%m-%d')
                if i[6] == t:
                    tournament = i[0]
                    homeTeam = i[1]
                    awayTeam = i[2]
                    city = i[4]
                    str_+= f"{tournament} H: {homeTeam} A: {awayTeam} City: {city}"
                    return str_
    except Exception as e:
        print(f"parse_teaminfo() {e}")
        return str_

def check_Games_Today():
    try:
        with open('football_schedule.csv') as outfile:
            reader = csv.reader(outfile)
            for i in reader:
                match_date = datetime.datetime.strptime(i[6], "%Y-%m-%d")
                match_date = match_date.date()
                if match_date == datetime.date.today():
                    gameTime = i[7]
                    gameTime = datetime.datetime.strptime(i[7], "%H:%M:%S%z")
                    gameTime = gameTime.time()
                    fixture_ID = i[5]
                    return gameTime, fixture_ID
            return False
    except Exception as e:
        print(f"Error check_Games_Today: {e}")
        return False

def teamLineUp(fixture_id):
    Lineup_Today = []
    
    for i in range(3):
        print(f"Lineup : i-value: {i}")
        headers = {
        'x-rapidapi-host': "v3.football.api-sports.io",
        'x-rapidapi-key': BOT_config.x_rapidapi_key
        }
        conn = http.client.HTTPSConnection("v3.football.api-sports.io")
        try:
            conn.request(
                "GET", f"/fixtures/lineups?fixture={fixture_id}", headers=headers)

            res = conn.getresponse()
            data = res.read()
            data = data.decode("utf-8")
            Json_file = json.loads(data)

            #check if we have proper response 
            if Json_file["results"] == 0:
                raise Exception("Nått är fel")

            # Ensure ascii = false removes unicode characters such as \u010d
            with open('UTD_lineup.json', 'w') as outf:
                json.dump(Json_file, outf, indent=4, ensure_ascii=False)

            if not Json_file["response"]:
                print("startXI is not available")
                return Lineup_Today

            for item in Json_file["response"]:
                team_name = item["team"]["name"]
                Lineup_Today.append('\U0001f6a8')
                Lineup_Today.append("Team News")
                Lineup_Today.append('\U0001f6a8')
                Lineup_Today.append(team_name)
                for player in item["startXI"]:
                    playerName = player["player"]["name"]
                    Lineup_Today.append(playerName)
                Lineup_Today.append(' ')
            pprint(Lineup_Today)
            return Lineup_Today

        except Exception as e:
            print(f"Lineup: {e}")
            time.sleep(3)
    print("Team lineup was not possible AT THIS TIME")
    return Lineup_Today

def split_lineup(fixture_ID):
    try:
        Lineup_Today = teamLineUp(fixture_id=fixture_ID)
        lineup1 = []
        lineup2 = []
        x = 999
        for i in range(len(Lineup_Today)):
            if Lineup_Today[i] == " ":
                x = i
                continue
            else:
                if x > i:
                    lineup1.append(Lineup_Today[i])
                else:
                    lineup2.append(Lineup_Today[i])
        return lineup1, lineup2
    except Exception as e:
        print(f"Split lineup: {e}")

            

def game_Events(fixture_ID):
    for i in range(3):
        print(f"Event : i-value: {i}")
        headers = {
        'x-rapidapi-host': "v3.football.api-sports.io",
        'x-rapidapi-key': BOT_config.x_rapidapi_key
        }
        conn = http.client.HTTPSConnection("v3.football.api-sports.io")
        print(f"Fixture_ID: {fixture_ID}")
        try:
            conn.request("GET", f"/fixtures?id={fixture_ID}&timezone=Europe/Stockholm", headers=headers)

            res = conn.getresponse()
            data = res.read()
            data = data.decode("utf-8")
            Json_file = json.loads(data)

            #check if we have proper response 
            if Json_file["results"] == 0:
                raise Exception

            # Ensure ascii = false removes unicode characters such as \u010d
            with open('gameEvents.json', 'w') as outf:
                json.dump(Json_file, outf, indent=4, ensure_ascii=False)

            f = open('gameEvents.json')
            data = json.load(f)

            event_List = []
            game_Status_long = None
            game_Status_short = None
            for item in data["response"]:
                for i in item["events"]:
                    extra = i["time"]["extra"]
                    if extra == None:
                        time_event = i["time"]["elapsed"]
                    else:
                        time_event = i["time"]["elapsed"] + extra

                    teamName_event = i["team"]["name"]
                    playerName_event = i["player"]["name"]
                    typeEvent_type = i["type"]
                    typeEvent_detail = i["detail"]
                    assist = i["assist"]["name"]
                    typeEvent_event = event_details(typeEvent_type, typeEvent_detail)
                    score_update = ""
                    if typeEvent_type == "Goal":
                        if assist != None:
                            score_update, tournament = team_info()
                            str_comp1 = f"{time_event}' : {teamName_event} : {playerName_event} : Assist {assist} : {typeEvent_event} \n"
                            ans = check_file_content(str_comp1)
                            if ans == False:
                                str_comp1 += score_update
                        else:
                            score_update, tournament = team_info()
                            str_comp1 = f"{time_event}' : {teamName_event} : {playerName_event} : {typeEvent_event} \n"
                            ans = check_file_content(str_comp1)
                            if ans == False:
                                str_comp1 += score_update
                    elif typeEvent_type == "subst":
                        if assist != None:
                            str_comp1 = f"{time_event}' : {teamName_event} : In {playerName_event} : Out {assist} : {typeEvent_event}"
                        else:
                            str_comp1 = f"{time_event}' : {teamName_event} : In {playerName_event} : {typeEvent_event}"
                    else:
                        str_comp1 = f"{time_event}' : {teamName_event} : {playerName_event} : {typeEvent_event}"

                    event_List.append(str_comp1)
                    game_Status_short = item["fixture"]["status"]["short"]
                    game_Status_long = item["fixture"]["status"]["long"]
            return event_List, game_Status_short, game_Status_long

        except Exception as e:
            print(f"Requests.exceptions - Game event: {e}")
            time.sleep(3)
            #return None, None, None

    print("Team-Events was not possible AT THIS TIME")

def check_file_content(str_):
    try:
        with open('utt1.txt', 'r') as oo:
            if str_ in oo.read():
                return True
            else:
                return False
    except Exception as e:
        print(f"check_file_content {e}")

def event_details(typeEvent_type, typeEvent_detail):
    str_ = ""
    if typeEvent_type == "Goal":
        if typeEvent_detail == "Normal Goal":
            str_ += typeEvent_detail
            str_ += " \u26bd"
            return str_
        elif typeEvent_detail == "Own Goal":
            str_ += typeEvent_detail
            str_ += " \u26bd"
            return str_
        elif typeEvent_detail == "Penalty":
            str_ += typeEvent_detail
            str_ += " \U0001f945"
            return str_
        elif typeEvent_detail == "Missed Penalty":
            str_ += typeEvent_detail
            str_ += " \u26d4\U0001f945"
            return str_
    elif typeEvent_type == "Card":
        if typeEvent_detail == "Yellow Card":
            str_ += typeEvent_detail
            str_ += " \U0001f7e8"
            return str_
        elif typeEvent_detail == "Second Yellow Card":
            str_ += typeEvent_detail
            str_ += " \U0001f7e8\U0001f7e8"
            return str_
        elif typeEvent_detail == "Red Card":
            str_ += typeEvent_detail
            str_ += " \U0001f7e5"
            return str_
        
    elif typeEvent_type == "subst":
        str_ += typeEvent_detail
        str_ += " \U0001f504"
        return str_
    else:
        return typeEvent_detail

def main():

    #team_info()
    ManUtd_Schedule()
    # print(check_Games_Today())
    #game_Events(924430)
    # print(ans)
    # pprint(event_List)
    #teamLineUp(234234234)
    #split_lineup(877947)
    #parse_teaminfo()


if __name__ == "__main__":
    main()
