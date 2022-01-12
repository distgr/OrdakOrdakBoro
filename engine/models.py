from django.db import models

class RecentActivity(models.Model):
    query = models.CharField(
        max_length=200,
        blank=False,
        null=False,
        verbose_name='عبارت جستجو شده'
    )
    device = models.CharField(
        max_length=200,
        blank=False,
        null=False,
        verbose_name='نام دستگاه'
    )
    secret_ip = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        verbose_name='آی پی خصوصی'
    )
    timestamp = models.DateTimeField(
        auto_now_add=True,
        verbose_name='زمان ثبت'
    )

    class Meta:
        verbose_name = 'فعالیت/جستوجو'
        verbose_name_plural = 'فعالیت/جستوجو های اخیر'
        
    def __str__(self):
        return self.query