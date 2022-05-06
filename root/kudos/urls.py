from django.urls import path

from root.kudos import views

app_name = "kudos"
urlpatterns = [
    path("", views.kudos_list_view, name="kudos_list"),
    path("create/", views.kudos_create_view, name="send_kudos"),
]
