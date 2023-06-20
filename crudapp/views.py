from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from .forms import ContactForm
from django.views.generic import ListView, DetailView
from .forms import CoreForm
from django.views.generic.edit import FormView
from django.urls import reverse_lazy


class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'contact_list'

    def get_queryset(self):
        return Contact.objects.all()

class ContactDetailView(DetailView):
    model = Contact
    template_name = 'contact-detail.html'

def create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = ContactForm()

    return render(request,'create.html',{'form': form})

def edit(request, pk, template_name='edit.html'):
    contact = get_object_or_404(Contact, pk=pk)
    form = ContactForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, template_name, {'form':form})

def delete(request, pk, template_name='confirm_delete.html'):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method=='POST':
        contact.delete()
        return redirect('index')
    return render(request, template_name, {'object':contact})

class CoreFormView(FormView):
    template_name = 'core.html'
    form_class = CoreForm
    success_url = reverse_lazy('core_list')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)