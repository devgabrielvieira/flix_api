from django.contrib import admin
from django.urls import path, include
from schema_graph.views import Schema

urlpatterns = [
    path('admin/', admin.site.urls),
    path("schema/", Schema.as_view()),

    path('api/v1/', include('authentication.urls')),
    path('api/v1/', include('genres.urls')),
    path('api/v1/', include('actors.urls')),
    path('api/v1/', include('movies.urls')),
    path('api/v1/', include('reviews.urls')),

]
