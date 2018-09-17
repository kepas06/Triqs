from django.contrib.auth.models import User, Group
from rest_framework import serializers
from quickstart.models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = player
        fields = ('url','username','password','highscore','level_id' )


class WordsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = word
        fields = ('url','polish','english','level_id' )
