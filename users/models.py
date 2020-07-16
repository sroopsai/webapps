from django.db import models


# Create your models here.
class User(models.Model):
    first_name = models.CharField("the user's first name", max_length=30)
    last_name = models.CharField("the user's last name", max_length=30)
    cars = models.ManyToManyField('Car', verbose_name="the user's cars")

    def __str__(self):
        return self.first_name + self.last_name


STATUS_CHOICES = (
    ('R', 'Reviewed'),
    ('N', 'Not Reviewed'),
    ('A', 'Accepted'),
    ('E', 'Error')
)


class WebApps(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField(unique=True)
    release_date = models.DateField()
    rating = models.IntegerField()
    status = models.CharField(choices=STATUS_CHOICES, max_length=1)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


class Car(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
