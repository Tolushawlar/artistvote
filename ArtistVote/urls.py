"""ArtistVote URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from voteapp import  views as voteViews 

urlpatterns = [
    path('', voteViews.home, name="Home"),
    path('<int:award_id>/', voteViews.vote, name='Vote'),
    path('vote_save', voteViews.voteSave, name="SaveVote"),
    path('<int:award_id>/results', voteViews.result, name='Results'),
    path('resultsdata/<int:data_id>/', voteViews.resultsData, name="ResultData"),
    path('about', voteViews.aboutUs, name="About"),
    path('admin/', admin.site.urls),
]
