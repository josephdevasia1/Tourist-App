from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DestinationUpdateView, DestinationDeleteView
from .views import (
    DestinationViewSet,
    destination_list_view,
    destination_detail_view,
    DestinationCreateView
)

# Create a router and register the DestinationViewSet
router = DefaultRouter()
router.register(r'destinations', DestinationViewSet)

urlpatterns = [
    path('api/', include(router.urls)),  # API routes handled by the router
    path('destinations/', destination_list_view, name='destination-list'),  # List view for destinations
    path('destinations/<int:id>/', destination_detail_view, name='destination-detail'),  # Detail view
    path('destinations/<int:pk>/edit/', DestinationUpdateView.as_view(), name='destination-edit'),
    path('destinations/<int:pk>/delete/', DestinationDeleteView.as_view(), name='destination-delete'),
    path('create/', DestinationCreateView.as_view(), name='destination-create'),  # Destination creation view
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
