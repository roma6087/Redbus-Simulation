from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Userdetails(User):
    user=models.OneToOneField(User,parent_link=True,primary_key=True,on_delete=models.CASCADE)
  

    def __str__(self):
        return self.user.username
