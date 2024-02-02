from django.urls import path
# Импортируем созданное нами представление
from .views import Newslist, NewsDetail
from .views import PostSearchView


urlpatterns = [

   path('', Newslist.as_view()),
   path('<int:pk>', NewsDetail.as_view()),
   path('news/search/', PostSearchView.as_view()),

]