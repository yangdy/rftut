from django.forms import widgets
from rest_framework import serializers
from .models import Snippet
from django.contrib.auth.models import User

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
  owner = serializers.Field(source='owner.username')

  class Meta:
    model = Snippet
    fields = ('url', 'title', 'code', 'linenos', 'owner')

class UserSerializer(serializers.HyperlinkedModelSerializer):
  snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail')

  class Meta:
    model = User
    fields = ('url', 'username', 'snippets')

