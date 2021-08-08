from django import forms
from django.db.models import fields
from .models import WalkingTrails, Review

class PostForm(forms.ModelForm):
    class Meta:
        model = WalkingTrails
        fields = ('latitude', 'longitude')

# 평점의 선택지
REVIEW_POINT_CHOICES = (
    ('1', 1),
    ('2', 2),
    ('3', 3),
    ('4', 4),
    ('5', 5),
)
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['point', 'comment']
        labels = {
            'point': _('평점'),
            'comment': _('코멘트'),
        }
        widgets = {
            'point': forms.Select(choices=REVIEW_POINT_CHOICES)  # 선택지를 인자로 전달
        }
        help_texts = {
            'point': _('평점을 입력해주세요.'),
            'comment': _('코멘트를 입력해주세요.'),
        }