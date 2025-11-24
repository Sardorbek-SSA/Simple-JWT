from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,AllowAny
from .models import Toy
from .serializers import ToySerializer
from .permissions import IsOwner

class ToyListCreateView(generics.ListCreateAPIView):
    queryset = Toy.objects.all()
    serializer_class = ToySerializer
    permission_classes = [AllowAny]
    
    def perform_create(self,serializer):
        serializer.save(owner=self.user)
        
    @property
    def user(self):
        return self.request.user
    
class ToyUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Toy.objects.all()
    serializer_class = ToySerializer
    permission_classes = [IsAuthenticated,IsOwner]
    