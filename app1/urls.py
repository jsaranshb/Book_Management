from .import views
from django.urls import path

app_name = 'app1'

urlpatterns = [
    path('', views.HomeView.as_view(), name="homepage"),
    path('signup/', views.RegisterView.as_view(), name = 'signup'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout_user'),
    path('user_details/', views.AuthorSellersView.as_view(), name="user_details"),
    path('dashboard/', views.BookFilesView.as_view(), name="dashboard"),
    path('my_books/', views.MyBookDetailsView, name="my_books"),
]
