from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import NewSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import new_one
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

# Create your views here.
# class newView(APIView):
#     authentication_classes=[TokenAuthentication]
#     permission_classes=[IsAuthenticated]
#     serializer_Class=NewSerializer
    
#     def get(self, request):
#         queryset=new_one.objects.all()
#         print(queryset)
#         serializer=self.serializer_Class(queryset, many=True)
#         print(serializer)
#         return Response(serializer.data)
        
class newOneView(ModelViewSet):
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated,]
    serializer_class = NewSerializer
    queryset = new_one.objects.all()