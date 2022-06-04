from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required
from datetime import datetime
from django.db.models import Q
from .forms import PostForm, registerForm, registerProfForm
from .forms import IndividuForm, DiplomeForm, CandidatForm, UserUpdateForm, ProfileUpdateForm
from datetime import datetime
from .models import Individu, Test, Diplome, Candidat, These, Equipe_recherche, Professeur, Doctorant, Jury, Enregistrement, Article, Msg, Profile
from .forms import candidatForm, diplomeCandidatForm, testForm
from django.contrib.auth.models import User

### Pour le test de l'edition de formulaire
from django.views.generic import ListView, DetailView
from .forms import createAccountForm
#from .forms import userLoginForm
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.views.generic import ListView

# Create your views here.

#def permissionCheck(user):
    #access = False
    #if user.individu.my_status == "professeur":
        #access = True
    #return access





def home(request):
    return render(request, "general/home.html")

#@user_passes_test(lamda u: u.is_superuser)
@login_required()
def admintemp(request):
    return render(request, "pages/admintemp.html")


#### Fonction pour la validation de l'inscription du candidat
@login_required(login_url="/accounts/login/")
def registerFormView(request):
    submitted = False
    if request.method == 'POST':
        form = registerForm(request.POST, request.FILES)
        if form.is_valid():
            cin = request.POST['cin']
            fname = request.POST['fname']
            lname = request.POST['lname']
            photo = request.FILES['photo']
            tel = request.POST['tel']
            address = request.POST['address']
            ville_residence = request.POST['ville_residence']
            genre = request.POST['genre']
            etat_civil = request.POST['etat_civil']
            date_nais = request.POST['date_nais']
            type_dip = request.POST['type_dip']
            date_dip= request.POST['date_dip']
            diplome = Diplome(type_dip = type_dip, date_dip = date_dip)
            fonction = request.POST['fonction']
            entreprise = request.POST['entreprise']
            candidat = Candidat(fonction = fonction, entreprise = entreprise)
            candidat.date = datetime.now().date()
            individu = Individu(cin = cin, nom = fname, prenoms = lname, photo = photo, tel = tel, addr = address, ville_residence = ville_residence, genre = genre, etat_civil = etat_civil, date_nais = date_nais)
            individu.user = request.user
            individu.save()
            user = individu.user
            user.first_name = fname
            user.last_name = lname
            user.save()
            candidat.individu = individu
            diplome.save()
            candidat.save()
            candidat.diplome.add(diplome)
            return redirect('pages:home')

    else:
        form = registerForm()
    return render(request, 'general/register.html', {'form': form})





#Fonction pour la validation de l'inscription du professeur
@login_required(login_url="/accounts/login/")
def registerProfFormView(request):
    submitted = False
    if request.method == 'POST':
        form = registerProfForm(request.POST, request.FILES)
        if form.is_valid():
            cin = request.POST['cin']
            fname = request.POST['fname']
            lname = request.POST['lname']
            photo = request.FILES['photo']
            tel = request.POST['tel']
            address = request.POST['address']
            ville_residence = request.POST['ville_residence']
            genre = request.POST['genre']
            etat_civil = request.POST['etat_civil']
            date_nais = request.POST['date_nais']
            individu = Individu(cin = cin, nom = fname, prenoms = lname, photo = photo, tel = tel, addr = address, ville_residence = ville_residence, genre = genre, etat_civil = etat_civil, date_nais = date_nais, my_status = "professeur")
            individu.user = request.user
            user = individu.user
            user.first_name = fname
            user.last_name = lname
            user.save()
            equipe = request.POST['equipe']
            equipes = Equipe_recherche.objects.get(libelle_equipe = equipe)
            equipes.save()
            jury = request.POST['jury']
            jurys = Jury.objects.get(libelle_jury = jury)
            jurys.save()
            status = request.POST['status']
            if status == "Directeur de thèse":
                professeur = Professeur(status = True)
            else:
                professeur = Professeur(status = False)
            professeur.individu = individu
            professeur.equipe = equipes
            professeur.jury = jurys
            individu.save()
            professeur.save()
            return redirect('pages:home')

    else:
        form = registerProfForm()
    return render(request, 'general/registerProf.html', {'form': form})





# Creation de compte
def createAccountView(request):
    if request.method == 'POST':
         form = createAccountForm(request.POST)
         if form.is_valid():
             form.save()
             username = form.cleaned_data.get('username')
             messages.success(request, f'Le compte est cree! Vous pouvez vous conecter')
             return redirect('pages:login')
    else:
        form = createAccountForm()
    return render(request, 'general/createAccount.html', { 'form': form })





