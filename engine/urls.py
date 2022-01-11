from django.urls.conf import path
from .views import Main, RecentActivity

app_name = 'engine'

urlpatterns = [
    path('', Main, name='main'),
    path('recentactivity', RecentActivity, name='recentactivity')
]
