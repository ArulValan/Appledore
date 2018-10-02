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
