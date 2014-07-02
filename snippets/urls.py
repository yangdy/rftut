from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import SnippetViewSet, UserViewSet
from rest_framework import renderers

snippet_list = SnippetViewSet.as_view({
  'get': 'list',
  'post': 'create'
})

snippet_deail = SnippetViewSet.as_view({
  'get': 'retrieve',
  'put': 'update',
  'patch': 'partial_update',
  'delete': 'destroy'
})

user_list = UserViewSet.as_view({
  'get': 'list'
})

user_detail = UserViewSet.as_view({
  'get': 'retrieve'
})

urlpatterns = patterns('snippets.views',
  url(r'^$', 'api_root'),
  url(r'^snippets/$', snippet_list, name='snippet-list'),
  url(r'^snippets/(?P<pk>[0-9]+)/$', snippet_deail, name='snippet-detail'),
  url(r'^users/$', user_list, name='user-list'),
  url(r'^users/(?P<pk>[0-9]+)/$', user_detail, name='user-detail'),
)

urlpatterns = format_suffix_patterns(urlpatterns)
