from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ExchangeForm
from django.shortcuts import redirect

def send_msg(email, name, title, artist, genre, price, comment):
    subject = f"Обмен {artist}-{title}"
    body = f"""Предложение на обмен диска от {name} ({email})

    Название: {title}
    Исполнитель: {artist}
    Жанр: {genre}
    Стоимость: {price}
    Комментарий: {comment}

    """
    send_mail(
        subject, body, email, ["admin@rockenrolla.net", ],
    )


def index(request):
    if request.method == 'POST':
        form = ExchangeForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            title = form.cleaned_data['title']
            artist = form.cleaned_data['artist']
            genre = form.cleaned_data['genre']
            price = form.cleaned_data['price']
            comment = form.cleaned_data['comment']
            #form.save()
            return redirect('/thank-you/')
        else:
            return render(request, 'index.html', {'form': form})
    else:
        form = ExchangeForm()
        return render(request, 'index.html', {'form': form})


