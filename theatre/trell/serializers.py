from rest_framework import serializers
from .models import Movie, MovieTimings
from rest_framework.validators import UniqueTogetherValidator
from django.contrib.auth.models import User 

class userSerializers(serializers.ModelSerializer): 
  
    class Meta: 
        model = User 
        fields =  ('username','password','email')

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('__all__')

class MovieTimingsSerializers(serializers.ModelSerializer):

    
    class Meta:
        model = MovieTimings
        fields = ('movie_name','timings','price','ticket','purchased')
        read_only_fields = ('purchased'),
        validators = [ UniqueTogetherValidator(
                queryset=MovieTimings.objects.all(),
                fields=['movie_name', 'timings']
            )]