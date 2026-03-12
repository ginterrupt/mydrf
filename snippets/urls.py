#snippets/urls.py

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    path("snippets/",views.SnipetList.as_view()),
    path("snippets/<int:pk>/",views.SnippetDetail.as_view()),
]


urlpatterts = format_suffix_patterns(urlpatterns)