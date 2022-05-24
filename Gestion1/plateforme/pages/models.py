from django.db import models
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.models import User
from PIL import Image
from django_countries.fields import CountryField



# Create your models here.

class Individu(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    cin = models.CharField(max_length = 8, unique = True, default = "")
    nom = models.CharField(max_length = 50, default="")
    prenoms = models.CharField(max_length = 50, default="")
    photo = models.ImageField(default = "default.jpg", upload_to = 'individu_pics')
    tel = models.CharField(max_length = 15, default="")
    addr = models.CharField(max_length = 60, default="")
    ville_residence = models.CharField(max_length = 250, default="")
    pays = models.CharField(max_length = 30, default = "Maroc")
    genre = models.CharField(max_length = 15, default = "Masculin")
    etat_civil = models.CharField(max_length = 15, default = "Célibataire")
    date_nais = models.DateField()
    status_choices = (
        ('professeur', 'professeur'),
        ('candidat', 'candidat'),
        ('doctorant', 'doctorant'),
    )
    my_status = models.CharField(max_length = 15, choices = status_choices, default = "candidat")
    desactiver = models.BooleanField(default = False)

    def __str__(self):
        return "%s %s" %(self.nom, self.prenoms)



class Diplome(models.Model):
    type_dip = models.CharField(max_length=100, default = "")
    date_dip = models.DateTimeField()
    def __str__(self):
        return str(self.type_dip)



class Candidat(models.Model):
    individu = models.OneToOneField(Individu, on_delete = models.CASCADE)
    fonction = models.CharField(max_length = 60, default="")
    entreprise = models.CharField(max_length = 60)
    diplome = models.ManyToManyField(Diplome)
    preselection = models.BooleanField(default = False)
    selection = models.BooleanField(default = False)
    def __str__(self):
        return "%s %s" %(self.individu.nom, self.individu.prenoms)




class Compte(models.Model):
    ref_compte = models.AutoField(primary_key = True)
    date_cree = models.DateTimeField(default=datetime.now)



class Jury(models.Model):
    libelle_jury =  models.CharField(max_length=100, default="")
    date_soutenance = models.DateTimeField(null = True)
    def __str__(self):
        return str(self.libelle_jury)


class Equipe_recherche(models.Model):
    libelle_equipe = models.CharField(max_length=100, default="")
    def __str__(self):
        return str(self.libelle_equipe)


class Professeur(models.Model):
    status = models.BooleanField(default = False)
    individu = models.OneToOneField(Individu, on_delete = models.CASCADE)
    equipe = models.ForeignKey(Equipe_recherche, on_delete = models.CASCADE)
    jury = models.ForeignKey(Jury, on_delete = models.CASCADE)
    def __str__(self):
        return str(self.individu.nom)




class These(models.Model):
    titre_these = models.CharField(max_length=100, default="")
    director_these = models.ForeignKey(Professeur, on_delete = models.CASCADE)
    def __str__(self):
        return str(self.titre_these)



class Doctorant(models.Model):
    these= models.OneToOneField(These, on_delete=models.CASCADE)
    candidat = models.OneToOneField(Candidat, on_delete = models.CASCADE)
    equipe = models.ForeignKey(Equipe_recherche, on_delete = models.CASCADE)
    jury = models.ForeignKey(Jury, on_delete = models.CASCADE, null = True)
    mention_choice = (
        ('Honorable','Honorable'),
        ('Très Honorable','Très Honorable'),
    )
    mention = models.CharField(max_length = 20, choices = mention_choice, default = "")
    def __str__(self):
        return "%s %s" %(self.candidat.individu.nom, self.candidat.individu.prenoms)


class Enregistrement(models.Model):
    titre = models.CharField(max_length = 100, default = "")
    rapport = models.FileField(max_length=100, default="")
    date_enregristrement = models.DateTimeField(default=datetime.now)
    auteur = models.ForeignKey(Doctorant, on_delete = models.CASCADE)
    def __str__(self):
        return "%s %s" %(self.auteur.candidat.individu.nom, self.titre)


class Article(models.Model):
    titre = models.CharField(max_length = 100, default = "")
    body = models.TextField()
    date = models.DateField(default = timezone.now)
    auteur = models.ForeignKey(Doctorant, on_delete = models.CASCADE)
    accept = models.BooleanField(default = True)
    def __str__(self):
        return str(self.titre)



class Test(models.Model):
    fname = models.CharField(max_length = 6, default = "")
    lname = models.CharField(max_length = 6, default = "")
    mail = models.EmailField(max_length = 30)
    def __str__(self):
        return str(self.fname)


### Une table pour les users
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(default = 'default.jpg', upload_to = 'profile_pics')


    def __str__(self):
        return f'{self.user.username} profile'

    def save (self):
        super().save()
# to resize the image
        img = Image.open(self.image.path)
        if img.height > 400 or img.width > 400:
            output_size = (400, 400)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Msg(models.Model):
    to_who = models.CharField(max_length=100, null = True, blank = True)
    msg = models.TextField(default="", null = True, blank = True)
    sender = models.ForeignKey(Individu, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now)
    def __str__(self):
        return self.sender.nom
