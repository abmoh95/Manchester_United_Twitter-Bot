import http.client
import json
import csv

conn = http.client.HTTPSConnection("api.sofascore.com")

payload = ""

conn.request("GET", "/api/v1/sport/football/events/live", payload)

def sofascore_example():
    res = conn.getresponse()
    data = res.read()

    data = data.decode("utf-8")

    Json_file = json.loads(data)
    print(type(Json_file))


    with open('outputfile_restApi.json', 'w') as outfile:
        json.dump(Json_file, outfile, indent=4, ensure_ascii=False)

def main():
    sofascore_example()

if __name__ == "__main__":
    main()