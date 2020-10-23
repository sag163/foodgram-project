"""assistant_product URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from recipe import additional_views
from recipe.additional_views import *
from django.conf import settings
from django.conf.urls.static import static
import debug_toolbar
from django.contrib.flatpages import views
from django.conf.urls import handler404, handler500

urlpatterns = [
    path("admin/", admin.site.urls),
    path("about/", include("django.contrib.flatpages.urls")),
    path("auth/", include("users.urls")),
    path("auth/", include("django.contrib.auth.urls")),
    path("ingredients/", additional_views.get_ingredients, name="ingredients"),
    path("about_author/", views.flatpage, {"url": "/author/"}, name="author"),
    path("", include("recipe.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    urlpatterns += (path("__debug__/", include(debug_toolbar.urls)),)

handler404 = "recipe.views.page_not_found"
handler500 = "recipe.views.server_error"
