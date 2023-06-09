from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models

USER_TYPE = (
    ('Админ', 'Aдмин'),
    ('VIP Клиент', "VIP Клиент"),
    ('Клиент', 'Клиент'),
)

GENDER = (
    ('M', "M"),
    ('Ж', 'Ж'),
)

ORIENTATION = (
    ('STRAIGHT', 'STRAIGHT'),
    ('GAY', 'GAY'),
    ('LESBIAN', 'LESBIAN'),
)

MARRY_TYPE = (
    ('MARRIED', 'MARRIED'),
    ('SINGLE', 'SINGLE'),
)

YES = 1
NO = 2
I_DONT_KNOW = 3

DUMP_TYPE = (
    (YES, 'YES!'),
    (NO, 'NO!'),
    (I_DONT_KNOW, 'I DONT KNOW!'),
)


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.IntegerField(required=True)
    age = forms.IntegerField(required=True)
    user_type = forms.ChoiceField(choices=USER_TYPE, required=True)
    gender = forms.ChoiceField(choices=GENDER, required=True)
    birthday = forms.CharField(required=True)
    orientation = forms.ChoiceField(choices=ORIENTATION, required=True)
    marry = forms.ChoiceField(choices=MARRY_TYPE, required=True)
    city = forms.CharField(required=True)
    favorite_film = forms.CharField(required=True)
    dump = forms.ChoiceField(choices=DUMP_TYPE, required=True)

    class Meta:
        model = models.CustomUser
        fields = (
            'username',
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'age',
            'user_type',
            'gender',
            "birthday",
            "orientation",
            "dump",
            "favorite_film",
            "marry",
            "city",
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
