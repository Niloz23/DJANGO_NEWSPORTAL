from django.urls import path
# Импортируем созданное нами представление
from .views import Newslist, NewsDetail


urlpatterns = [

   path('', Newslist.as_view()),
   path('<int:pk>', NewsDetail.as_view()),

]