# Desactivation de compte
@login_required()
@user_passes_test(lambda u: u.is_superuser)
def desactivateAccountView(request):
    if request.method == 'POST':
        list_ind= Individu.objects.all()
        for individu in list_ind:
            key = 'inpt_'+individu.cin
            var_inpt =  request.POST[key]
            if  var_inpt =='desactiver':
                individu.desactiver = True
                individu.user.is_active = False
                individu.user.save()
                #users = Individu.objects.get(cin = var_inpt)
                #user = users.user
                #user.is_active = False
                #user.save()
                messages.success(request, 'Profile successfully disabled.')
            else :
                individu.desactiver = False
                individu.user.is_active = True
                individu.user.save()
                #users = Individu.objects.get(cin = var_inpt)
                #user = users.user
                #user.is_active = True
                #user.save()
                messages.success(request, 'Profile successfully abled.')
            individu.save()
        return redirect('pages:desactivateAccount')
    else:
        list_individu = Individu.objects.all()
        return render(request, 'pages/desactivateAccount.html', { 'list_individu': list_individu })






### fonction pour afficher le profile de l'utilisateur
@login_required
def profile(request):
    return render(request, "general/profile.html")





#@login_required(login_url="/pages/login/")
@login_required()
def personalPageView(request):
    if request.user.individu.my_status == 'doctorant' or request.user.individu.my_status == 'professeur':
        individus = Individu.objects.all()
        return render(request, "pages/personalPage.html", {'individus': individus})
    else:
        return redirect('pages:login')




#@login_required(login_url="/pages/login/")
@login_required()
def personalPageAdminView(request):
    if request.user.is_superuser:
        individus = Individu.objects.all()
        return render(request, "pages/personalPage.html", {'individus': individus})
    else:
        return redirect('pages:login')





#pour la preSelection des candidats
@login_required()
@user_passes_test(lambda u: u.is_superuser)
def selectCandidatView(request):
    if request.method == 'POST':
        list_ind= Candidat.objects.all()
        for candidat in list_ind:
            key = 'inpt_'+candidat.individu.cin
            var_inpt =  request.POST[key]
            if  var_inpt =='accepted':
                candidat.preselection = True
            else :
                candidat.preselection = False
            candidat.save()
        return redirect('pages:selectCand')

    else:
        list_individus= Candidat.objects.all(); #remember to check how to paginate
        return render(request, 'pages/selectCand.html', { 'list_individus': list_individus })





## affichage de la liste de preselection
@login_required()
def preSelectionView(request):
    candidats = Candidat.objects.filter(preselection = True)
    return render(request, "pages/candidat_list.html", {'candidats': candidats})





# pour la selection final des candidates
@login_required()
@user_passes_test(lambda u: u.is_superuser)
def selectFinalView(request):
    if request.method == 'POST':
        list_ind= Candidat.objects.filter(preselection = True)
        for candidat in list_ind:
            key = 'inpt_'+candidat.individu.cin
            var_inpt =  request.POST[key]
            if  var_inpt =='accepted':
                candidat.selection = True
                candidat.save()
                var_indiv = candidat.individu
                var_indiv.my_status = 'doctorant'
                var_indiv.save()
            else :
                candidat.selection = False
                candidat.save()


        return redirect('pages:addInfoDoc')

    else:
        list_individus= Candidat.objects.filter(preselection = True); #remember to check how to paginate
        return render(request, 'pages/selectFinal.html', { 'list_individus': list_individus })




## Creer le doctorant et ajouter sa thèse et son équipe de recherche
@login_required()
@user_passes_test(lambda u: u.is_superuser)
def addInfoDocView(request):
    if request.method == 'POST':
        list_ind= Candidat.objects.filter(selection = True)
        for candidat in list_ind:
            key2 = 'inpt_th_'+candidat.individu.cin
            var_inpt2 =  request.POST[key2]
            these = These.objects.get(id=var_inpt2 )
            key3 = 'inpt_eq_'+candidat.individu.cin
            var_inpt3 =  request.POST[key3]
            equipe = Equipe_recherche.objects.get(id=var_inpt3 )
            if(not hasattr(candidat, 'doctorant')):
                doctorant= Doctorant(these =these, candidat=candidat, equipe= equipe )
                doctorant.save()
            else:
                doctorant= Doctorant.objects.get(id= candidat.doctorant.id)
                doctorant.these= these
                doctorant.equipe = equipe
                doctorant.save()

        return redirect('pages:addInfoDoc')

    else:
        list_individus= Candidat.objects.filter(selection = True); #remember to check how to paginate
        list_theses  = These.objects.all()
        list_equipes  = Equipe_recherche.objects.all()
        return render(request, 'pages/addInfoDoc.html', { 'list_individus': list_individus , 'list_theses': list_theses, 'list_equipes': list_equipes })





