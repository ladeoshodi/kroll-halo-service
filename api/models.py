from django.db import models


# Create your models here.
class KrollHaloMapping(models.Model):
    kroll_ticket_id = models.CharField(max_length=255, unique=True)
    halo_ticket_id = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ["created_at"]

    def __str__(self):
        return self.kroll_ticket_id
