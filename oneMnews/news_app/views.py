from django.shortcuts import render
from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .models import (
						NewsTypes,
						Country,
						News,
						)
from .serializers import (
							NewsTypesSerializer,
							CountrySerializer,
							NewsSerializer,
							)

@api_view(['GET'])
@permission_classes((permissions.IsAuthenticated,))
def all_news(request):
#Returns all news without any filter

	if request.method == 'GET':
		news = News.objects.all()
		serializer = NewsSerializer(news, many=True)
		response_data = serializer.data
		return Response(response_data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def type_news(request, n_type):
#Returns news based on news type
	try:
		news_type_id = NewsTypes.objects.get(news_type=n_type)
	except NewsTypes.DoesNotExist:
		response_data = {'error': 'News Type does not exist'}
		return Response(response_data, status=status.HTTP_406_NOT_ACCEPTABLE)

	if request.method == 'GET':		
		filtered_news = News.objects.filter(news_type=news_type_id.id)
		serializer = NewsSerializer(filtered_news, many=True)
		response_data = serializer.data
		return Response(response_data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def country_news(request, c_type):
#Returns news based on country type
	try:
		country_type_id = Country.objects.get(country_name=c_type)
		
	except Country.DoesNotExist:
		response_data = {'error': 'Country Type does not exist'}
		return Response(response_data, status=status.HTTP_406_NOT_ACCEPTABLE)

	if request.method == 'GET':		
		filtered_news = News.objects.filter(news_type=country_type_id.id)
		if not filtered_news:
			response_data = {'error': 'No news for this country'}
			return Response(response_data, status=status.HTTP_204_NO_CONTENT)

		serializer = NewsSerializer(filtered_news, many=True)
		response_data = serializer.data
		return Response(response_data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def trending_news(request):
#Returns all trending news also flag should be true
	if request.method == 'GET':
		filtered_news = News.objects.filter(is_trending='Y', flag=True)
		serializer = NewsSerializer(filtered_news, many=True)
		response_data = serializer.data
		return Response(response_data, status=status.HTTP_200_OK)
