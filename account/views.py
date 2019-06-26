from django.views import View
from django.shortcuts import render
from django.contrib.sites.shortcuts import get_current_site


from django.contrib.auth import login, update_session_auth_hash, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text



from .forms import UserRegistrationForm
from .tokens import account_activation_token
from mysite.utils import BaseEmailSender

class RegistrationEmailSender(BaseEmailSender):
    subject = "BNK Support: Account Activation"
    template_path = 'registration/activation_email.html'
    def get_context(self):
        author = self.kwargs['author']
        current_site = self.kwargs['current_site']
        uid = urlsafe_base64_encode(force_bytes(author.pk))
        token = account_activation_token.make_token(author)
        return {
            'user': author,
            'domain':current_site,
            'uid':uid,
            'token':token,
        }
class Activate(View):
    template_path = "registration/register_confirmed.html"
    def get(self, request, uidb64, token):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and account_activation_token.check_token(user, token):
            # activate user and login:
            user.is_active = True
            user.save()
            return render(request, self.template_path, {'new_user': user,'validlink':True})

        else:
            return render(request, self.template_path, {'new_user': user, 'validlink':False})
class Register(View):
    register_template_path = "registration/register.html"
    register_done_template_path = 'registration/register_done.html'
    form_class = UserRegistrationForm
    def get(self, request):
        return render(request, self.register_template_path, {'form':self.form_class()})
    def post(self, request):
        user_form = self.form_class(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.is_active = False
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.username = user_form.cleaned_data.get('email')
            new_user.save()
            email_sender = RegistrationEmailSender(
                                receiver_list=[new_user.email],
                                to_compliance = False,
                                author = new_user,
                                current_site = get_current_site(request)
                            )
            email_sender.async_send()
            return render(request, self.register_done_template_path, {'new_user':new_user})
        else:
            return render(request, self.register_template_path, {'form':user_form})
