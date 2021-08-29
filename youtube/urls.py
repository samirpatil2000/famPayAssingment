
from django.urls import path

import youtube
from youtube import views

urlpatterns = [
    path('',views.index,name='index'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('fetch/',views.fetch_query,name='fetch-query'),
    path('video/<int:id>',views.detail,name='detail'),
    path('delete_video/<int:id>',views.delete_API,name='delete'),


]
