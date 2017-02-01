"""fooapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]

# you'll need to add the include import
from django.conf.urls import url, include
from django.contrib import admin

# here we import the router from our views.py
# the router handles all url mapping for our app
from user.views import router

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # This includes all our registered ViewSets
    url(r'^', include(router.urls)),

    # This provides the ability to login to the app
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]

## Setting up static files for development:
if settings.DEBUG == True:
  urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
