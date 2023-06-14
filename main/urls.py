from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('tasks.urls')),
    path('', include('accounts.urls')),
    path("ckeditor5/", include('django_ckeditor_5.urls'), name="ck_editor_5_upload_file"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)






