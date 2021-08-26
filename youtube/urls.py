
from django.urls import path

import youtube
from youtube import views

urlpatterns = [
    path('',views.index,name='index'),
    path('fetch/',views.fetch_query,name='fetch-query'),
    

]
