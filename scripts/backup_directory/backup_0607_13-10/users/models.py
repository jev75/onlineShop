from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(
        verbose_name='Avataras',
        upload_to='image/',
        default='image/default.jpg',
        blank=True,
    )

    class Meta:
        verbose_name = 'Profilis'
        verbose_name_plural = 'Profiliai'

    def __str__(self):
        return self.user.username


