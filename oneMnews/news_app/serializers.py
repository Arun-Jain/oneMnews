
from rest_framework import serializers
from .models import (
						NewsTypes,
						Country,
						News,
						)

class NewsTypesSerializer(serializers.ModelSerializer):
	class Meta:
		model = NewsTypes
		fields = ('id', 'news_type',)

class CountrySerializer(serializers.ModelSerializer):
	class Meta:
		model = Country
		fields = ('id', 'country_name',)

class NewsSerializer(serializers.ModelSerializer):
	class Meta:
		model = News
		fields = ('id', 'news_type', 'heading', 'image_path', 'news_body', 'is_trending', 'created_at', 'updated_at', 'flag', 'country')
