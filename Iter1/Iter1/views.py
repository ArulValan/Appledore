from django.http import HttpResponse, JsonResponse

def test(request):
    return JsonResponse({"success":200})

def status(request,user):
    return HttpResponse(user+" is "+request.session.get('user','Not Logged in'))

def login(request,user):
    request.session['user'] = 'Logged in'
    return HttpResponse(user+" Sucessfully Logged in")
def logout(request,user):
    del request.session['user']
    return HttpResponse(user+" Sucessfully Logged out")

from jinja2 import Template
def profile(request,user):
    if(request.session.get('user','Not Logged in')=='Not Logged in'):
        return HttpResponse("User not logged in")
    else:
        profile_temp = open('templates/profile.html', 'r').read()
        print(profile_temp)
        return HttpResponse(profile_temp)

def Collections(request,user,Collection):
    if(request.session.get('user','Not Logged in')=='Not Logged in'):
        return HttpResponse("User not logged in")
    else:
        profile_temp = open('templates/'+Collection+'.html', 'r').read()
        print(profile_temp)
        return HttpResponse(profile_temp)

def Topics(request,user,Topic):
    if(request.session.get('user','Not Logged in')=='Not Logged in'):
        return HttpResponse("User not logged in")
    else:
        profile_temp = open('templates/'+Topic+'.html', 'r').read()
        print(profile_temp)
        return HttpResponse(profile_temp)
