from django.shortcuts import render

from django.contrib.auth.models import User, Group
from quickstart.models import player,word
from rest_framework import viewsets
from quickstart.serializers import UserSerializer, GroupSerializer,PlayerSerializer,WordsSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = player.objects.all()
    serializer_class = PlayerSerializer


class WordViewSet(viewsets.ModelViewSet):
    queryset = word.objects.all()
    serializer_class = WordsSerializer
