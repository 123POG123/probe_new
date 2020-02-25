from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .models import Forms
from .forms import ContactForm
from django.utils import timezone


# Create your views here.
def new(request):
    return render(request, 'Wapic.html')


def by(request):
    return render(request, 'Wapic_by.html')


def about_us(request):
    return render(request, 'Wapic_about_us.html')


def contact(request):
    form_contact = Forms.objects.all()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('about_us')
    else:
        form = ContactForm()
    forms_contact = ContactForm()
    context = {
        'form_contact': form_contact,
        'forms_contact': forms_contact,
    }
    return render(request, 'Wapic_contact.html', context)
