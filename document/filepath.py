from datetime import datetime


def pdf_upload_path(instance, filename):
    return f'pdf/{datetime.now().year}/{datetime.now().month}/{datetime.now().day}/{filename}'

def image_upload_path(instance, filename):
    return f'image/{datetime.now().year}/{datetime.now().month}/{datetime.now().day}/{filename}'
