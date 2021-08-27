import asyncio
import json
import os
import sys

import googleapiclient
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.shortcuts import render, redirect
from famPayAssingment.settings import DEVELOPER_KEY,YOUTUBE_API_SERVICE_NAME,YOUTUBE_API_VERSION,API_KEYS

# Create your views here.
from googleapiclient.discovery import build

from .models import API,Category
from .forms import FilterForm

def is_valid_params(param):
    return param!="" and param is not None

def index(request):
    template_name='youtube/index.html'
    # fetch()

    queryset=API.objects.all()

    category_id = request.GET.get('category')
    search_query = request.GET.get('name')

    which_query=[]
    if is_valid_params(search_query):
        search_query=search_query.split(" ")
        print(search_query)
        if len(search_query)>0:
            query=Q(name__icontains=search_query[0]) #|Q(description__icontains=search_query[0])
            for q in search_query[1:]:
                query =query | Q(name__contains=q) #| Q(description__icontains=q)
            queryset=queryset.filter(query)
            which_query.append(search_query)
    if is_valid_params(category_id):
        category_=Category.objects.get(id=int(category_id))
        print(category_)
        queryset = queryset.filter(category__name=category_)
        which_query.append(str(category_.name))

    context={
        'objects':queryset,
        'filterForm':FilterForm,
    }
    return render(request,
                  template_name,context)

def fetch_query(request):
    query = request.GET.get('fetch_query')
    if is_valid_params(query):
        category=Category.objects.get_or_create(name=query)
        fetch(category[0])
        messages.success(request,f'data successfully fetch for keyword {query}')
    return render(request,'youtube/fetch_data.html',context={})

def fetch_videos():
    categories = Category.objects.all()
    for cat in categories:
        fetch(query=cat.name)

def fetch(query="FamPay",max_results=2):
    query,max_results="FamPay",2
    retry=True
    response=None
    try:
        for key in API_KEYS:
            try:
                # import pdb;pdb.set_trace()
                request_to_youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,developerKey=key)
                response = request_to_youtube.search().list(q=query,part='id,snippet',maxResults=max_results).execute()
                print(response)
                retry=False

            except googleapiclient.errors.HttpError as e:
                # s=[{'message': 'The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.',
                #      'domain': 'youtube.quota', 'reason': 'quotaExceeded'}]
                print(e,"THE expection")
            if not retry:
                break

        if response:
            title=[]
            try:
                category=Category.objects.get(name=query)
            except ObjectDoesNotExist:
                category=Category.objects.create(name=query)
            response={'items':[]}
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
                            category=category,
                            videoId=videoId)
            print(title)
        else:
            # messages.error(,"")
            raise

    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)

    # return redirect('index')


def detail(request,id):
    context = {
        'object':API.objects.get(id=id)
    }
    return render(request,'youtube/detail.html',context)

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
