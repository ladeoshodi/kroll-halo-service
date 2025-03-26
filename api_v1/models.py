from django.db import models


# Create your models here.
class KrollHaloMapping(models.Model):
    kroll_ticket_id = models.StringField(max_length=255)
    halo_ticket_id = models.StringField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class meta:
        db_table = "kroll_halo_mapping"
        unique_together = ("kroll_id", "halo_id")
        ordering = ["created_at"]
