from django import forms
from .models import Forms


class ContactForm(forms.ModelForm):
    class Meta:
        model = Forms
        fields = ('name', 'email', 'fone', 'description')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name','id': 'input_color', 'class': 'input_color', 'type': "text"}),
            'email': forms.TextInput(attrs={'placeholder': 'Email', 'class': 'input_color'}),
            'fone': forms.TextInput(attrs={'placeholder': 'Phone', 'class': 'input_color'}),
            'description': forms.Textarea(attrs={'placeholder': 'Message', 'class': 'input_color'}),

            # 'firstname': forms.TextInput(attrs={'placeholder': 'Имя', 'class': 'col-md-12 form-control'}),
            # 'lastname': forms.TextInput(attrs={'placeholder': 'Фамилия', 'class': 'col-md-12 form-control'}),
            # 'midle_name': forms.TextInput(attrs={'placeholder': 'Отчество', 'class': 'col-md-12 form-control'}),
            # 'gender' : forms.ChoiceField(widget = forms.Select(attrs={'class':'hidden'}), choices = ([('MAN','Муж'), ('FEMALE','Жен')])),
            # 'birthday': forms.DateInput(format=('%d/%m/%Y'), attrs={'placeholder': 'Введите дату рождени',
            #                                                         'class': 'col-md-12 form-control datepicker'}),
            # 'email': forms.TextInput(attrs={'placeholder': 'Электронный адрес', 'class': 'col-md-12 form-control'}),
            # 'phone': forms.TextInput(attrs={'placeholder': 'Телефон', 'class': 'col-md-12 form-control'}),
            # 'photo': forms.FileInput(attrs={'type': 'file', 'class': 'col-md-12'}),
        }
