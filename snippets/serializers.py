from django.forms import widgets
from rest_framework import serializers
from .models import Snippet

"""
class SnippetSerializer(serializers.Serializer):
  pk = serializers.Field()
  title = serializers.CharField(required=False, max_length=100)
  code = serializers.CharField(widget=widgets.Textarea, max_length=10000)
  linenos = serializers.BooleanField(required=False)

  def restore_object(self, attrs, instance=None):
    if instance:
      instance.title = attrs.get('title', instance.title)
      instance.code = attrs.get('code', instance.code)
      instance.linenos = attrs.get('linenos', instance.linenos)
      return instance

    return Snippet(**attrs)
"""

class SnippetSerializer(serializers.ModelSerializer):
  class Meta:
    model = Snippet
    fields = ('id', 'title', 'code', 'linenos')

