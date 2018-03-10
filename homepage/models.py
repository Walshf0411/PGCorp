from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse


class Flat(models.Model):
    slug = models.SlugField(unique=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    image = models.FileField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    nearest_railway_station = models.CharField(max_length=100)
    number_of_members = models.IntegerField()
    PREFERRED_GUESTS = (('Employee', 'Employee'), ('Student', 'Student'))
    HOUSE_TYPE = (('1 BHK', '1 BHK'), ('2 BHK', '2 BHK'), ('3 BHK', '3 BHK'), ('4 BHK', '4 BHK+'))
    price_negotiable = models.BooleanField(default=False)
    description = models.TextField()
    preferred_guests = models.CharField(max_length=10, choices=PREFERRED_GUESTS, default='Student')
    house_type = models.CharField(max_length=10, choices=HOUSE_TYPE, default='1 BHK')

    def get_absolute_url(self):
        return reverse('url homepage:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return 'Nearest Rail : '+str(self.nearest_railway_station)+" id : "+str(self.pk)
