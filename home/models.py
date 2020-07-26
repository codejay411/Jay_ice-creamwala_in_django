from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    desc=models.TextField()
    date=models.DateField()


    # makemigrations--> create chnages and store in the file
    # migrate--> apply the pending changes created by makemigrations

    # this set the value of content of table by their name
    def __str__(self):
        return self.name



