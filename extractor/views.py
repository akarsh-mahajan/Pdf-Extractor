from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.files.storage import FileSystemStorage

def upload_file(request):
    if request.method == 'POST':
        # If the form is submitted
        uploaded_file = request.FILES['file']
        
        # Save the file to a specific location (change the location as needed)
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)

        # Redirect to a success page or perform additional actions
        return HttpResponseRedirect(reverse('success_page'))
    else:
        # If the form is not submitted, display the form
        return render(request, 'upload.html')
