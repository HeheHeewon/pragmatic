from django.urls import path

from profileapp.views import ProfileCreateViw

app_name='profileapp'

urlpatterns= [
    path('create/', ProfileCreateViw.as_view(),name='create'),
]