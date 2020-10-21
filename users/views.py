from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.shortcuts import redirect
from .models import Transactions,Expenses
from .forms import CustomUserCreationForm,TransactionForm

# Create your views here.
def logout_request(request):
    if request.method=="POST":
        logout(request)
        messages.info(request, "Logged out successfully!")
        return redirect("/users/login")

def register_request(request):
    return render(request=request,template_name="register.html")

def home(request):
    amounts=[ i.transaction_amount for i in request.user.transactions_set.all() ]
    total=sum(amounts)
    return render(request=request,
    template_name="home.html",
    context={
        "total":total,
        "transaction_list":request.user.transactions_set.all(),
        "College":"Christ University",
        "expenses":Expenses.objects.all()
    })

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user=authenticate(username=username,password=raw_password)
            messages.info(request, f"You are now logged in as {username}")
            return redirect('/users/login')
        else:
            print(form.errors)
            print("innalud form")
            messages.error(request, "Invalid username or password.")
    form=CustomUserCreationForm()
    return render(request = request,
            template_name = "register.html",
            context={"form":form})



def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/users/home')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "index.html",
                    context={"form":form})



def test(request):
    return render(request=request,template_name="index.html")


def submit_transaction(request):
    if request.method=='POST':
        data=request.POST.copy()
        data["transaction_amount"]=str(int(data["transaction_amount"])+300)
        print(data)
        data["user"]=request.user
        form=TransactionForm(data=data)
        if form.is_valid():
            form.save()
            return redirect('/users/home')
        else:
            print(form.errors)

def delete_transac(request):
    if request.method=='POST':
        data=request.POST.copy()
        transac_obj=Transactions.objects.get(transaction_field=data["transaction_id"])
        transac_obj.delete()
        return redirect("/users/home")


def update_transac(request):
    if request.method=='POST':
        data=request.POST.copy()
        try:
            transac_obj=Transactions.objects.get(transaction_field=data["transaction_id"])
            transac_obj.transaction_desc=data["transaction_name"]
            transac_obj.save()
            return redirect("/users/home")
        except Transactions.DoesNotExist:
            return redirect("/users/home")
