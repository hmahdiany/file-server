from django.db import models


class Qcow(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='media/')

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.file.delete()
        super().delete(*args, **kwargs)