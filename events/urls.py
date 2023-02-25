from django.urls import path

from events.views import event_list

urlpatterns = [
    path('', event_list, name='event-list'),
]