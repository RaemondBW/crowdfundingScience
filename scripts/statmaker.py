import json
import urllib2
f = open("kickstarter.json")
d = json.load(f)
f.close()
my_key = "AIzaSyAUVSPhAtIV3vKtKilq8JcMH-QFZd-9Ep0"
projectSizes = {}
locationInfo = {}
locLat = {}
successfulProjects = 0
totalProjects = 0

f = open("geocoord.txt")
for line in f.readlines():
    location, latlon = line.split(":")
    locLat[location] = latlon


for project in d:
    location = project["location"]
    amountRaised = float(project["totalPledged"])
    name = project["title"]
    goal = float(project["goal"])
    if location in locationInfo:
        locationInfo[location]["raised"] += amountRaised
        locationInfo[location]["numProjects"] += 1
        locationInfo[location]["successful"] += int(amountRaised >= goal)
    else:
        skip = False
        if location not in locLat:
            continue
        info = {}
        info["raised"] = amountRaised
        info["numProjects"] = 1
        info["successful"] = int(amountRaised >= goal)
        #url = "https://maps.googleapis.com/maps/api/geocode/json?address=" + location.replace(" ", "+") + "&sensor=false&key=AIzaSyAUVSPhAtIV3vKtKilq8JcMH-QFZd-9Ep0"
        #try:
        #    resultJson = json.load(urllib2.urlopen(url))
        #except UnicodeEncodeError:
        #    skip = True
        # if not skip:
        #     lat = resultJson["results"][0]["geometry"]["location"]["lat"]
        #     lon = resultJson["results"][0]["geometry"]["location"]["lng"]
        #     print location
        #     print (lat, lon)
        #     info["geocode"] = (lat, lon)
        #     locationInfo[location] = info
        info["geocode"] = locLat[location]
        locationInfo[location] = info

    info = {}
    info["succesful"] = amountRaised >= goal
    info["raised"] = amountRaised
    projectSizes[name] = info

    if amountRaised >= goal:
        successfulProjects += 1

    totalProjects += 1

print "percentage of successful projects: " + str(float(successfulProjects)/totalProjects)

f = open("byLocation.json", 'w')
f.write(json.dumps(locationInfo, indent=4))
f.close()

f = open("projectSizes.json", 'w')
f.write(json.dumps(projectSizes, indent=4))
f.close()
