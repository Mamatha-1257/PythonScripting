import urllib.request, json
from selenium import webdriver
import time

def lookForNewVideo():

    apiKey = "AIzaSyD_89wjl46BivR_IwihKbFl-MJu4moVtSg"

    channelId = "UCiWphW3UbbuG7FR3sAr3b0A"

    baseVideoUrl = "https://www.youtube.com/watch?v="
    baseSearchUrl = "https://www.googleapis.com/youtube/v3/search?"

    URL = baseSearchUrl + 'key={}&channelId={}&part=snippet,id&order=date&maxResults=1'.format(apiKey, channelId)
    #inp = urllib.request.urlopen(url)
    #resp = json.loads(inp.read())

    with urllib.request.urlopen(URL) as url:
        data = json.loads(url.read().decode())

    vidID = resp['items'][0]['id']['videoId']

    videoExists = False

    with open('videoid.json', 'r') as json_file:
        data = json.load(json_file)

    if data['videoId'] != vidID:

        driver = webdriver.Firefox()
        driver.get(baseVideoUrl + vidID)
        videoExists = True

    if videoExists:
        with open('videoid.json', 'w') as json_file:
            data = {"videoId": vidID}
            json.dump(data, json_file)



try:
    while True:
        lookForNewVideo()
        time.sleep(10)
except KeyboardInterrupt:
    print('sleeping')






