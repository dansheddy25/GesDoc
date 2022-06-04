from django.shortcuts import render,redirect

# Create your views here.
def wel(request):
    return render(request,"paneladmin/wel.html")
    #return render(request,'paneladmin/wel.html')
    #return redirect('pages:forms' )
