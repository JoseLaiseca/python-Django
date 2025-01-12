from django import forms


class FormularioRemera(forms.Form):
    marca = forms.CharField(label="Marca", max_length=128)
    TALLES = (
        (1, "XS"),
        (2, "S"),
        (3, "M"),
        (4, "L"),
        (5, "XL"),
        (6, "XXL")
    )
    talle = forms.ChoiceField(label="Talle", choices=TALLES)
    color = forms.CharField(label="Color", max_length=128)
    lisa = forms.BooleanField(label="Lisa", required=False)
    GENEROS = (
        (1, "Hombre"),
        (2, "Mujer"),
        (3, "Unisex")
    )
    genero = forms.ChoiceField(label="Género", choices=GENEROS)
