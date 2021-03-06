from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from snippets import views
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title='Django Rest Framework Tutorial')

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    url(r'^schema/$', schema_view),
    url(r'^', include(router.urls)),
]

# Api auth urls
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls')),

]

# Urls automagically added by the DefaultRouter following conventions
# snippet_list = SnippetViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# snippet_detail = SnippetViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
# snippet_highlight = SnippetViewSet.as_view({
#     'get': 'highlight'
# }, renderer_classes=[renderers.StaticHTMLRenderer])
# user_list = UserViewSet.as_view({
#     'get': 'list'
# })
# user_detail = UserViewSet.as_view({
#     'get': 'retrieve'
# })