from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer

#create
class UserCreateView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
#read all
class UserListView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many = true)
        return Response(serializer.data)

#read single
class UserDetailView(APIView):
    def get(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except:
            return Response({"error": "User not found"}, status=404)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
#update
class UserUpdateView(APIView):
    def put(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=404)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
#delete
class UserDeleteView(APIView):
    def delete(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=404)
        user.delete()
        return Response(status=204)
    


"""
user = User.objects.get(pk=pk) dediğimizde burada Django ORM kullanıyoruz.
User.objects User modelinin tüm kayıtlarını temsil eder. 
.get(pk=pk) veritabanından bir tane kayıt çekmeyi temsil etmek için 
kullanılır, burada pk id.

serializer = UserSerializer(user) dediğimizde Django Rest framework
serializerları veriyi json a çevirir veya tersine de olabilir. 
burada user model instance ını alıyoruz ve serializer a veriyoruz.
O kullanıcıyı JSON’a dönüştür, API’de dönebilir hale getir.
"""