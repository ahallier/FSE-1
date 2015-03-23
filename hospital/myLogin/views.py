from django.http import HttpResponse
from django.template import loader, RequestContext
from django.shortcuts import render
from django.contrib.auth import views
import django

#def authenticate_user(request):
def login_page(request,):
  # return loginTime(request)
    template_response= django.contrib.auth.views.login(request)
    return template_response
   # """Logs a user into the application."""
 
def loginTime(request):
    template = loader.get_template('myLogin/index.html')
    test = "hello"
    context = {"tempVar":test}
#   context = RequestContext(request, {"tempVar" :test,})
    return render(request,'myLogin/index.html', context)

def login_after(request):
    if not request.user.is_authenticated():
        return HttpResponse("Bad Password")
    else:
        return HttpResponse("Good Password")
#   return HttpResponse("at login After")
#   return HttpResponse(template.render(context))
#   return HttpResponse("loginTime")

def login_success(request):
    return HttpResponse("Success")

def login_fail(request):
    return HttpResponse("fail")



# Create your views here.
