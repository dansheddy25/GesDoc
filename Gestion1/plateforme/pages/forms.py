from django import forms
from .models import Individu, Candidat, Diplome, Profile
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django_countries.fields import CountryField




# Personnalisation de du formulaire de creation de compte
class createAccountForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


##

### Class django pour afficher le calendrier au niveau du formulaire
class dateInput(forms.DateInput):
####Le formulaire pour l'inscription du candidat####
    input_type = 'date'
class registerForm(forms.Form):
    cin = forms.CharField(max_length = 8, label = "CIN")
    fname = forms.CharField(max_length = 50, label = "Nom")
    lname = forms.CharField(max_length = 50, label = "Prénom")
    photo = forms.ImageField(required = False, label = "Photo")
    tel = forms.CharField(max_length = 15, label = "Téléphone")
    pays = CountryField().formfield()
    ville_residence = forms.CharField(max_length = 250, label = "Ville de résidence")
    address = forms.CharField(max_length = 60, label = "Adresse")
    genre = forms.ChoiceField(choices = [('Masculin', 'Masculin'), ('Feminin', 'Feminin')], label = "Genre")
    etat_civil = forms.ChoiceField(choices = [('Célibataire', 'Célibataire'), ('Marié/Mariée', 'Marié/Mariée')], label = "Etat civil")
    date_nais = forms.DateField(label = "Date de naissance", widget = dateInput)
    type_dip = forms.ChoiceField(choices = [('Master', 'Master'),("Diplome d'ingenieur", "Diplome d'ingenieur")], label = "Choisissez votre diplome")
    date_dip = forms.DateField(label = "Date du diplome", widget = dateInput)
    fonction = forms.CharField(max_length = 60, label = "Votre fonction")
    entreprise = forms.CharField(max_length= 60, label = "Le nom de l'entreprise")




### Class django pour afficher le calendrier au niveau du formulaire
class dateInput(forms.DateInput):
####Le formulaire pour l'inscription du candidat####
    input_type = 'date'
class registerProfForm(forms.Form):
    cin = forms.CharField(max_length = 8, label = "CIN")
    fname = forms.CharField(max_length = 50, label = "Nom")
    lname = forms.CharField(max_length = 50, label = "Prénom")
    photo = forms.ImageField(required = False, label = "Photo")
    tel = forms.CharField(max_length = 15, label = "Téléphone")
    pays = CountryField().formfield()
    ville_residence = forms.CharField(max_length = 250, label = "Ville de résidence")
    address = forms.CharField(max_length = 60, label = "Adresse")
    genre = forms.ChoiceField(choices = [('Masculin', 'Masculin'), ('Feminin', 'Feminin')], label = "Genre")
    etat_civil = forms.ChoiceField(choices = [('Célibataire', 'Célibataire'), ('Marié/Mariée', 'Marié/Mariée')], label = "Etat civil")
    date_nais = forms.DateField(label = "Date de naissance", widget = dateInput)
    status = forms.ChoiceField(choices = [('Directeur de thèse', 'Directeur de thèse'), ('Co-directeur de thèse', 'Co-directeur de thèse')], label = "Statut")
    equipe = forms.ChoiceField(choices = [('Equipe Systèmes Electriques', 'Equipe Systèmes Electriques'), ('Equipe Architecture Systèmes', 'Equipe Architecture Systèmes'), ('Equipe de Contrôle de Procédés Industriels', 'Equipe de Contrôle de Procédés Industriels'), ('Equipe Réseaux Télécommunication et systèmes Embarqués', 'Equipe Réseaux Télécommunication et systèmes Embarqués'), ('Equipe de Recherche sur la Formation en Sciences de l’Ingénieur', 'Equipe de Recherche sur la Formation en Sciences de l’Ingénieur'), ('Equipe Mécanique des structures et des matériaux', 'Equipe Mécanique des structures et des matériaux')], label = "Equipe de recherche")
    jury = forms.ChoiceField(choices = [('jury1', 'Jury 1'), ('jury2', 'Jury 2'), ('jury3', 'Jury 3'), ('jury4', 'Jury 4'), ('jury5', 'Jury 5'), ('jury6', 'Jury 6'), ('jury7', 'Jury 7')], label = "Jury")


class IndividuForm(forms.ModelForm):
    class Meta:
        model = Individu
        fields = ('cin', 'nom', 'prenoms', 'photo', 'tel', 'addr', 'ville_residence', 'genre', 'etat_civil', 'date_nais')


class DiplomeForm(forms.ModelForm):
    class Meta:
        model = Diplome
        fields = ('type_dip', 'date_dip')


class CandidatForm(forms.ModelForm):
    class Meta:
        model = Candidat
        fields = ('fonction', 'entreprise')


class PostForm(forms.ModelForm):

    class Meta:
        required_css_class = 'required'
        #model = diplome
        #model = candidat,
        model = Individu
        #fields = ('code_dip', 'type_dip',)
    #    fields = ('date', 'fonction', 'entreprise')
        fields = ('cin', 'nom', 'prenoms', 'photo', 'tel', 'addr', 'ville_residence', 'genre', 'etat_civil', 'date_nais')

class candidatForm(forms.ModelForm):
    class Meta:
        model = Candidat
        fields = ('fonction', 'entreprise')


#class diplomeForm(forms.ModelForm):
#    class Meta:
#        model = Diplome
#        fields = ('code_dip', 'type_dip', 'date_dip')


class testForm(forms.Form):
    nom = forms.CharField(max_length = 6, label = 'Nom')
    prenom = forms.CharField(max_length = 6, label = 'Prénom')
    email = forms.EmailField(max_length = 30, label = 'Adresse mail')




class diplomeCandidatForm(forms.Form):
    type_dip = forms.CharField(max_length = 100, label = 'Type du diplome')
    date_dip = forms.DateField(label = 'Date obtention du diplome')
    fonction = forms.CharField(max_length = 60, label = 'Fonction')
    entreprise = forms.CharField(max_length = 60, label = 'Entreprise')



class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']



    """
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
                                                """
