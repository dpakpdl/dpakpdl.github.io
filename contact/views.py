from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from .forms import ContactForm
from django.contrib import messages


def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # send email code goes here
            sender_name = form.cleaned_data['name']
            sender_email = form.cleaned_data['email']

            message = "{0} has sent you a new message:\n{1}".format(sender_name, form.cleaned_data['message'])

            send_mail('New Enquiry', message, sender_email, ['deepakpaudel93@gmail.com'])
            messages.success(request, 'Thanks for contacting us!')
            return HttpResponseRedirect(request.path_info)
    else:
        form = ContactForm()
    return render(request, 'contact_form.html', {'form': form})


