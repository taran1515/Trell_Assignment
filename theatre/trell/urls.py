from django.urls import path,include
from . import views
from rest_framework import routers,authtoken

router = routers.DefaultRouter()
router.register(r'movies', views.AddMovie)
router.register(r'movies_timings', views.AddTimings)
router.register('user', views.userviewsets) 

urlpatterns = [
    path('',include(router.urls)),
    path('api-token-auth/', authtoken.views.obtain_auth_token),
    path('purchase/<int:id>/',views.purchase,name='purchase'),
    path('total_admin/',views.total_admin,name='total_admin'),
]

