import googlemaps
import json
import urllib
import csv

def geocode(city):
    credsfile = open("../../Geo-Credentials/creds.txt", "r")
    AUTH_KEY = credsfile.read()

    url = ('https://maps.googleapis.com/maps/api/geocode/json'
           '?address=%s'
           '&key=%s') % (city.replace(' ', '+'), AUTH_KEY)

    response = urllib.request.urlopen(url)
    jsonRaw = response.read()
    jsonData = json.loads(jsonRaw)
    return jsonData

def writeToCSV():
    f = open('cities.txt', 'r')
    fn = "test.csv"
    with open(fn, mode = 'w', newline = '') as csv_test:
        csv_writer = csv.writer(csv_test, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
        for l in f:
            retData = geocode(l[:-1])
            if retData['status'] == 'OK':
                print(retData['results'][0]['geometry']['location'])
                csv_writer.writerow([l[:-1],
                    retData['results'][0]['geometry']['location']['lat'],
                    retData['results'][0]['geometry']['location']['lng']])
            else:
                print("oopsie poopsie")
        f.close()

def main():
    writeToCSV()
main()
