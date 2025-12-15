from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required


from Users.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from storeProducts.models import Basket

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect('storeProducts:main')  
    else:
        form = UserLoginForm()
    
    context = {'form': form}
    return render(request, 'Users/login.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)  
            messages.success(request, 'Вы успешно зарегистрировались!')
            return redirect('Users:profile') 
    else:
        form = UserRegisterForm()
        
    context = {'form': form}
    return render(request, 'Users/register.html', context)

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('Users:profile')
        else:
            print(form.errors)
    else:
        form = UserProfileForm(instance=request.user)
        
    baskets = Basket.objects.filter(user=request.user)
    total_sum = sum(basket.sum for basket in baskets)
    total_quantity = sum(basket.quantity for basket in baskets)
    return render(request, 'Users/profile.html', 
                  {'form': form, 
                   'title': 'Store - Профиль', 
                   'baskets':baskets, 
                   'total_sum':total_sum, 
                   'total_quantity':total_quantity}
                 )
    

def logout(request):
    auth.logout(request)
    return redirect('storeProducts:main')

def email_verification(request):
    return render(request, 'Users/email_verification.html')