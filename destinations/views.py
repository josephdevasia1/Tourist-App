from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Destination
from .serializers import DestinationSerializer
from django.views import View
from .forms import DestinationForm


# Edit (Update) view for a destination
class DestinationUpdateView(UpdateView):
    model = Destination
    form_class = DestinationForm
    template_name = 'destinations/destination_form.html'
    context_object_name = 'destination'

    def get_success_url(self):
        return reverse_lazy('destination-detail', kwargs={'id': self.object.id})

# Delete view for a destination
class DestinationDeleteView(DeleteView):
    model = Destination
    template_name = 'destinations/destination_confirm_delete.html'
    context_object_name = 'destination'

    def get_success_url(self):
        return reverse_lazy('destination-list')  # Redirect to the destination list after deletion

# List view for destinations (function-based view)
def destination_list_view(request):
    destinations = Destination.objects.all()
    return render(request, 'destinations/destination_list.html', {'destinations': destinations})

# Detail view for a specific destination
def destination_detail_view(request, id):
    destination = get_object_or_404(Destination, id=id)
    return render(request, 'destinations/destination_detail.html', {'destination': destination})

# Pagination class for API views
class DestinationPagination(PageNumberPagination):
    page_size = 10  # Set the number of items per page

# API ViewSet for destinations
class DestinationViewSet(viewsets.ModelViewSet):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer
    pagination_class = DestinationPagination

# Class-based view for creating a destination
class DestinationCreateView(View):
    def get(self, request):
        form = DestinationForm()
        return render(request, 'destinations/destination_form.html', {'form': form})

    def post(self, request):
        form = DestinationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('destination-list')  # Redirect to the destination list after successful creation
        return render(request, 'destinations/destination_form.html', {'form': form})
