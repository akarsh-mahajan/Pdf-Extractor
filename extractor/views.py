from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.files.storage import FileSystemStorage
from .utils import extraction
import os

def upload_file(request):
    if request.method == 'POST':
        try:
            uploaded_file = request.FILES['file']
            print(upload_file)
            
            fs = FileSystemStorage()
            fs.save(uploaded_file.name, uploaded_file)
            file_path = uploaded_file.name
            html_content = extraction(file_path)
            os.remove(file_path)
            return render(request, 'result.html', {'html_content': html_content})
        
        except Exception as e:
            error_message = "Either provided document is not invoice or it is not of specified type"
            return render(request, 'upload.html', {'error_message': error_message})

    else:
        return render(request, 'upload.html')
