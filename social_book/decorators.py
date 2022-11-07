from django.http import HttpResponseRedirect
from django.core.exceptions import PermissionDenied
from app1.models import CustomUser, uploaded_files
from django.urls import reverse

def IsVisible(get):
    def wrap(request, *args, **kwargs):
        if CustomUser.public_visibility == True :
            return get(request, *args, **kwargs)
        else:
            return PermissionDenied
    return wrap

def IsUploaded(view_func):
    def wrap(request, *args, **kwargs):
        if uploaded_files.objects.filter(owner=request.user):
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('app1:dashboard'))
    return wrap
