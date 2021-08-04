from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractUser)
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class SocialPlatform(models.Model):
    platform = models.CharField(max_length=20, default=0)

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
    age_range = models.CharField(
        blank=True,
        null=True,
        max_length=16,
        choices=AGE_RANGE_CHOICES,
        verbose_name='연령대')
    nickname = models.CharField(
        blank=True,
        null=True,
        max_length=64,
        verbose_name='닉네임')
    GENDER_CHOICES = (
		('male', '남'),
		('female', '여')
	)
    gender = models.CharField(
        blank=True,
        null=True,
        max_length=8,
        choices=GENDER_CHOICES,
        verbose_name='성별')
    profile_public = models.BooleanField(
        verbose_name='프로필 공개 허용 여부',
        default=True)
    number_of_pet = models.IntegerField(
        verbose_name='등록 반려동물 수',
        default=0)
    warning_stack = models.IntegerField(
        verbose_name='신고 누적 횟수',
        default=0)
    social = models.ForeignKey(
        SocialPlatform,
        on_delete=models.CASCADE,
        max_length=20,
        blank=True,
        db_constraint=False,
        default=1)
    social_login_id = models.CharField(
        max_length=50,
        blank=True)
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