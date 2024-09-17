from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from Myapp.models import Contact
from django.http import HttpResponse


# Contact form view
@csrf_exempt  # Allowing form submission without CSRF token (not recommended for production)
def Contactus(request):
    if request.method == 'POST':
        # Retrieve form data from the POST request
        name = request.POST.get('name')  # Using .get() to avoid potential KeyError
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # Create a new contact instance and save it to the database
        contact = Contact(Name=name, Email=email, Phone=phone, Message=message)
        contact.save()

        # Redirect to a success page (you need to create this view and template)
        return redirect('success')  # Ensure 'success' URL is defined in your urls.py

    # For non-POST requests, render the contact form
    return render(request, 'Contact.html')
