from django.db import models

# Create your models here.
from django.urls import reverse

dummy_youtube_response = {
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

class Category(models.Model):
    name = models.CharField(max_length=30,unique=True)
    def __str__(self):
        return self.name

class API(models.Model):
    name = models.CharField(max_length=200,blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    date_published = models.DateTimeField(blank=True,null=True)
    date_created = models.DateTimeField(auto_now=True,null=True,blank=True)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,blank=True,null=True)
    thumbnail_url = models.URLField(blank=True)
    channel_name = models.CharField(max_length=50,blank=True,null=True)
    videoId = models.SlugField(unique=True,max_length=30)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail',kwargs={'id':self.id})