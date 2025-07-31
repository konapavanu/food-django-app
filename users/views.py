from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import ProfileUpdateForm
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def register(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Welcome {username},you Successfully logged in')
            return redirect('login')    
    else:
        form=RegisterForm()
    context={'form':form}
    return render(request,'users/register.html',context)

# @login_required
# def profile(request):
#     return render(request,'users/profile.html')



@login_required
def profile_view(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'users/profile.html', {'form': form})
 

# users/views.py
# from django.contrib.auth.views import LogoutView

# class CustomLogoutView(LogoutView):
#     def GET(self, request, *args, **kwargs):
#         messages.success(request, "You have been logged out successfully.")
#         return self.post(request, *args, **kwargs)


