from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from loginapp.forms import SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q

# Create your views here.
def home(request):
    return render(request,'loginapp/home.html')

def signup(request):
    form = SignUpForm()
    if request.method == 'POST':
        try:
            user_exist = User.objects.get(Q(username = request.POST['username']) | Q(email = request.POST['email']))
            if user_exist:
                return HttpResponse("<center><h1>Either Username or email already exist !</h1></center>")
        except:
            form = SignUpForm(request.POST)
            if form.is_valid():
                user = form.save()
                user.set_password(user.password)
                user.save()
                return HttpResponseRedirect('/accounts/login')
    return render(request,'registration/signup.html',{'form':form})

@login_required
def totalUser(request):
    user_qs = User.objects.all()
    user_detail = []
    user_count = 0
    if user_qs:
        for obj in user_qs:
            user_count += 1
            user = dict()
            user['id'] = obj.id
            user['username'] = obj.username
            user['first_name'] = obj.first_name
            user['last_name'] = obj.last_name
            user['email'] = obj.email
            user_detail.append(user)
        return render(request,'loginapp/total_users.html',{'user_detail':user_detail,'user_count':user_count})

def deleteUser(request):
    if request.method=='POST':
        user_id = request.POST['user_id']
        print('user_id',user_id)
        if user_id:
            obj = User.objects.get(id=user_id)
            obj.delete()
    return redirect('/total_users.html')


def logout(request):
    return render(request,'registration/logout.html')
