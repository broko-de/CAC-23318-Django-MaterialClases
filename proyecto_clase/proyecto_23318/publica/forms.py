from django import forms

class ContactoForm(forms.Form):
    TIPO_CONSULTA = (
        ('','-Seleccione-'),
        (1,'Inscripciones'),
        (2,'Soporte Aula Virtual'),
        (3,'Ser docente'),
    )

    nombre = forms.CharField(label='Nombre',max_length=4)
    email = forms.EmailField(label='Email',max_length=200,required=False)
    asunto = forms.CharField(label='Asunto')
    mensaje = forms.CharField(label='Mensaje')
    tipo_consulta = forms.ChoiceField(
        label='Tipo de consulta',
        choices=TIPO_CONSULTA
    )
    suscripcion = forms.BooleanField(
        label='Deseo suscribirme a las noticias',
        required=False
    )