from django.http import request
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from serpapi import GoogleSearch
from .models import RecentActivity as RecentActivityModel
from decouple import config

def Main(request):
    if(request.GET.get('query')):

        search = GoogleSearch({
            "q": request.GET.get('query'),
            "location": "Austin, Texas, United States",
            "hl": "en", "gl": "us", "google_domain": "google.com",
            "api_key": config("google_api_key", cast=str)
        })
        results = search.get_dict()

        xff = request.META.get('HTTP_X_FORWARDED_FOR')
        ip = xff.split(',')[0] if xff else request.META.get('REMOTE_ADDR')
    
        RecentActivityModel.objects.create(
            query=request.GET.get('query'),
            device=request.META.get('HTTP_USER_AGENT'),
            secret_ip=ip[:4]+('*'*(len(ip)-7))+ip[len(ip)-3:len(ip)]
        )
        return render(request, 'result.html', {
            'query': request.GET.get('query'),
            'results': results['organic_results'] if 'organic_results' in results else []
        })
    return render(request, 'index.html')

def RecentActivity(request):
    return JsonResponse({
        'activities': [
            {
                'query': activity.query,
                'device': activity.device,
                'secret_ip': activity.secret_ip,
                'timestamp': activity.timestamp.strftime('%Y-%m-%d %H:%M:%S')
            } for activity in RecentActivityModel.objects.all()[::-1]
        ]
    })