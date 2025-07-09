from django.db import models
from django.urls import reverse


class Student(models.Model):
    ...

    def get_absolute_url(self):
        return reverse('student-detail', args=[str(self.id)])
