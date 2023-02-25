from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import render

from events.forms import EventForm
from events.models import Event
from events.permissions import IsAdminOrReadOnly


@login_required
def event_list(request):
    events = Event.objects.all()
    form = EventForm()

    if request.method == 'POST':
        if not IsAdminOrReadOnly().has_permission(request, None):
            return HttpResponseForbidden()
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = EventForm()

    return render(request, 'event_list.html', {'events': events, 'form': form})
