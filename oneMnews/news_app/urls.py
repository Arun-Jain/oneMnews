from django.urls import path, include
from oneMnews import urls
from . import views

urlpatterns = [
	path(r'news/', views.all_news),
	path(r'news/trending/', views.trending_news),
	path(r'news/<str:n_type>/', views.type_news),
	path(r'news/country/<str:c_type>/', views.country_news),
]
