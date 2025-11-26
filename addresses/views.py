from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Address
from .serializers import AddressSerializer

#create
class AddressCreateView(APIView):
    def post(self, request):
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

#read
class AddressListView(APIView):
    def get(self, request):
        addresses = Address.objects.all()
        serializer = AddressSerializer(addresses, many=True)
        return Response(serializer.data)

#read single
class AddressDetailView(APIView):
    def get(self, request, pk):
        try:
            address = Address.objects.get(pk=pk)
        except Address.DoesNotExist:
            return Response({"error": "Address not found"}, status=404)
        serializer = AddressSerializer(address)
        return Response(serializer.data)

#update
class AddressUpdateView(APIView):
    def put(self, request, pk):
        try:
            address = Address.objects.get(pk=pk)
        except Address.DoesNotExist:
            return Response({"error": "Address not found"}, status=404)
        serializer = AddressSerializer(address, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

#delete
class AddressDeleteView(APIView):
    def delete(self, request, pk):
        try:
            address = Address.objects.get(pk=pk)
        except Address.DoesNotExist:
            return Response({"error": "Address not found"}, status=404)
        address.delete()
        return Response(status=204)
