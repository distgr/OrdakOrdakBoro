from django.http import request
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import RecentActivity as RecentActivityModel
from scripts.ddg import DuckDuckGo
import datetime

def Main(request):
    if(request.GET.get('query')):

        results = DuckDuckGo().search(
            request.GET.get('query')
        )

        xff = request.META.get('HTTP_X_FORWARDED_FOR')
        ip = xff.split(',')[0] if xff else request.META.get('REMOTE_ADDR')
    
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
    return JsonResponse({
        'activities': [
            {
                'query': activity.query,
                'device': activity.device,
                'secret_ip': activity.secret_ip,
                'timestamp': activity.timestamp.strftime('%Y-%m-%d %H:%M:%S')
            } for activity in RecentActivityModel.objects.filter(
                timestamp__gte=(datetime.datetime.now() - datetime.timedelta(days=1))
            )[::-1]
        ]
    })