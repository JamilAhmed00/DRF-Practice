from django.shortcuts import render

# Create your views here.

from rest_framework import status 
from rest_framework.response import Response

from rest_framework.views import  APIView

from .models import StuInfo
from .serializers import StuSerializers



class StudentAPI(APIView):
    
    
    def get(self, request, pk = None, format = None ):
        
        id = pk
        
        if id is not None:
            
            stu = StuInfo.objects.get(id=id)
            serial = StuSerializers(stu)
            return Response(serial.data)
        
        stu = StuInfo.objects.all()
        serial = StuSerializers(stu, many= True)
        return Response(serial.data)
    
    
    def post(self,request, format = None ):
        
        serial = StuSerializers(data = request.data)
        if serial.is_valid():
            serial.save()
            return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
        
        return Response({'msg': 'Error'}, status=status.HTTP_400_BAD_REQUEST)
    
    
    def put(self, request,pk,  format = None):
               
        id = pk
        
        stu = StuInfo.objects.get(pk=id)
        serial = StuSerializers(stu, data = request.data)
        
        if serial.is_valid():
            
            serial.save()
            return Response({'msg' :'Data Updated'}, status = status.HTTP_200_OK)
       
        return Response(serial.errors, status = status.HTTP_400_BAD_REQUEST)     
                
       
            
            
            


