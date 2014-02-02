
import urllib2
import json

def printResults(data):
  theJSON = json.loads(data)

  for i in theJSON["features"]:
    if i["properties"]["mag"] >= 1.0:
      print "%2.1f" % i["properties"]["mag"]

def main():
  urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson"
  webUrl = urllib2.urlopen(urlData)
  if (webUrl.getcode() == 200):
    data = webUrl.read()
    printResults(data)
  else:
    print "Received an error from server, cannot retrieve results " + str(webUrl.getcode())

if __name__ == "__main__":
  main()
