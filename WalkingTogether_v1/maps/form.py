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

# 강아지 산책 가능 여부
DOG_POSS=(
    ('가능'),
    ('불가능'),
)
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['point', 'comment']
        labels = {
            'point': _('별점'),
            'dog_possible':_('강아지 산책 가능 여부'),
            'comment': _('내용'),
        }
        widgets = {
            'point': forms.Select(choices=REVIEW_POINT_CHOICES)  # 선택지를 인자로 전달
        }
        help_texts = {
            'point': _('별점을 입력해주세요.'),
            'dog_possible':_("강아지 산책 가능 여부를 선택해주세요"),
            'comment': _('내용을 입력해주세요.'),
        }