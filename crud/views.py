from django.shortcuts import render
from .serializer import Studentserilaiser
from .models import Student
from rest_framework.response import Response
from rest_framework import status,viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly,DjangoModelPermissionsOrAnonReadOnly




class Student_view(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = Studentserilaiser

    authentication_classes = [SessionAuthentication]
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    

    

    
    


        


        




# Create your views here.
