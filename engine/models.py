from django.db import models

class RecentActivity(models.Model):
    query = models.CharField(max_length=200)
    device = models.CharField(max_length=200)
    secret_ip = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.query