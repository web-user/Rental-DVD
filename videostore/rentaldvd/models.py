from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save, post_save

from django.conf import settings
AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class DvdQuerySet(models.QuerySet):
    pass


class DvdManager(models.Manager):
    def get_queryset(self):
        return DvdQuerySet(self.model, using=self._db)


class Rent(models.Model):
    STATUS_CHOICES = (
        ('took', 'Took the disk'),
        ('returned', 'Returned disk'),
    )

    user            = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)
    status          = models.CharField(max_length=10, choices=STATUS_CHOICES, default='took')
    date_took       = models.DateTimeField(auto_now_add=False, editable=True, blank=True)
    date_returned   = models.DateTimeField(auto_now=True)

    objects = models.Manager()


def rent_pre_save_receiver(sender, instance, *args, **kwargs):

    if instance.status == 'returned':
        print("Return rent")

        obj_rent = Rent.objects.get(id=instance.id)
        print(instance.id)
        obj_rent.delete()

post_save.connect(rent_pre_save_receiver, sender=Rent)

class Dvd(models.Model):
    rent        = models.ForeignKey(Rent, on_delete=models.CASCADE, null=True, default=None, blank=True)
    title       = models.CharField(max_length=120)
    content     = models.TextField()
    updated     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    objects = DvdManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("rentaldvd:detail", kwargs={"id": self.id})