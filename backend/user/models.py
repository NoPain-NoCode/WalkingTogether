from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractUser)
from django.utils.translation import ugettext_lazy as _
from elasticsearch_dsl.field import Text

from maps.models import WalkingTrails
from .utils import PetIndex
# Create your models here.
class SocialPlatform(models.Model):
    platform = models.CharField(
        max_length=20,
        default=0,
        unique=True)

    def __str__(self):
        return self.platform

    class Meta:
        db_table = "social_platform"


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    AGE_RANGE_CHOICES = (
		('10~19', '10대'),
		('20~29', '20대'),
        ('30~39', '30대'),
		('40~49', '40대'),
        ('50~59', '50대'),
		('60~69', '60대'),
        ('70~79', '70대'),
		('80~89', '80대')
	)
    age_range = models.CharField(blank=True, null=True, max_length=16, choices=AGE_RANGE_CHOICES, verbose_name='연령대')
    nickname = models.CharField(blank=True, null=True, max_length=64, verbose_name='닉네임')
    GENDER_CHOICES = (
		('male', '남'),
		('female', '여')
	)
    gender = models.CharField(blank=True, null=True, max_length=8, choices=GENDER_CHOICES, verbose_name='성별')
    profile_public = models.BooleanField(verbose_name='프로필 공개 허용 여부', default=True)
    number_of_pet = models.IntegerField(verbose_name='등록 반려동물 수', default=0)
    warning_stack = models.IntegerField(verbose_name='신고 누적 횟수', default=0)
    social = models.ForeignKey(SocialPlatform, on_delete=models.CASCADE, max_length=20, blank=True, db_constraint=False, default=1)
    # 산책로 데이터 foreign key(ManyToMany)
    like_trail = models.ManyToManyField(WalkingTrails, blank=True, verbose_name='좋아요 누른 산책로', related_name='like_users', through='UserLikeWalkingTrail')
    social_login_id = models.CharField(max_length=50, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    class Meta:
        db_table = 'user'
        verbose_name = '회원' 
        verbose_name_plural = '회원'  # 복수형 지정


class UserLikeWalkingTrail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='liked_user')
    walkingtrail = models.ForeignKey(WalkingTrails, on_delete=models.CASCADE, related_name='user_like_walkingtrail')

    def __str__(self):
        return str(self.walkingtrail.point_number)

    class Meta:
        db_table = 'User_Like_WalkingTrails'
        verbose_name = 'User Like Walking Trails' 
        verbose_name_plural = 'User Like Walking Trails'  # 복수형 지정


class Pet(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='주인 정보')
    pet_name = models.CharField(max_length=64, verbose_name='이름')
    GENDER_CHOICES = (
		('male', '수컷'),
		('female', '암컷')
	)
    gender = models.CharField(blank=True, null=True, max_length=8, choices=GENDER_CHOICES, verbose_name='성별')
    pet_image = models.ImageField(verbose_name='프로필 사진', null=True, blank=True)
    introducing_pet = models.TextField(verbose_name='반려동물 소개', null=True)

    def __str__(self):
        return self.pet_name
    
    def indexing(self):
        obj = PetIndex(
            meta={'id':self.id},
            owner=self.owner,
            pet_name=self.pet_name,
            gender=self.gender,
            introducing_pet=self.introducing_pet,
        )
        if obj.owner:
            obj.owner = obj.owner.email
        obj.save()
        return obj.to_dict(include_meta=True)
    
    class Meta:
        db_table = 'user_Pet'
        verbose_name = '반려동물'
        verbose_name_plural = '반려동물'