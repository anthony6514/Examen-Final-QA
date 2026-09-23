from django.forms import ModelForm, ValidationError
from .models import Entrega


class EntregaForm(ModelForm):
    class Meta:
        model = Entrega
        fields = ['codigo', 'camion', 'destino', 'fecha', 'estado']
        error_messages = {
            'codigo': {
                'required': 'El código es obligatorio.',
                'unique': 'Ya existe una entrega con ese código.',
                'max_length': 'El código no puede tener más de 50 caracteres.',
            },
            'camion': {
                'required': 'Ingresa la placa del camión.',
                'max_length': 'La placa no puede tener más de 20 caracteres.',
            },
            'destino': {
                'required': 'El destino es obligatorio.',
                'max_length': 'El destino no puede tener más de 100 caracteres.',
            },
            'fecha': {
                'required': 'La fecha es obligatoria.',
                'invalid': 'Ingresa una fecha válida (formato: YYYY-MM-DD).',
            },
            'estado': {
                'required': 'Selecciona un estado.',
                'invalid_choice': 'Estado no válido.',
            },
        }

    def clean_codigo(self):
        codigo = self.cleaned_data.get('codigo', '')
        if not codigo:
            raise ValidationError('El código es obligatorio.')
        if codigo[0].isdigit():
            raise ValidationError('El código no puede comenzar con un número.')
        return codigo

    def clean_camion(self):
        camion = self.cleaned_data.get('camion', '')
        if not camion:
            raise ValidationError('Ingresa la placa del camión.')
        return camion.upper()

    def clean_fecha(self):
        from datetime import date
        fecha = self.cleaned_data.get('fecha')
        if not fecha:
            raise ValidationError('La fecha es obligatoria.')
        if fecha < date.today():
            raise ValidationError('La fecha no puede ser anterior a hoy.')
        return fecha
