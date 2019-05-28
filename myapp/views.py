from django.shortcuts import render

# Create your views here.
import json
import os

from .forms import SignupForm, calc_fineForm, look_fineForm
from .forms import LoginForm
from .forms import add_fineForm

def clogin(request, *args, **kwargs):
    return render(request, "myapp/clogin.html")

def alogin(request, *args, **kwargs):
    return render(request, "myapp/alogin.html")

def signup(request, *args, **kwargs):
    return render(request, "myapp/signUp.html")

def look_fineSubmit (request, *args, **kwargs):
    my_form = look_fineForm()
    vNumber = ''
    print ('1111111111111111')
    if request.method == "POST":
        my_form = look_fineForm(request.POST)
        print('22222222222222')
        print(my_form.is_valid())
        if my_form.is_valid():
            print ('3333333333333')
            vNumber = request.POST.get('vehicleNumber')
            result = my_form.cleaned_data
            result = json.dumps(result)
            resultsJson = json.loads(result)
            vehicleFileName = os.path.join('data/vehicles', '{}.json'.format(vNumber))
            vehicleFileName = vehicleFileName.replace("\\", "/")
            data = ''

            exists = os.path.isfile(vehicleFileName)

            if exists:
                print(vehicleFileName, exists)
                return render(request, "myapp/fine_look.html", {"message": "There is a fine present "})
            else:
                return render(request, "myapp/fine_look.html", {"message": "There is No Fine present."})
        else:
            return render(request, "myapp/fine_look.html", {"message": "Enter Vehicle Number."})


def calc_fineSubmit(request, metadata=None, **kwargs):
    my_form = calc_fineForm()
    vNumber = ''

    if request.method == "POST":
        my_form = calc_fineForm(request.POST)
        print(my_form.is_valid())
        if my_form.is_valid():
            vNumber = request.POST.get('vehicleNumber')
            result = my_form.cleaned_data
            result = json.dumps(result)
            resultsJson = json.loads(result)
            ## Read Vehicle fines information
            vehicleFileName = os.path.join('data/vehicles', '{}.json'.format(vNumber))
            vehicleFileName = vehicleFileName.replace("\\", "/")
            data = ''

            exists = os.path.isfile(vehicleFileName)

            if exists:
                print(vehicleFileName, exists)
                os.remove(vehicleFileName)
                return render(request, "myapp/payment.html")
            else:
                return render(request, "myapp/calc_fine.html", {"message": "No Vehicle present."})
        else:
            return render(request, "myapp/calc_fine.html", {"message": "Enter Vehicle Number."})

def add_fineSubmit(request, metadata=None, **kwargs):
    ## read the data from Form
    my_form = add_fineForm()
    vNumber = ''
    if request.method == "POST":
        my_form = add_fineForm(request.POST)
        if my_form.is_valid():
            vNumber = request.POST.get('vehicleNumber')
            result = my_form.cleaned_data
            result = json.dumps(result)

            resultsJson = json.loads(result)
            del resultsJson['vehicleNumber']

    ##  Write Fine information to Vehicle fine file which is indexed
    data = ""
    vehicleFileName = os.path.join('data/vehicles', '{}.json'.format(vNumber))
    vehicleFileName = vehicleFileName.replace("\\", "/")

    ## Read the Vehicles details from file
    finesData = '''
                   {"fines":[]}
               '''
    ##Create Vehicle fines file if not exists
    createFile(vehicleFileName, finesData)

    ## Read Vehicle fines information
    with open(vehicleFileName, "r+") as f:
        try:
            data = json.load(f)
        except IOError: #FileNotFoundError
            print(vehicleFileName, " file not found.")
        except json.decoder.JSONDecodeError:
            data = json.loads(finesData)
        f.close()

    ## write the vehicle fine details to vehicle fine file in Json format
    data['fines'].append(resultsJson)
    with open(vehicleFileName, 'w') as f1:
        json.dump(data, f1, indent = 2)
        f1.close()

    ##====================Index file manipulations ===============
    vehicleIndexFileName = os.path.join('data/index-files', 'vehicle-index.json')

    vehiclesEmptyData = '''
               {"vehicles":[]}
           '''
    createFile(vehicleIndexFileName, vehiclesEmptyData)

    vehiclesData = ''
    with open(vehicleIndexFileName, "r+") as f10:
        try:
            vehiclesData = json.load(f10)
        except IOError:  # FileNotFoundError
            print(vehicleIndexFileName, " file not found")
        except json.decoder.JSONDecodeError:
            vehiclesData = json.loads(vehiclesEmptyData)
        f10.close()

    ## Find Vehicle indexed in Index file
    vehicleStatus = False
    for vehicle in vehiclesData['vehicles']:
        if (vehicle['vehicleNumber'] == vNumber):
            vehicleStatus = True

    ## Index the Vehicle fines file in Index file
    if(vehicleStatus == False):
        with open(vehicleIndexFileName, 'w',  newline="") as indexfile:
            vdata = {}
            vdata['indexFile'] = vehicleFileName
            vdata['vehicleNumber'] = vNumber
            vehiclesData['vehicles'].append(vdata)
            json.dump(vehiclesData, indexfile, indent = 2)
            indexfile.close()
    ##====================Index file manupulations ends ===============

    return render(request, "myapp/add_fine.html", {"message": "Fined successful for vehicle :" + vNumber})

