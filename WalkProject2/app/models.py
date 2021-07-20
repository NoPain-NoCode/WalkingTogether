
from django.db import models

class Mytrails(models.Model):
    User_email = models.ForeignKey('User',on_delete=models.CASCADE)
    trailname = models.CharField(max_length=64, verbose_name='산책로명')
    distance = models.FloatField(max_length=64, verbose_name='거리')
    time_spend = models.FloatField(max_length=64, verbose_name='소요시간')
    walking_date = models.DateTimeField(default=datetime.now, blank=true, verbose_name='산책일시')
    pet_accessibility = models.BooleanField(default=False)
    exercise_accessibility = models.BooleanField(default=False)
    Transportation = models.CharField(max_length=256,verbose_name='교통수단')
    mypoint_number = models.IntegerField(verbose_name='포인트순번')
    mypoint_name = models.CharField(max_length=256, verbose_name='포인트명칭')
    longitude = models.DecimalField(verbose_name='경도')
    latitude  = models.DecimalField(verbose_name='위도')
    starred = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], default=3, verbose_name='별점')

    def _str_(self):
        return self.trailname

    class Meta:
        db_table = 'Mytrails'
        ordering = ['create_date']

CHOICES = (
    ('남', '여')
)
class Pet(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='주인 정보')
    pet_name = models.CharField(max_length=64, verbose_name='이름')
    gender = models.ChoiceField(widget=forms.RadioSelect(choices=CHOICES), default='남', verbose_name='성별')
    pet_image = models.ImageField(verbose_name='프로필 사진', null=True)
    introducing_pet = models.TextField(verbose_name='반려동물 소개', null=True)
     
    class Meta:
        db_table = 'user_Pet'
        verbose_name = '반려동물 정보'
        verbose_name_plural = '반려동물 정보'