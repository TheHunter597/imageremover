from django.urls import path
from .views import ImageRemover

urlpatterns = [path("", ImageRemover.as_view())]
