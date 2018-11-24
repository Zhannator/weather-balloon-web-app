from django.conf.urls import url
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^graph/', views.graph_data, name='graph_data'),
	url(r'^gallery/', views.gallery_data, name='gallery_data'),
	url(r'^$', TemplateView.as_view(template_name='homepage.html'), name='homepage'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)