from django.forms import widgets
from rest_framework import serializers
from .models import Snippet
from django.contrib.auth.models import User

class SnippetSerializer(serializers.ModelSerializer):
  owner = serializers.Field(source='owner.username')
  
  class Meta:
    model = Snippet
    fields = ('id', 'title', 'code', 'linenos', 'owner')

class UserSerializer(serializers.ModelSerializer):
  snippets = serializers.PrimaryKeyRelatedField(many=True)

  class Meta:
    model = User
    fields = ('id', 'username', 'snippets')

