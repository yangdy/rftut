from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter
from snippets.views import SnippetViewSet, UserViewSet

router = DefaultRouter()
router.register(r'snippets', SnippetViewSet)
router.register(r'users', UserViewSet)

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rftut.views.home', name='home'),
    # url(r'^rftut/', include('rftut.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url('^', 'pages.views.index', name='index'),
    url('^api/', include(router.urls)),
    url('^auth/', include('rest_framework.urls', namespace='rest_framework')),
)
