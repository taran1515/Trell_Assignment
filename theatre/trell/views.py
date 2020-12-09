from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Movie,MovieTimings
from .serializers import MovieSerializer,MovieTimingsSerializers,userSerializers
from django.http import JsonResponse
from django.contrib.auth.models import User 
# Create your views here.


  
  
class userviewsets(viewsets.ModelViewSet): 
    queryset = User.objects.all() 
    serializer_class = userSerializers 

class AddMovie(viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()

class AddTimings(viewsets.ModelViewSet):
    # authentication_classes = [TokenAuthentication,]
    # permission_classes = [IsAuthenticated]

    serializer_class = MovieTimingsSerializers
    queryset = MovieTimings.objects.all()


# def add_timings(request):
#     if request.method == 'POST':


def purchase(request,id):
    if request.method=='GET':
        # print(id)
        movies = MovieTimings.objects.filter(movie_name=id)
        # print(movie)
        for movie in movies:
            movie.purchased = True
            movie.save()
        data = {
            'message':'purchase successfull'
        }
        return JsonResponse(data)

def total_admin(request):
    if request.method=='GET':
        admin = User.objects.count()
        if(admin>0):
            data = {
                'message':'login'
            }
        else:
            data = {
                'message':'sign_up'
            }

        return JsonResponse(data)
