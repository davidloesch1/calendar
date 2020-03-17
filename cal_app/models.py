from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Event(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    @property
    def get_html_url(self):
        url = reverse('cal_app:event_edit', args=(self.id,))
        return f'<a class="event-card" href="{url}"> {self.title} </a>'
