"""The URLconfig of the music app."""


from django.urls import path

from music import views

urlpatterns = [
    path('', views.index, name='index')
]

# urlpatterns += [
#     path('performers/<int:pk>', views.performer_detail, name='performer-detail')
# ]

urlpatterns += [
    path('performers/', views.PerformerListView.as_view(), name='performer-list')
]

urlpatterns += [
    path('performers/<int:pk>/', views.PerformerDetailView.as_view(), name='performer-detail')
]

urlpatterns += [
    path('songs/', views.SongListView.as_view(), name='song-list')
]

urlpatterns += [
    path('songs/<int:pk>/', views.SongDetailView.as_view(), name='song-detail')
]

urlpatterns += [
    path('performers/create/', views.PerformerCreate.as_view(), name='performer-create'),
    path('performers/<int:pk>/update/', views.PerformerUpdate.as_view(), name='performer-update'),
    path('performers/<int:pk>/delete/', views.PerformerDelete.as_view(), name='performer-delete'),
]

urlpatterns += [
    path('songs/create/', views.SongCreate.as_view(), name='song-create'),
    path('songs/<int:pk>/update/', views.SongUpdate.as_view(), name='song-update'),
    path('songs/<int:pk>/delete/', views.SongDelete.as_view(), name='song-delete'),
]

