import requests
import json
import sys

url = "https://youtube-downloader9.p.rapidapi.com/"

headers = {
    'x-rapidapi-host': "youtube-downloader9.p.rapidapi.com",
    'x-rapidapi-key': "578b771870mshea19d8ae701033fp1db6d1jsnc270e20be7bf"
    }

def main():
#   video_format = input()
#   video_id = input()
#   video_url = url + video_id + "/" + video_format
  video_url = url + sys.argv[2] + "/" + sys.argv[1] 
  print(video_url)
  response = requests.request("GET", video_url, headers=headers)
  video = response.json()[0]["url"]
  print(video)


if __name__ == "__main__":
    main()
