from django.urls import path

from events.api.views import EventList

urlpatterns = [
    path('', EventList.as_view())
]
