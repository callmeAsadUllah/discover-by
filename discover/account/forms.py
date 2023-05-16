from django import forms
from django.forms import (
    Form,
    ModelForm
)



from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class LoginForm(Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'special'}))
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'

        self.helper.add_input(Submit('submit', 'Submit'))