from django import forms
from .models import SCHOOL_CLASS, PIZZA_SIZES, Toppings


class StudentSearchForm(forms.Form):
    last_name = forms.CharField(label='Nazwisko ucznia', max_length=64)


class StudentForm(forms.Form):
    first_name = forms.CharField(label='Imię', max_length=64)
    last_name = forms.CharField(label='Nazwisko', max_length=64)
    school_class = forms.ChoiceField(label='Klasa', choices=SCHOOL_CLASS)
    year_of_birth = forms.IntegerField(label='Data urodzenia')


class PizzaToppingsForm(forms.Form):
    size = forms.ChoiceField(label='Rozmiar Twojej pizzy', choices=PIZZA_SIZES)
    toppings = forms.ModelMultipleChoiceField(
        label='Dodatki',
        queryset=Toppings.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )


class PresenceListForm(forms.Form):
    student = forms.IntegerField(label='Uczeń')
    day = forms.DateField(label='Dzień', widget=forms.HiddenInput)
    present = forms.BooleanField(label='Obecność', widget=forms.CheckboxInput, required=False)


COLORS = (
    ("BLACK", "BLACK"),
    ("WHITE", "WHITE"),
    ("RED", "RED"),
    ("YELLOW", "YELLOW"),
    ("BLUE", "BLUE")
)


class BackgroundColorForm(forms.Form):
    color = forms.ChoiceField(label='Wybierz kolor', choices=COLORS)
