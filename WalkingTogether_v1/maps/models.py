from django.db import models

# Create your models here.
class WarlkingTrails(models.Model):
    category = models.CharField(max_length=50, verbose_name='카테고리')
    region = models.CharField(max_length=50,verbose_name='지역구')
    distance = models.CharField(max_length=50,verbose_name='거리')
    time_required = models.CharField(max_length=50,verbose_name='소요시간')
    level = models.IntegerField(verbose_name='코스레벨')
    subway = models.CharField(max_length=255,verbose_name='연계 지하철')
    Transportation = models.CharField(max_length=5000,verbose_name='교통편')
    course_name = models.CharField(max_length=255,verbose_name='코스명')
    course_detail = models.CharField(max_length=5000,verbose_name='세부코스')
    _explain = models.CharField(max_length=5000,verbose_name='포인트설명')
    point_number = models.IntegerField(verbose_name='포인트순번')
    point_name = models.CharField(max_length=255,verbose_name='포인트명칭')
    longitude = models.DecimalField(decimal_places=14,max_digits=17,verbose_name='경도')
    latitude  = models.DecimalField(decimal_places=14,max_digits=16,verbose_name='위도')
    class Meta:
        db_table = 'Walkingtrails'