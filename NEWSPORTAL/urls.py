from django.urls import path, include
from .views import PostList, PostDetail, PostCreate, PostUpdate, PostDelete, subscribe,PostSearchView
from .views import IndexView
from .views import CategoryListView



urlpatterns = [
   path('i18n/', include('django.conf.urls.i18n')),
   path('', PostList.as_view()),
   path('<int:pk>', PostDetail.as_view()),
   path('search/', PostSearchView.as_view()),
   path('create/', PostCreate.as_view(), name='news_create'),
   path('<int:pk>/edit/', PostUpdate.as_view(), name='news_edit'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='news_delete'),
   path('articles/create/', PostCreate.as_view(), name='articles_create'),
   path('articles/<int:pk>/edit/', PostUpdate.as_view(), name='articles_edit'),
   path('articles/<int:pk>/delete/', PostDelete.as_view(), name='articles_delete'),
   path('profile/', IndexView.as_view()),
   path('categories/<int:pk>', CategoryListView.as_view(), name='category_list'),
   path('categories/<int:pk>/subscribe', subscribe, name='subscribe'),

]