from django.shortcuts import render

from home.api import get_news_from_api
from .models import Articles
# Create your views here.
def home(request):
    # url = 'https://newsapi.org/v2/everything?q=tesla&from=2022-08-23&sortBy=publishedAt&apiKey=060b3b45d5ae4fe7a53d648e73914ce7'
    # get_ne{{ws_from_api(url)
    context={
        'articles' : Articles.objects.all()
    }
    return render(request,'home.html',
        context={
        'articles' : Articles.objects.all()
    }
    )