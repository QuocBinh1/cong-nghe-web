from django.db import models

# Create your models here.
class contactForm(models.Model):
    username = models.CharField(max_length = 25)
    email = models.EmailField()
    password = models.CharField(max_length=20,default='' ) 


    def __str__(self): # hien ra ten o admin (de nhan biet)
        #  return f"username : {self.username} Email: {self.email} body : {self.body}"
        return self.username
