from django.core.exceptions import ValidationError

def validate_file_extension(value):
    import os
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.pdf', '.docx', '.pptx']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension. Please upload PDF, DOCX or PPTX.')

def validate_file_size(value):
    filesize = value.size
    if filesize > 5 * 1024 * 1024: # 5MB limit
        raise ValidationError("The maximum file size that can be uploaded is 5MB")