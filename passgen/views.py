import string, random
from django.shortcuts import render
from .forms import PasswordForm

def password_generator(request):
    password = ''
    if request.method == 'POST':
        form = PasswordForm(request.POST)
        if form.is_valid():
            length = form.cleaned_data['length']
            chars = ''
            if form.cleaned_data['use_letters']:
                chars += string.ascii_letters
            if form.cleaned_data['use_digits']:
                chars += string.digits
            if form.cleaned_data['use_punctuation']:
                chars += string.punctuation

            if chars:
                password = ''.join(random.choice(chars) for _ in range(length))
            else:
                form.add_error(None, "최소 하나 이상의 문자 유형을 선택하세요.")
    else:
        form = PasswordForm()

    return render(request, 'passgen/password_generator.html', {
        'form': form,
        'password': password,
    })
