from django.conf.urls import url
from .views import MainPageView, ContactView, success

urlpatterns = [
    url(r'^$', MainPageView.as_view(), name='home'),
    url(r'^contact', ContactView.as_view(), name='contact'),
    url(r'^success', success, name='success'),
]
