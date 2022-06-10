import re
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import send_mass_mail, send_mail
from django.core import mail
from django.contrib import messages

from .forms import EmailForm

def indexView(request):

    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data.get('subject')
            message = form.cleaned_data.get('message')

            mail_list = form.cleaned_data.get('to_email_list')
            emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", mail_list)

            res = send_mail(subject, message, 'bcgcrysis2@gmail.com', emails, fail_silently=False)
            if res:
                messages.add_message(request, messages.INFO, 'Mail Send Successfully.')
                return redirect(reverse('index'))
        else:
            print("No data available....")
    else:
        form = EmailForm()

    data = {'form': form}
    return render(request, 'bulkemailsenderapp/pages/index.html', data)