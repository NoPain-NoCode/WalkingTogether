from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager

# Create your models here.
class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    age_range = models.CharField(blank=True, null=True, max_length=16, verbose_name='연령대')
    nickname = models.CharField(blank=True, null=True, max_length=64, verbose_name='닉네임')
    GENDER_CHOICES = (
		('male', '남'),
		('female', '여')
	)
    gender = models.CharField(blank=True, null=True, max_length=8, choices=GENDER_CHOICES, verbose_name='성별')
    profile_public = models.BooleanField(verbose_name='프로필 공개 허용 여부', default=True)
    number_of_pet = models.IntegerField(verbose_name='등록 반려동물 수', default=0)
    warning_stack = models.IntegerField(verbose_name='신고 누적 횟수', default=0)

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'user'
        verbose_name = '회원' 
        verbose_name_plural = '회원'  # 복수형 지정
