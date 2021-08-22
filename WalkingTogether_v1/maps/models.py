from django.db import models
# from django.contrib.auth.models import User
# from user.models import User

# Create your models here.
class WalkingTrails(models.Model):
    category = models.CharField(max_length=50, verbose_name='카테고리')
    region = models.CharField(max_length=50,verbose_name='지역구')
    distance = models.CharField(max_length=50,verbose_name='거리')
    time_required = models.CharField(max_length=50,verbose_name='소요시간')
    _level = models.IntegerField(verbose_name='코스레벨')
    subway = models.CharField(max_length=255,verbose_name='연계 지하철')
    Transportation = models.CharField(max_length=5000,verbose_name='교통편')
    course_name = models.CharField(max_length=255,verbose_name='코스명')
    course_detail = models.CharField(max_length=5000,verbose_name='세부코스')
    _explain = models.CharField(max_length=5000,verbose_name='포인트설명')
    point_number = models.IntegerField(primary_key=True, verbose_name='포인트순번')
    point_name = models.CharField(max_length=255,verbose_name='포인트명칭')
    longitude = models.DecimalField(decimal_places=14,max_digits=17,verbose_name='경도')
    latitude  = models.DecimalField(decimal_places=14,max_digits=16,verbose_name='위도')
    
    # count_review = models.IntegerField(default=0, verbose_name="리뷰 개수")

    def __str__(self):
        return str(self.point_number)

    class Meta:
        managed = False
        db_table = 'walkingtrails'
        verbose_name = 'Walking Trails' 
        verbose_name_plural = 'Walking Trails'  # 복수형 지정

class Review(models.Model):
    # id = models.CharField(max_length=255,primary_key=True,verbose_name="리뷰 id")
    walkingtrails = models.ForeignKey(WalkingTrails,blank=True, null=True, related_name="walkingtrails", db_column="point_number", on_delete=models.CASCADE)
    user = models.ForeignKey('user.User',blank=True, null=True, related_name="user", on_delete=models.CASCADE)
    content = models.TextField(null=True, verbose_name="내용")
    
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="작성시간")
    updated_date = models.DateTimeField(auto_now=True, verbose_name="수정 시간")
    # image = models.ImageField(blank=True,null=True, verbose_name="이미지")
    
    # 별점 선택지
    REVIEW_POINT_CHOICES = (
    ('1', 1),
    ('2', 2),
    ('3', 3),
    ('4', 4),
    ('5', 5),
    )

    # 강아지 산책 가능 여부
    DOG_POSS=(
    ('ok','가능해요'),
    ('no','불가능해요'),
    ('dontKnow','잘 모르겠어요')
    )

    point = models.CharField(max_length=255,blank=True,choices=REVIEW_POINT_CHOICES,verbose_name="별점")
    dog_possible = models.CharField(max_length=255,blank=True, null=True, choices=DOG_POSS, verbose_name="강아지 산책 가능 여부")


    objects = models.Manager()

    def __str__(self):
        return str(self.id)
    
    class Meta:
        db_table = 'review'
        verbose_name = 'review'
        verbose_name_plural = 'reviews'