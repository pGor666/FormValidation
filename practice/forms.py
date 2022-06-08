from django import forms
from . models import GENRE_CHOICES, CD

class ExchangeForm(forms.Form):
    name = forms.CharField(max_length=100, label='Название')
    email = forms.EmailField(label='Почта')
    title = forms.CharField(max_length=100, label='Заголовок')
    artist = forms.CharField(max_length=40, label='Артист')
    genre = forms.ChoiceField(choices=GENRE_CHOICES, label='Жанр')
    price = forms.DecimalField(max_digits=5, decimal_places=2, label='Цена', required=False)
    comment = forms.CharField(widget=forms.Textarea, label='Комментарий', required=False)
    
    def clean_artist(self):
        artist_name = self.cleaned_data['artist']
        latest=CD.objects.filter(artist__icontains=artist_name.lower())
        if not latest.exists():
            raise forms.ValidationError("Артиста нет в базе!")       
        return artist_name
