from django.urls import include, re_path
from django.urls import path
from .import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('neww', views.newOneView)

accounts_urlpatterns = [
    path('', include(router.urls)),
    # path('new/', views.newView.as_view()),
    re_path(r'^api/v1/', include('djoser.urls')),
    re_path(r'^api/v1/', include('djoser.urls.authtoken')),
]
