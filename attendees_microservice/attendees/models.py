from django.db import models
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist


class Attendee(models.Model):
    """
    The Attendee model represents someone that wants to attend
    a conference
    """

    email = models.EmailField()
    name = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    conference = models.ForeignKey(
        "ConferenceVO",
        related_name="attendees",
        on_delete=models.CASCADE,
    )

    def create_badge(self):
        try:
            self.badge
        except ObjectDoesNotExist:
            Badge.objects.create(attendee=self)

    def __str__(self):
        return self.name

    def get_api_url(self):
        return reverse("api_show_attendee", kwargs={"id": self.id})


class Badge(models.Model):
    """
    The Badge model represents the badge an attendee gets to
    wear at the conference.

    Badge is a Value Object and, therefore, does not have a
    direct URL to view it.
    """

    created = models.DateTimeField(auto_now_add=True)

    attendee = models.OneToOneField(
        Attendee,
        related_name="badge",
        on_delete=models.CASCADE,
        primary_key=True,
    )


class ConferenceVO(models.Model):
    import_href = models.CharField(max_length=200, unique=True)
    name = models.CharField(max_length=200)
