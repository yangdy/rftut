from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Snippet
from .serializers import SnippetSerializer

@api_view(['GET', 'POST'])
def snippet_list(request, format=None):
  """
  List all snippets, or create a snippet.
  """
  if request.method == 'GET':
    snippets = Snippet.objects.all()
    serializer = SnippetSerializer(snippets, many=True)
    return Response(serializer.data)

  elif request.method == 'POST':
    serializer = SnippetSerializer(data=request.DATA)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def snippet_detail(request, pk, format=None):
  """
  Retrieve, update or delete a code snippet.
  """
  try:
    snippet = Snippet.objects.get(pk=pk)
  except Snippet.DoesNotExist:
    return Response(status=status.HTTP_400_NOT_FOUND)

  if request.method == 'GET':
    serializer = SnippetSerializer(snippet)
    return Response(serializer.data)

  if request.method == 'PUT' or request.method == 'PATCH':
    serializer = SnippetSerializer(snippet, data=request.DATA)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  if request.method == 'DELETE':
    snippet.delete()
    return HttpResponse(status=status.HTTP_204_CREATED)
