import http.client
import json
import csv

conn = http.client.HTTPSConnection("api.sofascore.com")

payload = ""

conn.request("GET", "/api/v1/sport/football/events/live", payload)

def func1():
    res = conn.getresponse()
    data = res.read()

    data = data.decode("utf-8")

    Json_file = json.loads(data)
    print(type(Json_file))


    with open('outputfile_restApi.json', 'w') as outfile:
        json.dump(Json_file, outfile, indent=4, ensure_ascii=False)

def func2():
    
    with open('restApi.csv', 'w') as outfile:
        csv.writer(outfile)
        str_ = "hejsan"
        outfile.write(str_)


def main():
    func1()
    func2()

if __name__ == "__main__":
    main()