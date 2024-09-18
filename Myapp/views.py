from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from Myapp.models import Contact,Feedback
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


def feedback_view(request):  # Rename the view function to avoid conflict
     if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        product = request.POST.get('product')
        message = request.POST.get('message')
        
        # Create a new feedback instance and save it to the database
        feedback = Feedback(Name2=name, Email2=email, Phone2=phone, Product2=product, Message2=message)
        feedback.save()

        return redirect('feedback_view')  # Update redirect to the new view name    
     return render(request, 'Feed.html')