## affichage de la selection finale
@login_required()
def selectionView(request):
    individus = Candidat.objects.filter(selection = True)
    return render(request, "pages/selection.html", {'individus': individus})

# class selection(ListView):
#     model = Candidat
#     template_name = 'pages/selection.html'
#     context_object_name = 'list_candidats'
#     paginate_by = 6





### Pour afficher les information relatives à l'utlisateur connecté différent du profile
@login_required()
def mesInfoView(request):
    if request.user.individu.my_status == "professeur":
            list_doctorants = Doctorant.objects.filter(equipe = request.user.individu.professeur.equipe)
            return render(request, 'pages/mesInfo.html', { 'list_doctorants': list_doctorants })
    else:
        return render(request, 'pages/mesInfo.html')




### Pour renseigner la date de la soutenance
@login_required()
@user_passes_test(lambda u: u.is_superuser)
def soutDateView(request):
    if request.method == 'POST':
        list_ind= Doctorant.objects.all()
        for doctorant in list_ind:
            key2 = 'inpt_th_'+doctorant.candidat.individu.cin
            var_inpt2 =  request.POST[key2]
            jury = Jury.objects.get(id=var_inpt2 )
            date = request.POST['date']
            #key3 = 'inpt_eq_'+candidat.individu.cin
            #var_inpt3 =  request.POST[key3]
            #equipe = Equipe_recherche.objects.get(id=var_inpt3 )
            #if(not hasattr(candidat, 'doctorant')):
            #doctorant= Doctorant(these =these, candidat=candidat, equipe= equipe )
            #doctorant.save()
            #else:
            doctorant= Doctorant.objects.get(id = doctorant.id)
            jurys = Jury.objects.get(libelle_jury = jury)
            jurys.date_soutenance = date
            jurys.save()
            doctorant.jury= jury
            doctorant.save()

        return redirect('pages:soutDate')

    else:
        list_individus= Doctorant.objects.all()
        list_these = These.objects.all()
        list_jury = Jury.objects.all()
        list_equipe = Equipe_recherche.objects.all()
        return render(request, 'pages/soutDate.html', { 'list_individus': list_individus, 'list_jury': list_jury, 'list_equipe': list_equipe, 'list_these': list_these})




## Pour renseigner la mention du doctorant
@login_required()
@user_passes_test(lambda u: u.is_superuser)
def mentionDocView(request):
    if request.method == 'POST':
        list_ind= Doctorant.objects.all()
        for doctorant in list_ind:
            mention = request.POST['mention']
            doctorant = Doctorant.objects.get(id = doctorant.id)
            doctorant.mention = mention
            doctorant.save()
        return redirect('pages:mentionDoc')

    else:
        list_individus= Doctorant.objects.all(); #remember to check how to paginate
        return render(request, 'pages/mentionDoc.html', { 'list_individus': list_individus })




# Creation de compte par l'admin
@login_required()
@user_passes_test(lambda u: u.is_superuser)
def createAccountAdminView(request):
    if request.method == 'POST':
         form = createAccountForm(request.POST)
         if form.is_valid():
             form.save()
             username = form.cleaned_data.get('username')
             messages.success(request, f'Le compte est cree! Vous pouvez vous conecter')
             return redirect('pages:admintemp')
    else:
        form = createAccountForm()
    return render(request, 'pages/createAccountAdmin.html', { 'form': form })




# Pour ajouter le rapport d'avancement
@login_required()
def addReportView(request):
    if request.method == 'POST':
        titre = request.POST['titre']
        rapport = request.FILES['rapport']
        date = request.POST['date']
        auteur = request.user.individu.candidat.doctorant
        record = Enregistrement(titre = titre, auteur = auteur, rapport = rapport, date_enregristrement = date)
        record.save()
        return redirect('pages:personalPage')
    else:
        return render(request, 'pages/addReport.html')




# Pour ajouter un article
@login_required()
def writeArticleView(request):
    if request.method == 'POST':
        titre = request.POST['titre']
        body = request.POST['body']
        auteur = request.user.individu.candidat.doctorant
        record = Article(titre = titre, auteur = auteur, body = body)
        record.save()
        return redirect('pages:mesArticles')
    else:
        return render(request, 'pages/writeArticle.html')




