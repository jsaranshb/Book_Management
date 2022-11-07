from django.shortcuts import render
from django.views import View
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from .models import CustomUser, uploaded_files
from social_book.decorators import IsVisible, IsUploaded
from django.template.loader import get_template
from django.conf import settings
from django.core.mail import EmailMessage


from django.core.mail import send_mail

# Create your views here.

class HomeView(View):
    
    def get(self, request):
        return render(request, 'app1/index.html')


class RegisterView(View):

    def get(self, request):
        return render(request, "app1/register.html")

    def post(self, request):
        username=request.POST.get("username")
        fullname=request.POST.get("fullname")
        email=request.POST.get("email")
        birthday_year=request.POST.get("birthday_year")
        address=request.POST.get("address")
        password=request.POST.get("password")
        confirm_password=request.POST.get("confirm_password")
        if not username or not fullname or not email or not password or not confirm_password :
            return render(request, 'app1/register.html',{"msg":"All field are required to register."})
        elif password != confirm_password :
            return render(request, 'app1/register.html',{"msg":"Password and confirm-password should be same to register."})
        elif CustomUser.objects.filter(username=username).exists() :
            return render(request, 'app1/register.html',{"msg":"Username already exists, Please try another username."})
        elif CustomUser.objects.filter(email=email).exists() :
            return render(request, 'app1/register.html',{"msg":"Account with this email already exists, Please try another email."})
        else:
            user = CustomUser.objects.create_user(username=username, fullname=fullname, email=email, birthday_year=birthday_year, address=address, password=password)
            user.save()
            return render(request, 'app1/login.html',{"msg":"Registered Successfully, Please Login ..."})
        
        
class LoginView(View):

    def get(self, request):
        msg = request.GET.get("msg")
        if request.user.is_authenticated:
            return render(request, "app1/index.html")
        return render(request, 'app1/login.html', {"msg":msg})

    def post(self, request):
        input_username=request.POST.get("username")
        input_password=request.POST.get("password")
        if not input_username or not input_password:
            return render(request, 'app1/login.html',{"msg":"Both username and password required to login."})    
        else:
            user = authenticate(username=input_username, password=input_password)
            if user:
                login(request, user)
                emailmsg=EmailMessage(
                'Login notofication',
                'Hello!!! you have successfully logged into Social-Book application.',
                settings.EMAIL_HOST_PASSWORD,
                [request.user.email]
                )
                emailmsg.fail_silently=False
                emailmsg.send()
                return render(request, 'app1/index.html', {"msg":"You have successfully logged-In."})
            else:
                return render(request, 'app1/login.html',{"msg":"Invalid username and password combination."})
    
def logout_user(request):
    logout(request)
    #return HttpResponseRedirect(reverse("blogapp:login_user"))   
    return render(request, 'app1/login.html', {})


class AuthorSellersView(View):
    
    def get(self, request):
        details = CustomUser.objects.filter(public_visibility="True")
        context = {
            "details" : details
        }
        return render(request, 'app1/user_details.html', context)
    
    
class BookFilesView(View):
    
    def get(self, request):
        # book_details = uploaded_files.objects.filter(owner=request.user)
        # print(book_details)
        msg = request.GET.get("msg")
        context={
            # "book_details": book_details,
            "msg": msg,
        }
        return render(request, 'app1/dashboard.html', context)
        # if request.user.is_authenticated:
        #     return render(request, 'app1/dashboard.html', context)
        #     return render(request, "blogapp/homepage.html")
        # return HttpResponseRedirect(reverse("app1:login"))
        # return render(request, 'app1/login.html', {"msg": "Login First ..."})
    
    def post(self, request):
        book_title=request.POST.get("book_title")
        description=request.POST.get("description")
        visibility=request.POST.get("visibility")
        print('\n', visibility)
        cost=request.POST.get("cost")
        published_year=request.POST.get("published_year")
        book_file=request.FILES.get('book_file')
        obj = uploaded_files(owner=request.user, book_title=book_title, description=description, visibility=visibility, cost=cost, published_year=published_year, book_file=book_file)
        obj.save()
        return render(request, 'app1/dashboard.html',{"msg": "Book uploaded Successfully"})
    
    
@IsUploaded
def MyBookDetailsView(request):
    if request.method == 'GET':
        book_details=uploaded_files.objects.filter(owner=request.user)
        # if uploaded_files.objects.filter(owner=request.user):
        #     print("True")
        # else:
        #     print("False")
        context={ 
            'book_details': book_details,
        }
        if request.user.is_authenticated:
            return render(request, 'app1/my_book_details.html', context)
        return HttpResponseRedirect(reverse('app1:login'))
