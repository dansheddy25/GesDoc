from django.urls import re_path
from . import views
from django.contrib.auth import views as auth_views
from . import views as user_views
# from pages.views import selection


### Pour le test de l'edition du formulaire
##from . views import IndividuListView, IndividuDetailView
app_name='pages'
urlpatterns = [

### Page d'accueil
    re_path(r'^$', views.home, name = 'home'),
    re_path(r'test/$', views.personalPageView, name = 'test'),


    ### URL to redirect to a profile page
    re_path(r'profile/$', user_views.profile, name = 'profile'),

    ### URL pout tester l'edition d'un formulaire
    #url(r'test1/$', IndividuListView.as_view(), name="test1"),
    #url(r'test1/<char:pk>/$', IndividuDetailView.as_view(), name="test1_detail"),

    ### Login and logout URL
    re_path(r'login/$', auth_views.LoginView.as_view(template_name='general/login.html'),name="login"),
    re_path(r'logout/$', auth_views.LogoutView.as_view(template_name='general/logout.html'),name="logout"),

    ### URL to create an account
    re_path(r'createAccount/$', views.createAccountView,name="createAccount"),

    ### URL to desactivate an account
    re_path(r'desactivateAccount/$', views.desactivateAccountView,name="desactivateAccount"),

## preSelection
    re_path(r'selectCand/$', views.selectCandidatView,name="selectCand"),

## Pour afficher la liste de preselection
    re_path(r'preSelection/$', views.preSelectionView,name="preSelection"),

## Selection finale
    re_path(r'selectFinal/$', views.selectFinalView,name="selectFinal"),

## Pour afficher la liste de selection finale

    re_path(r'selection/$', views.selectionView,name="selection"),

## Pour editer editer les infos de these et Equipe_recherche
    re_path(r'addInfoDoc/$', views.addInfoDocView,name="addInfoDoc"),

## Pour afficher l'information de utilisateur connecté différents du profile
    re_path(r'mesInfo/$', views.mesInfoView,name="mesInfo"),


## La page admin des utilisateur
    re_path(r'personalPage/$', views.personalPageView,name="personalPage"),


## La page admin des utilisateur
    re_path(r'personalPageAdmin/$', views.personalPageAdminView,name="personalPageAdmin"),

### Inscription
#Candidat
    re_path(r'register/$', views.registerFormView, name="register"),
#Professeur
    re_path(r'registerProf/$', views.registerProfFormView, name="registerProf"),

    re_path('admintemp', views.admintemp, name = 'admintemp'),


    #url('candidat_list', views.preSelectionView, name = 'candidat_list'),
    #url('candidatList', views.selectionView, name = 'candidatList'),

### Pour renseigner la date des soutenance
    re_path('soutDate', views.soutDateView, name = 'soutDate'),


### Pour renseigner la mention du doctorant
    re_path('mentionDoc', views.mentionDocView, name = 'mentionDoc'),



### creattion de compte par l'admin
    re_path('createAccountAdmin', views.createAccountAdminView, name = 'createAccountAdmin'),


### Pour ajouter le rapport
    re_path('addReport', views.addReportView, name = 'addReport'),


### Pour ajouter un article
    re_path('writeArticle', views.writeArticleView, name = 'writeArticle'),


### Pour afficher la liste des articles du doctorant
    re_path('mesArticles', views.mesArticlesView, name = 'mesArticles'),


### Pour afficher la liste des articles des doctorants
    re_path('articles', views.articlesView, name = 'articles'),


### Pour afficher la page des articles
    re_path('listArticles/(?P<article_id>\d+)/$', views.listArticlesView, name = 'listArticles'),


### Pour supprimer un article
    re_path('deleteArticle/(?P<article_id>\d+)/$', views.deleteArticleView, name = 'deleteArticle'),


### Pour editer un article
    re_path('editArticle/(?P<article_id>\d+)/$', views.editArticleView, name = 'editArticle'),


### Pour lire un article
    re_path('readArticle/(?P<article_id>\d+)/$', views.readArticleView, name = 'readArticle'),


### Pour valider un article
    re_path('validArticle/(?P<article_id>\d+)/$', views.validArticleView, name = 'validArticle'),


### Pour valider un article
    re_path('sendMsg', views.sendMsgView, name = 'sendMsg'),

    ### Pour afficher le chat
    re_path('chat/(?P<user_id>\d+)/$', views.chatView, name = 'chat'),


    ### Pour lire un article
    re_path('allArticles', views.allArticlesView, name = 'allArticles'),

### Pour afficher la liste des messages recus
    re_path('mesMsg', views.mesMsgView, name = 'mesMsg'),


### Pour afficher la liste des messages recus
    re_path('profile', views.profile, name = 'profile'),



]


### <app>/<model>_<viewtype>.html
