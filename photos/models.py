from django.db import models


# Create your models here.

class Photo(models.Model):
    PORTRAIT = 'Portrait'
    LANDSCAPE = 'Landscape'
    PANORAMA = 'Panorama'
    UNKNOWN = 'unknown'
    PHOTO_TYPES = (
        (PORTRAIT, 'Portrait'),
        (LANDSCAPE, 'Landscape'),
        (PANORAMA, 'Panorama'),
        (UNKNOWN, 'unknown'),
    )
    type = models.CharField(max_length=15, choices=PHOTO_TYPES, default=UNKNOWN)
    title = models.CharField(max_length=15, blank=False)
    date = models.DateTimeField(blank=False)
    description = models.TextField(blank=False)
    image_url = models.URLField(blank=False)

    def __str__(self):
        return f'{self.id}; {self.title}; {self.date};'


class Like(models.Model):
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.photo}'


class Comment(models.Model):
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    text = models.TextField(blank=False)