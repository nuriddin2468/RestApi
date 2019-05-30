from django.urls import path
from api.views import *
urlpatterns = [
    path('', api),
    path('logos/', AddOrView.as_view()),
    path('logo/<int:logo_id>/', DeleteOrUpdateOrView.as_view())
]

