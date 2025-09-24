
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from Tour import views

urlpatterns = [
    # custom admin views first
    path("admin/planner/<int:profile_id>/", views.admin_planner_detail, name="admin_planner_detail"),
    path("admin/dashboard/", views.admin_dashboard, name="admin_dashboard"),
    path("admin/subscription/<int:sub_id>/edit/", views.admin_subscription_edit, name="admin_subscription_edit"),
    path("admin/subscription/<int:sub_id>/toggle/", views.admin_subscription_toggle, name="admin_subscription_toggle"),

    # then the real Django admin
    path("admin/", admin.site.urls),

    # app urls
    path("", include("Tour.urls")),
    path("", include("django.contrib.auth.urls")),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
