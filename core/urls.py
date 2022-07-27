from django.urls import path

from core.views import HelloView

urlpatterns = [
    path('', HelloView.as_view(), name='hello'),

]
