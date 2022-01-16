import json
import datetime
import jdatetime
import requests
from django.shortcuts import render
from .models import RecentActivity as RecentActivityModel
from scripts.ddg import DuckDuckGo

swear_words = requests.get(
    'https://raw.githubusercontent.com/amirshnll/Persian-Swear-Words/master/data.json').json()

def Main(request):
    if(request.GET.get('query')):

        results = DuckDuckGo().search(
            request.GET.get('query')
        )

        xff = request.META.get('HTTP_X_FORWARDED_FOR')
        ip = xff.split(',')[0] if xff else request.META.get('REMOTE_ADDR')
        if not RecentActivityModel.objects.filter(
                query=request.GET.get('query'),
                device=request.META.get('HTTP_USER_AGENT'),
                secret_ip=ip[:4]+('*'*(len(ip)-7))+ip[len(ip)-3:len(ip)]
            ).exists():
            RecentActivityModel.objects.create(
                query=request.GET.get('query'),
                device=request.META.get('HTTP_USER_AGENT'),
                secret_ip=ip[:4]+('*'*(len(ip)-7))+ip[len(ip)-3:len(ip)]
            )
        return render(request, 'result.html', {
            'query': request.GET.get('query'),
            'results': results
        })
    return render(request, 'index.html')

def RecentActivity(request):

    def get_platform(useragent):
        if 'android' in useragent.lower():
            return 'android'
        elif 'linux' in useragent.lower():
            return 'linux'
        elif 'windows' in useragent.lower():
            return 'win'
        elif 'safari' in useragent.lower():
            return 'osx'
        return 'unknown'
    
    def filter_query(query):
        for word in query.split():
            if word in swear_words['word']:
                query = query.replace(word, '*'*len(word))
        return query

    return render(request, 'recent.html', {
        'activities': [
            {
                'query': filter_query(activity.query),
                'device': activity.device,
                'platform': get_platform(activity.device),
                'secret_ip': activity.secret_ip,
                'timestamp': jdatetime.datetime(
                    activity.timestamp.year-622,
                    activity.timestamp.month,
                    activity.timestamp.day,
                    activity.timestamp.hour,
                    activity.timestamp.minute,
                    activity.timestamp.second,
                    locale='fa_IR').strftime("%a, %d %b %Y در ساعت %H:%M:%S")
            } for activity in RecentActivityModel.objects.filter(
                timestamp__gte=(datetime.datetime.now() - datetime.timedelta(days=1))
            )[::-1]
        ]
    })