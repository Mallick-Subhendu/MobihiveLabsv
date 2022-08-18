from django.db import models
from django.conf import settings
import qrcode
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    address=models.CharField(max_length=200,null=True)
    city=models.CharField(max_length=50,null=True)
    phone=models.IntegerField(null=True)
    date_of_birth = models.DateField(blank=True,null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d',blank=True)

    def __str__(self):
        return f'Profile for user {self.user.username}'
    
    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        print(self.photo)
        imag = Image.open(self.photo.path)
        if imag.width > 200 or imag.height> 200:
            output_size = (200, 200)
            imag.thumbnail(output_size)
            imag.save(self.photo.path)
    
    # def create_qr(Profile, instance, **kwargs):
    #     code = instance.Profile
    #     img = qrcode.make(code)
    #     instance.qr_path = img
    #     print(img)
    #     instance.save()
