from django import forms
from django.contrib.auth import authenticate, get_user_model


User = get_user_model()

class userLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username = username, password = password)

            if not user:
                raise forms.ValidationError('Ce utilisateur existe pas')

            if not user.check_password(password):
                raise forms.ValidationError('Mot de passe incorrect')

            if not user.is_active:
                raise forms.ValidationError('Ce utilisateur est pas actif')
            return super(userLoginForm, self).clean(*args, **kwargs)


class userRegisterForm(forms.Form):
    email = forms.EmailField(label = 'Adresse Mail')
    email2 = forms.EmailField(label = 'Confirmer Mail')
    password = forms.CharField(widget = forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'email2',
            'password'
        ]


    def cleaned_email(self):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')

        if email != email2:
            raise forms.ValidationError("Les adresses mails doivent correspondre")

        email_qs = User.objets.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("Cette adresse mail existe")
        return email
