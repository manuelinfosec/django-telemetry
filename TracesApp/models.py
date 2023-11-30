"""Models for TracesApp"""

import uuid
from django.db import models


class Logs(models.Model):
    """Stores log outputs generated from traces"""

    id = models.UUIDField(primary_key=True, default=uuid.UUID)
    message = models.TextField()
