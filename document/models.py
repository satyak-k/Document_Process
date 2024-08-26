from django.db import models

from document.filepath import pdf_upload_path
from user.models import User


class SaveFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='save_pdf_user')
    file = models.FileField(upload_to=pdf_upload_path)
    text = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.file}'