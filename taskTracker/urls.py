from django.contrib import admin
from django.urls import path, include, re_path
from boards.views import ListBoardsView, BoardDetailView


urlpatterns = [
    # Admin routes
    path('admin/', admin.site.urls),

    path('boards-list/', ListBoardsView.as_view(), name='board-list'),
    path('boards/<int:pk>/', BoardDetailView.as_view(), name='board-detail'),


    re_path(r'^auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.jwt')),


]