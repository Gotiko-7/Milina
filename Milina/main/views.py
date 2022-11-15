from django.shortcuts import render, redirect
from .models import Contacts
from .forms import ContactsForm

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def wedo(request):
    return render(request, 'main/wedo.html')

def pricing(request):
    return render(request, 'main/pricing.html')

def readmore(request):
    return render(request, 'main/readmore.html')

def experts(request):
    return render(request, 'main/experts.html')



def contact(request):
    error = 'Error'

    if request.method == 'POST':
        print('hi2')
        form = ContactsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactsForm()
    data = {
            'form': form,
            'error': error
        }
    return render(request, template_name='main/contact.html', context=data)




