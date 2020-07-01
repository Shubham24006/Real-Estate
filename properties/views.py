from django.shortcuts import render, get_object_or_404
from .models import Property
from .forms import PropertyForm
from django.views.generic import CreateView, UpdateView, DeleteView
from .decorators import user_authenticate
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy, reverse
# Create your views here.


def listing(request, property_id):
    property = Property.objects.get(id=property_id)
    context = {
        'property': property,
    }
    return render(request, 'properties/listing.html', context)


def listing_slug(request, property):
    property = get_object_or_404(Property, slug=property)
    context = {
        'property': property,
    }
    return render(request, 'properties/listing.html', context)


def listings(request):
    properties = Property.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(properties, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    return render(request, 'properties/listings.html', {'properties': paged_listings})


@method_decorator(user_authenticate, name='dispatch')
class SaveProperty(CreateView):
    model = Property
    form_class = PropertyForm
    template_name = 'properties/propertyform.html'

    def get_success_url(self):
        return reverse('dashboard', kwargs={'pk': self.request.user.id})

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.profile = self.request.user
        self.object.save()
        return super(SaveProperty, self).form_valid(form)


class PropertyUpdate(UpdateView, SuccessMessageMixin):
    success_message = 'Update sucessfully'
    template_name = 'properties/propertyform.html'
    form_class = PropertyForm
    queryset = Property.objects.all()

    def get_success_url(self):
        return reverse('dashboard', kwargs={'pk': self.request.user.id})


class DeleteProperty(DeleteView, SuccessMessageMixin):
    success_message = 'Delete Sucessfully'
    model = Property
    success_url = '/'

    def get_success_url(self):
        return reverse('dashboard', kwargs={'pk': self.request.user.id})
