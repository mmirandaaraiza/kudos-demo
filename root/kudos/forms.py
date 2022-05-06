from django import forms

from root.kudos.models import Kudos


class KudosForm(forms.ModelForm):
    class Meta:
        model = Kudos
        fields = ["receiver"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user")
        super().__init__(*args, **kwargs)
        self.fields["receiver"].queryset = self.user.organization.user_set.exclude(
            id=self.user.id
        )

    def clean(self):
        if self.user.kudos_left < 1:
            self.add_error(None, "User can't send any more kudos")

        return self.cleaned_data
