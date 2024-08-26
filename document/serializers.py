import os

from rest_framework import serializers

from document.analysis import extract_text_from_pdf
from document.models import SaveFile

poppler_path = r'C:\poppler-24.07.0\Library\bin'

class SaveFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaveFile
        fields = ['user', 'file']

