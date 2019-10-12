from django.urls import path, include
from oneMnews import urls
from . import views

urlpatterns = [
	path(r'news/', views.all_news, name="all_news"),
	path(r'news/trending/', views.trending_news, name="trending_news"),
	path(r'news/<str:n_type>/', views.type_news, name="news_type"),
	path(r'news/country/<str:c_type>/', views.country_news, name="country_news_type"),
]
