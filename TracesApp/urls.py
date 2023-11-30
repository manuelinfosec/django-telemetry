from django.urls import path

from .views import SampleView

urlpatterns = [
    path("traces", SampleView.as_view(), name="sample-view"),
]
