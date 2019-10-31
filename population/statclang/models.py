from django.db import models

# Create your models here.

class Population(models.Model):
    """Model definition for Population."""
    nom = models.CharField(max_length=255)
    nbre_habitant = models.PositiveIntegerField(default=0)
    # TODO: Define fields here

    class Meta:
        """Meta definition for Population."""

        verbose_name = 'Population'
        verbose_name_plural = 'Populations'

    def __str__(self):
        """Unicode representation of Population."""
        return self.nom
