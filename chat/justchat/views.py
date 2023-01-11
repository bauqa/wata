# chat/views.py
from django.views.generic import CreateView,ListView
from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from .forms import SignUpForm,BookForm
from .models import Book
from django.contrib.auth import authenticate,login

class Index(ListView):
    template_name = "justchat/index.html"
    model = Book
    context_object_name = "books"
def beb(request):
    if request.user.is_authenticated==False:
        
        return redirect("/usersa/login")
    
    return HttpResponse("Hello")
class CreatePost(CreateView):
    template_name = "justchat/newbook.html"
    success_url = '/'
    form_class = BookForm
    def form_valid(self,form):
        form.instance.userbook = self.request.user
        return super().form_valid(form)


def signup(request):
    if request.method == 'POST':

        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  
            # load the profile instance created by the signal
            user.save()
            raw_password = form.cleaned_data.get('password1')

            # login user after signing up
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)

            # redirect user to home page
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'justchat/signup.html', {'form': form})
