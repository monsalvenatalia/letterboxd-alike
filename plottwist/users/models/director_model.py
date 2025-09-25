from django.db import models

from django.utils.translations import gettext_lazy as _ 

class Director(models.Model):

    name= models.CharField(
        verbose_name= _("Name"), 
        max_length= 250
    )

    class Meta:
        ordering= ["name"]
        verbose_name= _("Director")
        verbose_name_plural= _("Directors")

    def __str__(self):
        return self.name
    