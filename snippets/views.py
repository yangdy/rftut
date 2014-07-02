from rest_framework import viewsets
from rest_framework import permissions
from django.contrib.auth.models import User
from .models import Snippet
from .serializers import SnippetSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly

from rest_framework import renderers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

@api_view(('GET',))
def api_root(request, format=None):
  return Response({
    'users': reverse('user-list', request=request, format=format),
    'snippets': reverse('snippet-list', request=request, format=format),
  })


class UserViewSet(viewsets.ReadOnlyModelViewSet):
  """
  This viewset automatically provides `list` and `detail` actions.
  """
  queryset = User.objects.all()
  serializer_class = UserSerializer

class SnippetViewSet(viewsets.ModelViewSet):
  """
  This viewset automatically provides `list`, `create`, `retrieve`,
  `update` and `destroy` actions.
  """
  queryset = Snippet.objects.all()
  serializer_class = SnippetSerializer
  permissions_class = (permissions.IsAuthenticatedOrReadOnly,
                       IsOwnerOrReadOnly,)

  def pre_save(self, obj):
    obj.owner = self.request.user


