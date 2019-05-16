from django.shortcuts import render

# Create your views here.
import json
import os

from .forms import RawProductForm
from .forms import SignupForm
from .forms import LoginForm
from .forms import add_fineForm

def clogin(request, *args, **kwargs):
    return render(request, "myapp/clogin.html")
def alogin(request, *args, **kwargs):
    return render(request, "myapp/alogin.html")
def signup(request, *args, **kwargs):
    return render(request, "myapp/signUp.html")

def add_fineSubmit(request, metadata=None, **kwargs):
    ## read the data from Form
    my_form = add_fineForm()
    vNumber = ''
    if request.method == "POST":
        my_form =add_fineForm(request.POST)
        if my_form.is_valid():
            print(my_form.cleaned_data)
            vNumber = request.POST.get('vehicleNumber')
            result = my_form.cleaned_data
            result = json.dumps(result)
            print(result)

            print('Vehicle Number:', vNumber)
    data = ""
    userStatus = False

    ## Read the Vehicles details from file
    fileName = os.getcwd() + "/data/vehicles/" + vNumber +".txt"
   ## fileName = os.getcwd() + "/data/signup.txt"
    print(fileName)
    exists = os.path.isfile(fileName)
    print(exists)
    if exists:
        print(exists)
    else:
        with open(fileName, "w") as f:
            vehicleData = '''
                   {"fines":[]}
               '''
            json.dump(json.loads(vehicleData), f)
        f.close()
    ##with open(fileName, "r+") as f:
    with open(fileName, "r+") as f:
        try:
            data = json.load(f)
            print("+++++++++++++++")
            print("data", data)
        except IOError: #FileNotFoundError
            print("no file found")
        except json.decoder.JSONDecodeError:
            vehicleData = '''
                   {"fines":[]}
               '''
            data = json.loads(vehicleData)
        f.close()
        print('------------------------')

        ## write the vehicle details ti vehicle file
        data['fines'].append(json.loads(result))
        print(data)
        with open(fileName, 'w') as f1:
            json.dump(data, f1)
        f1.close()
        return render(request, "myapp/add_fine.html", {"message": "Fined successful for vehicle :" + vNumber})

    f.close()

    return render(request, "myapp/add_fine.html")
## End of add_fineSubmit()

def signupSubmit (request, metadata=None, **kwargs):
    my_form = SignupForm()
    username1 = ''
    if request.method == "POST":
        my_form = SignupForm(request.POST)
        if my_form.is_valid():
            print(my_form.cleaned_data)
            username1 = request.POST.get('username')
            result = my_form.cleaned_data
            result = json.dumps(result)
            print(result)

            print('usernnnnnn', username1)
    data = ""
    userStatus = False
    with open(os.getcwd() + "/data/signup.txt", "r+") as f:
        try:
            data = json.load(f)
            print("data", data)
        except json.decoder.JSONDecodeError:
            usersData = '''
                {"users":[]}
            '''
            data = json.loads(usersData)

        count = len(data['users'])
        print(count)
        print('------------------------')
        if(count > 0):
            print(data)
            for user1 in data['users']:
                print(user1)
                print('username1', username1)
                print('userNameee', user1['username'])
                if (user1['username'] == username1):
                    context = {"errormessage": "User alredy exists."}
                    return render(request, "myapp/signup.html", context)
        else:
            print("No User found")

    f.close()

    if(userStatus):
        return render(request, "myapp/signup.html")

    data['users'].append(json.loads(result))
    with open(os.getcwd() + "/data/signup.txt", 'w') as f1:
        json.dump(data, f1)

   ## f1.write(data)
    f1.close()

    return render(request, "myapp/productresult.html")
## End of signupSubmit()

##Customer login request
def loginSubmit (request, metadata=None, **kwargs):
    my_form = LoginForm()
    username = ""
    password = ""
    if request.method == "POST":
        my_form = LoginForm(request.POST)
        print(my_form.is_valid())
        if my_form.is_valid():
            print(my_form.cleaned_data)
            username = request.POST.get('username')
            password = request.POST.get('password')
    print(username)
    print(password)
    data = ""
    with open(os.getcwd() + "/data/signup.txt", "r") as f:
        data = json.load(f)
    f.close()

    loginStatus = False
    if(data == ""):
        print("No User found.")
    else:
        print(data)
        for userdata in data['users']:
            if(userdata['username'] == username and userdata['password'] == password):
                print("Login is Success")
                loginStatus = True
    if (loginStatus):
        return render(request, "myapp/chome.html")
    else:
        context = {"message": "Invalid Username or Password."}
        return render(request, "myapp/clogin.html", context)
## End of loginSubmit()

##Admin login request
def aloginSubmit(request, metadata=None, **kwargs):
    my_form = LoginForm()
    username = ""
    password = ""
    if request.method == "POST":
        my_form = LoginForm(request.POST)
        print(my_form.is_valid())
        if my_form.is_valid():
            print(my_form.cleaned_data)
            username = request.POST.get('username')
            password = request.POST.get('password')
    print(username)
    print(password)
    data = ""
    with open(os.getcwd() + "/data/asignup.txt", "r") as f:
        data = json.load(f)
    f.close()

    loginStatus = False
    if (data == ""):
        print("No User found.")
    else:
        print(data)
        for userdata in data['users']:
            if (userdata['username'] == username and userdata['password'] == password):
                print("Login is Success")
                loginStatus = True
    if (loginStatus):
        return render(request, "myapp/ahome.html")
    else:
        context = {"message": "Invalid Username or Password."}
        return render(request, "myapp/alogin.html", context)

    return render(request, "myapp/ahome.html")
## End of aloginSubmit()

def ahome(request, *args, **kwargs):
    return render(request, "myapp/ahome.html")
def chome(request, *args, **kwargs):
    return render(request, "myapp/chome.html")

def add_fine(request, *args, **kwargs):
    return render(request, "myapp/add_fine.html")

def payment(request, *args, **kwargs):
    return render(request, "myapp/payment.html")

def fine_look(request, *args, **kwargs):
    return render(request, "myapp/fine_look.html")

def calc_fine(request, *args, **kwargs):
    return render(request, "myapp/calc_fine.html")
