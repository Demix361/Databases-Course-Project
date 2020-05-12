from django.db import models
from django.contrib.auth.models import User
import cv2


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = cv2.imread(self.image.path)
        h = img.shape[0]
        w = img.shape[1]

        if h > w:
            img = img[(h - w) // 2:h - (h - w - (h - w) // 2), :]
        else:
            img = img[:, (w - h) // 2:w - (w - h - (w - h) // 2)]

        img = cv2.resize(img, (300, 300), interpolation=cv2.INTER_AREA)

        cv2.imwrite(self.image.path, img)
