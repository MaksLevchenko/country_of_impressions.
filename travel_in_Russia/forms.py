from django import forms
from django.contrib.auth.models import User

from travel_in_Russia.models import Rating, RatingStar, Reviews, Profile


class ReviewForm(forms.ModelForm):
    """Форма отзывов"""

    class Meta:
        model = Reviews
        fields = ("text",)
        widgets = {
            "text": forms.Textarea(attrs={"class": "form-control border", "id": "contactcomment"}),
        }


class RatingForm(forms.ModelForm):
    """Форма добавления рейтинга"""
    star = forms.ModelChoiceField(
        queryset=RatingStar.objects.all(), widget=forms.RadioSelect(), empty_label=None
    )

    class Meta:
        model = Rating
        fields = ("star",)


class UserForm(forms.ModelForm):
    """Форма пользователя"""

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")


class ProfileForm(forms.ModelForm):
    """Форма профиля пользователя"""

    class Meta:
        model = Profile
        fields = ("birth_date", "avatar")
