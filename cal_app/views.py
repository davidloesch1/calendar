from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime, timedelta
from django.views import generic
from django.utils.safestring import mark_safe
import calendar
from .forms import EventForm, SignUpForm
from .models import *
from .utils import Calendar
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

def index(request):
    return HttpResponse('hello')


class CalendarView(generic.ListView):
    model = Event
    template_name = 'cal_app/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        cal = Calendar(d.year, d.month, self.request.user.id)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        return context

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return datetime(year, month, day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        print(form)
        form.username = request.POST.get('email')
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            print(form.cleaned_data)
            print(raw_password)
            user = authenticate(username=username, password=raw_password)
            print (user)
            login(request, user)
            return redirect('/calendar')
    else:
        form = SignUpForm()
    return render(request, 'cal_app/signup.html', {'form': form})

@login_required
def new(request):
    instance = Event()
    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        event = form.save(commit=False)
        event.owner = request.user
        event.save()
        return HttpResponseRedirect(reverse('cal_app:calendar'))
    return render(request, 'cal_app/event.html', {'form': form})

@login_required
def edit(request, event_id):
    instance = get_object_or_404(Event, pk=event_id)
    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('cal_app:calendar'))
    return render(request, 'cal_app/edit.html', {'form': form, 'event_id': event_id})

@login_required
def delete(request, event_id=None):
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
        instance.delete()
    else:
        return HttpResponseRedirect(reverse('cal_app:calendar'))
    return HttpResponseRedirect(reverse('cal_app:calendar'))
