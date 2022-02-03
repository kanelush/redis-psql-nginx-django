from django.shortcuts import render, get_object_or_404
from .models import Category, Negocio
from django.views.generic import DetailView
from django.views.generic.edit import FormMixin
from .forms import ContactForm
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import time
from django.views.decorators.cache import cache_page

# Create your views here.
@cache_page(60 * 60)
def base(request):
    category = Category.objects.all()
    negocio = Negocio.objects.all()
    context = {
        'category': category,
        'negocio': negocio,
    }
    
    return render(request, 'frontpage.html', context)

@cache_page(60 * 60)
def list(request, category_id):
    categories = Category.objects.all()
    category = get_object_or_404(Category, pk=category_id)

    context = {
        
        'category': category,
        'negocio': Negocio.objects.filter(category_id=category_id),
        'categories': categories
        
    }
    
    return render(request, 'list.html', context)

@cache_page(60 * 60)
def contact(request):
    return render(request, 'contacto.html')


class NegocioDetailView(FormMixin, DetailView):
    model = Negocio
    form_class = ContactForm
    template_name = 'detail.html'
    slug_field = 'negocio_slug'
    context_object_name = 'negocio'

    def  get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        
        return context

    def post(self, request, slug, *args, **kwargs):
        if request.method == 'POST':
            form = ContactForm(request.POST)

            if form.is_valid():
                name = form.cleaned_data['name']
                subject = form.cleaned_data['subject']
                mail = form.cleaned_data['mail']
                description = form.cleaned_data['description']
                form.save()
                time.sleep(0.6)


                
                form = ContactForm()


        else:
            form = ContactForm()
        
        return HttpResponseRedirect(reverse('detail', args=[slug]))
