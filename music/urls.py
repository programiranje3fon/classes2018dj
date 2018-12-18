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
    path('performers/<int:pk>', views.PerformerDetailView.as_view, name='performer-detail')
]

