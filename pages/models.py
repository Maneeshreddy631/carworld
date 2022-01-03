from django.db import models

# Create your models here.
class Team(models.Model) : #class name shoud be singular form here team is class name
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    designation = models.CharField(max_length = 255)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    facebook_link = models.URLField(max_length = 100)
    twitter_link = models.URLField(max_length = 100)
    google_plus_link = models.URLField(max_length=100)
    created_date = models.DateTimeField(auto_now_add = True)
    

    def __str__(self) : #self mean we are taking about above specified class in which we are writing this def functions
        return self.first_name

