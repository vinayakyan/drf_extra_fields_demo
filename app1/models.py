from django.db import models


class Profile(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    pro_pic = models.ImageField(upload_to="pro_pics", null= True, blank= True)
    email = models.EmailField()

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
