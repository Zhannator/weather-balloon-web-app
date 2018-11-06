from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^graph/', views.graph_data, name='graph_data'),
	url(r'^gallery/', views.gallery_data, name='gallery_data'),
	url(r'^$', TemplateView.as_view(template_name='homepage.html'), name='homepage'),
]