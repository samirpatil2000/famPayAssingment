import json
import os
import sys

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from famPayAssingment.settings import DEVELOPER_KEY,YOUTUBE_API_SERVICE_NAME,YOUTUBE_API_VERSION

# Create your views here.
from googleapiclient.discovery import build

from .models import API

def index(request):
    template_name='youtube/index.html'
    fetch()
    return render(request,
                  template_name)

dummy_response={
  "kind": "youtube#searchListResponse",
  "etag": "yFy6-Kk0uH8hf8Dna0lMSzIS0L0",
  "nextPageToken": "CAIQAA",
  "regionCode": "IN",
  "pageInfo": {
    "totalResults": 29305,
    "resultsPerPage": 2
  },
  "items": [
    {
      "kind": "youtube#searchResult",
      "etag": "VNRBEy0vi17jqkNLVc4t0W9TY9c",
      "id": {
        "kind": "youtube#video",
        "videoId": "9fL3EtkSMGo"
      },
      "snippet": {
        "publishedAt": "2021-02-03T07:11:23Z",
        "channelId": "UCRMavOo7JR7rIMYIuIaoHRg",
        "title": "fampay kaise use kare 🔥 - zero balance account opening online without pan card | fampay card apply",
        "description": "FamPay India's first Neobank for teenagers. fampay me bina pan card ke account open karke upi set kar sakte hai. fampay me debit card bhi milta hai. is video ...",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/9fL3EtkSMGo/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/9fL3EtkSMGo/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/9fL3EtkSMGo/hqdefault.jpg",
            "width": 480,
            "height": 360
          }
        },
        "channelTitle": "ISHAN MONITOR",
        "liveBroadcastContent": "none",
        "publishTime": "2021-02-03T07:11:23Z"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "WOZ9InUJko24fxR9slUf6S08S9M",
      "id": {
        "kind": "youtube#video",
        "videoId": "L8ZDGnaULow"
      },
      "snippet": {
        "publishedAt": "2020-09-06T03:41:05Z",
        "channelId": "UC8U6KC0g_llcgNhnP4CIO0A",
        "title": "FamPay Card Unboxing &amp; FULL Review | India&#39;s First Debit Card For Teenagers!! | Tech With Varun |",
        "description": "Hiiii guys, In this video I have unboxed FamPay Debit Card and have shared my complete experience, the positives and negatives which I have faced in the past ...",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/L8ZDGnaULow/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/L8ZDGnaULow/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/L8ZDGnaULow/hqdefault.jpg",
            "width": 480,
            "height": 360
          }
        },
        "channelTitle": "Tech With Varun",
        "liveBroadcastContent": "none",
        "publishTime": "2020-09-06T03:41:05Z"
      }
    }
  ]
}


def fetch():
    query,max_results="FamPay",2
    try:
        request_to_youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                        developerKey=DEVELOPER_KEY)
        response = request_to_youtube.search().list(
            q=query,
            part='id,snippet',
            maxResults=max_results
        ).execute()
        # print(json.dumps(response))
        # print(type(response),''.join(['*']*40))
        title=[]
        for result in response.get('items',[]):
            if result['id']['kind'] == 'youtube#video':
                title.append(result['snippet']['title'])
                videoId=result['id']['videoId']
                try:
                    API.objects.get(videoId=videoId)
                except ObjectDoesNotExist:
                    date=result['snippet']["publishedAt"]
                    API.objects.create(
                        name=result['snippet']['title'],
                        description=result['snippet']['description'],
                        # date_published=result['snippet']['title'],
                        thumbnail_url=result['snippet']['thumbnails']['high']['url'],
                        channel_name=result['snippet']['channelTitle'],
                        videoId=videoId)
        print(title)



    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)

    # return redirect('index')