## End of add_fineSubmit()

## Submit the Signup request
def signupSubmit (request, metadata=None, **kwargs):
    my_form = SignupForm()
    userName = ''
    if request.method == "POST":
        my_form = SignupForm(request.POST)
        if my_form.is_valid():
            userName = request.POST.get('username')
            result = my_form.cleaned_data
            result = json.dumps(result)

    data = ""
    userStatus = False
    with open(os.getcwd() + "/data/signup.json", "r+") as f:
        try:
            data = json.load(f)
        except json.decoder.JSONDecodeError:
            usersData = '''
                {"users":[]}
            '''
            data = json.loads(usersData)

        count = len(data['users'])
        if(count > 0):
            for user1 in data['users']:
                if (user1['username'] == userName):
                    context = {"errormessage": "User alredy exists."}
                    return render(request, "myapp/signup.html", context)
        else:
            print("No User found")

    f.close()

    if(userStatus):
        return render(request, "myapp/signup.html")

    data['users'].append(json.loads(result))
    with open(os.getcwd() + "/data/signup.json", 'w') as f1:
        json.dump(data, f1, indent = 2)

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
            username = request.POST.get('username')
            password = request.POST.get('password')

    data = ""
    with open(os.getcwd() + "/data/signup.json", "r") as f:
        data = json.load(f)
    f.close()

    loginStatus = False
    if(data == ""):
        print("No User found.")
    else:
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

        if my_form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

    data = ""
    with open(os.getcwd() + "/data/asignup.json", "r") as f:
        data = json.load(f)
    f.close()

    loginStatus = False
    if (data == ""):
        print("No User found.")
    else:
        for userdata in data['users']:
            if (userdata['username'] == username and userdata['password'] == password):
                loginStatus = True

    if (loginStatus):
        ##request.session['username'] = username
        request.session['role'] = 'admin'
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
    role = ''

    if(request.session.has_key('role')):
        role = request.session['role']

    if(role == 'admin'):
        return render(request, "myapp/add_fine.html")
    else:
        return render(request, "myapp/alogin.html")

def payment(request, *args, **kwargs):
    return render(request, "myapp/payment.html")

def fine_look(request, *args, **kwargs):
    return render(request, "myapp/fine_look.html")

def calc_fine(request, *args, **kwargs):
    return render(request, "myapp/calc_fine.html")

##Create the file if not exists
def createFile(fileName, emptydata):
    exists = os.path.isfile(fileName)

    if exists:
        print(fileName, exists)
    else:
        with open(fileName, "a") as f:
            json.dump(json.loads(emptydata), f, indent = 2)
        f.close()