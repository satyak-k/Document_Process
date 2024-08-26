import os

from rest_framework import status, generics
from rest_framework.response import Response

from document.analysis import extract_text_from_pdf, text_analysis, extract_text_from_image
from document.serializers import SaveFileSerializer

poppler_path = r'C:\poppler-24.07.0\Library\bin'


class ExtractAndSaveFileUploadView(generics.CreateAPIView):
    serializer_class = SaveFileSerializer

    def post(self, request, *args, **kwargs):
        file = request.FILES.get('file')
        user = request.data.get('user')

        if not file or not user:
            return Response({'error': 'File and user are required'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()
            file_path = instance.file.url
            modified_path = file_path.replace('/media/', '')
            fp = os.path.join('media', modified_path)

            filename = file.name.lower()
            if filename.endswith(('.png', '.jpg', '.jpeg', '.gif')):
                extracted_text = extract_text_from_image(file, 'eng+spa')
            else:
                extracted_text = extract_text_from_pdf(fp, poppler_path, 'eng')
            instance.text = extracted_text
            instance.save()
            analysis = text_analysis(extracted_text.replace('\n', ' '))
            return Response({
                'success': True,
                'message': 'successfully saved file and analysis',
                'data': {
                    'extracted_text': extracted_text,
                    'analysis': analysis
                }
            })
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
