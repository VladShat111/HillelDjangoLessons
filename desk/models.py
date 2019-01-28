from django.db import models

# Create your models here.
class DeskOfFile(models.Model):

    filename = models.CharField(max_length=60)
    fileForDownload = models.FileField(upload_to='file', blank=True)

    def __str__(self):
        return str(self.filename)


