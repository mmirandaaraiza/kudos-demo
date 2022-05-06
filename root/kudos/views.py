from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import CreateView, ListView

from root.kudos.forms import KudosForm
from root.kudos.models import Kudos


class KudosListView(LoginRequiredMixin, ListView):
    model = Kudos

    def get_queryset(self):
        return self.model._default_manager.filter(receiver=self.request.user)


kudos_list_view = KudosListView.as_view()


class KudosCreateView(LoginRequiredMixin, CreateView):
    model = Kudos
    form_class = KudosForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.sender = self.request.user

        self.request.user.kudos_left -= 1
        self.request.user.full_clean()
        self.request.user.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse("kudos:kudos_list")


kudos_create_view = KudosCreateView.as_view()
