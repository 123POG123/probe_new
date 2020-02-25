from django.db import models
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,Submit


# Create your models here.
class Forms(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True,help_text='123')
    email = models.EmailField(max_length=50, blank=True, null=True,help_text='123')
    fone = models.IntegerField(blank=True, null=True,help_text='123')
    description = models.TextField(max_length=300, blank=True, null=True,help_text='123')

    def __str__(self):
        return self.name

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper
    #     self.helper.form_method='post'
    #     self.helper.layout =Layout(
    #         'name',
    #         'email',
    #         'fone',
    #         'description ',
    #     )
