from django.db import models

# Create your models here.
class UploadFile(models.Model):
    # file = models.FileField(upload_to='%Y/%m/%d')
    file = models.FileField(upload_to='')

    class Meta:
        db_table = 'upload_file'