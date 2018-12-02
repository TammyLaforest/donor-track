from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site

from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_text, force_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

from accounts.forms import SignUpForm
from accounts.tokens import account_activation_token

from django.views.generic import CreateView

class signup_view(CreateView):
    template_name = 'signup.html'

def SignUp(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get()
            raw_password = form.cleaned_data.get()
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

#
#
# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             # user = form.save()
#             # user.refresh_from_db()  # load the profile instance created by the signal
#             # user.profile.birth_date = form.cleaned_data.get('birth_date')
#             user.is_active = False
#             user.save()
#             # raw_password = form.cleaned_data.get('password1')
#             # user = authenticate(username=user.username, password=raw_password)
#             current_site = get_current_site(request)
#             subject = 'Activate Your EasyDonor Account'
#             message = render_to_string('account_activation_email.html', {
#                 'user': user,
#                 'domain': current_site.domain,
#                 'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#                 'token': account_activation_token.make_token(user),
#             })
#             user.email_user(subject, message)
#             return redirect('account_activation_sent')
#             # login(request, user)
#             # return redirect('home')
#     else:
#         form = SignUpForm()
#     return render(request, 'signup.html', {'form': form})
#

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('home')
    else:
        return render(request, 'account_activation_invalid.html')
