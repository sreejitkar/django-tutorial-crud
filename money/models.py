from django.db import models

# Create your models here.

class Management(models.Model):
    """Model definition for Management."""

    # TODO: Define fields here
    manage_id = models.AutoField(primary_key=True)
    manage_name = models.CharField(max_length=50)

    class Meta:
        """Meta definition for Management."""

        verbose_name = 'Management'
        verbose_name_plural = 'Management'

    def __str__(self):
        """Unicode representation of Management."""
        pass