# Pour afficher la liste des articles du doctorant
@login_required()
def mesArticlesView(request):
    articles = Article.objects.filter(auteur = request.user.individu.candidat.doctorant, accept = True)
    return render(request, 'pages/mesArticles.html', {'articles': articles})




# Pour afficher la liste des articles des doctorants
@login_required()
def articlesView(request):
    if request.user.individu.my_status == "professeur":
        if request.method == 'POST':
            titre = request.POST['titre']
            body = request.POST['body']
            auteur = request.user.individu.candidat.doctorant
            record = Article(titre = titre, auteur = auteur, body = body)
            record.save()
            return redirect('pages:personalPage')
        else:
            articles = Article.objects.all()
            return render(request, 'pages/articles.html', {'articles': articles})
    else:
        return redirect('pages:login')




# Pour afficher la pages des articles
@login_required()
def listArticlesView(request, article_id):
    articles = Article.objects.get(id = article_id)
    return render(request, 'general/listArticles.html', {'articles': articles})




# Pour supprimer un article
@login_required()
def deleteArticleView(request, article_id):
    articles = Article.objects.get(id = article_id)
    articles.delete()
    return redirect('pages:mesArticles')




# Pour editer un article
@login_required()
def editArticleView(request, article_id):
    if request.method == 'POST':
        titre = request.POST['titre']
        body = request.POST['body']
        #auteur = request.user.individu.candidat.doctorant
        record = Article.objects.get(id = article_id)
        record.titre = titre
        record.body = body
        #record.auteur = auteur
        record.save()
        if request.user.individu.my_status == "doctorant":
            return redirect('pages:mesArticles')
        elif request.user.individu.my_status == "professeur":
            return redirect('pages:articles')
    else:
        articles = Article.objects.get(id = article_id)
        return render(request, 'pages/editArticle.html', {'articles': articles})




# Pour lire un article
@login_required()
def readArticleView(request, article_id):
    articles = Article.objects.get(id = article_id)
    return render(request, 'pages/readArticle.html', {'articles': articles})




# Pour lire un article
@login_required()
def allArticlesView(request):
    articles = Article.objects.all()
    return render(request, 'general/allArticles.html', {'articles': articles})


# Pour valider un article
@login_required()
def validArticleView(request, article_id):
    if request.user.individu.my_status == "professeur":
        if request.method == 'POST':
            articles = Article.objects.get(id = article_id)
            key = 'inpt_art_'+articles.auteur.candidat.individu.cin
            var_key = request.POST[key]
            if var_key == 'rejected':
                articles.accept = False
            else:
                articles.accept = True
            articles.save()
            return redirect('pages:articles')
        else:
            articles = Article.objects.get(id = article_id)
            return render(request, 'pages/readArticle.html', {'articles': articles})
    else:
        return redirect('pages:login')





@login_required()
def mesMsgView(request):
    if request.method == 'POST':
        messages = Msg.objects.filter(to_who = request.user.username)
        for message in messages:
            key = 'inpt_th_'+message.sender
            var = request.POST['key']
            keys = Key(value = var)
            keys.save()
            return redirect('pages:chat')
    else:
        messages = Msg.objects.filter(to_who = request.user.username)
        return render(request, 'pages/mesMsg.html',{'messages':messages})







### Application de chat
@login_required()
def chatView(request, user_id):
    var_correspondant = User.objects.get(id= user_id)
    messages = Msg.objects.filter(Q(to_who = request.user.username , sender = var_correspondant.individu) | Q(sender = request.user.individu , to_who = var_correspondant.username)).order_by('date')

    print(user_id)
    return render(request, 'pages/chat.html',{'messages':messages, 'var_correspondant':var_correspondant})





@login_required()
def sendMsgView(request):
    submitted = False
    if request.method == 'POST':
        from_who = request.user.individu
        to_who = request.POST['to_who']
        my_receiver = User.objects.get(username = to_who)
    #    sujet_msg = request.POST['sujet_msg']
        msg = request.POST['msg']
        my_msg = Msg (sender = from_who, to_who = to_who,  msg = msg)
        my_msg.save()
        return redirect('pages:chat',user_id = my_receiver.id)

    else:
        if request.user.individu.my_status == "professeur":
            prof = Doctorant.objects.all()
        elif request.user.individu.my_status == "doctorant":
            prof = Professeur.objects.all()
        return render(request, 'pages/sendMsg.html', {'prof': prof})




@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('pages:profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form

    }
    return render(request, 'pages/profile.html',context)
