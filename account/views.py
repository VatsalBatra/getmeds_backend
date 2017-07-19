from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, JsonResponse, HttpResponse
from django.views.decorators.http import require_GET, require_POST,require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from .models import MyUser, create_otp, get_valid_otp_object
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template import loader
# Create your views here.
def hello(request):
    return HttpResponse('<h1>Hello</h1>');






@require_GET
def show_login(request):
    if request.user.is_authenticated():
        return redirect(reverse('home', kwargs={'id': request.user.id}));
    return render(request, 'account/auth/login.html');

@require_POST
def login(request):
    if request.user.is_authenticated():
        return redirect(reverse('home', kwargs={'id': request.user.id}));
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    user = authenticate(username = username, password = password);
    if not user:
        context = { 'error' : 'Invalid Username/Password'}
        return render(request, 'account/auth/login.html', context)
    else:
        auth_login(request,user)
        return redirect(reverse('home', kwargs={'id': request.user.id}));

def add(request):
    # if request.user.is_authenticated():
    #     context('error':"USER ALREADY EXIST")
    # return render(request,'account/auth/login.html',context)
    username  = request.POST.get('username','')
    password = request.POST.get('password','')
    
    
    if  username and password and MyUser.objects.filter(username = username).exists():
        context = { 'error' : ' Username exist'}
        return render(request, 'account/auth/login.html', context)
    elif username and not password:
        context = { 'error' : ' enter password'}
        return render(request, 'account/auth/login.html', context)
    else:
        user = MyUser.objects.create_user(username,'',password);
        user.save();
        user = authenticate(username = username, password = password);
        auth_login(request,user)
        return redirect(reverse('home', kwargs={'id': request.user.id}));


def reset_password(request):
    username  = request.POST.get('username','')
    if username and MyUser.objects.filter(username = username).exists():
        user = MyUser.objects.get(username =username)
        otp = create_otp(user = user, purpose = 'FP')
        email_body_context = {'user':user,'otp' :otp}
        body = loader.render_to_string('account/auth/email/email.txt',email_body_context)
        message = EmailMultiAlternatives("Reset Password", body, settings.EMAIL_HOST_USER, [user.email])
        #message.attach_alternative(html_body, 'text/html')
        message.send()

        return HttpResponse('check ypur registered email for further process')
    content = {'error':'Username does not exist'}
    return render(request,'account/auth/forgot_password.html',content)
 

@require_http_methods(['GET', 'POST'])
def change_password(request,id = None, otp = None):
    if request.user.is_authenticated():
        return redirect(reverse('home', kwargs={'id': request.user.id}));
    user = get_object_or_404(MyUser, id=id);
    otp_object = get_valid_otp_object(user = user, purpose='FP', otp = otp)
    if not otp_object:
         raise Http404();
    if request.method =='POST':
    
        new_password = request.POST.get('password','')
        console.log(new_password)
        confirm_password = request.POST.get('confirm_password','')
        if new_password and confirm_password and new_password == confirm_password:
            user  = MyUser.objects.get(username = request.user.username)
            user.set_password (new_password)
            user.save()
            otp_object.delete()
            return HttpResponse("ok");
    else:

        content = {
            'uid': user.id,
            'otp':otp_object.otp,
           
            }
        return render(request,'account/auth/change_password.html',content)
   
        
        



@require_GET
def forgot_password(request):
    return render(request,'account/auth/forgot_password.html');

def home(request, id):
    if not request.user.is_authenticated():
        return redirect(reverse('base'))
    return render(request, 'account/auth/loggedin.html')

def logout(request):
    auth_logout(request)
    return redirect(reverse('base'));