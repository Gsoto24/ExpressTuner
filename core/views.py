from django.shortcuts import render
from core import authfile as AuthenticationModule
from django.db import IntegrityError
from core import schedule_rolls as Scheduler
from core import process_charge as Charge
from core import download_logic as DownloadLogic
from core import maintenance as Maintenance

from django.http import HttpResponse



# Create your views here.

def upload_new_declines(request):
    Maintenance.check_expirations()
    if request.method == 'POST':

        try:
            username_input = request.POST['username']
            password_input = request.POST['password']
            try:
                csv_input = request.FILES["csv_file"]
            except:
                csv_input = None

            # Validate the User
            # UserAuthResult, AuthMsg = AuthenticationModule.AuthenticateUser(username_input, password_input)
            # if UserAuthResult == False:
            #     msg = "The Username/Password entered is not valid."
            #     Dmsg = AuthMsg
            #     return render(request, 'error.html', {'error_msg':msg, 'detail_error_msg':Dmsg, 'redirectURL':'/'})
            # # Validate the User

            # Validate CSV data
            CSVAuthResult,data = AuthenticationModule.AuthenticateCSV(csv_input, username_input, password_input, request)
            if CSVAuthResult == False:
                print ("CSV Data is not valid")
                return render(request, 'error.html', {'error_msg':data['error_msg'], 'detail_error_msg':data['detail_error_msg'], 'redirectURL':'/'})
            # Validate CSV data

            # Schedule Accounts in CSV // Save to models
            if CSVAuthResult == True:
                df = data
                Scheduler.schedule(df,username_input)
                # CreateProcessRequest(df)
                # ProcessCharge(df, username_input, password_input)
                return render(request, 'success.html')
            # Schedule Accounts in CSV // Save to models

        except IntegrityError as e:
            print ("ERROR WITH GETTING POST DATA")
            return render(request, 'error.html',
                          {'error_msg': 'Error with importing post method data.', 'detail_error_msg': e, 'redirectURL':'/'})

    return render(request, 'load_new_declines.html')

def run_expresstuner(request):
    Maintenance.check_expirations()
    if request.method == 'POST':
        try:
            username_input = request.POST['username']
            password_input = request.POST['password']
            try:
                csv_input = request.FILES["csv_file"]
            except:
                csv_input = None

            # Validate the User
            # UserAuthResult, AuthMsg = AuthenticationModule.AuthenticateUser(username_input, password_input)
            # if UserAuthResult == False:
            #     msg = "The Username/Password entered is not valid."
            #     Dmsg = AuthMsg
            #     return render(request, 'error.html', {'error_msg':msg, 'detail_error_msg':Dmsg, 'redirectURL':'/runexpresstuner/'})
            # Validate the User

            # Validate CSV data
            CSVAuthResult,data = AuthenticationModule.AuthenticateCSV(csv_input, username_input, password_input, request)
            if CSVAuthResult == False:
                print ("CSV Data is not valid")
                return render(request, 'error.html', {'error_msg':data['error_msg'], 'detail_error_msg':data['detail_error_msg'], 'redirectURL':'/runexpresstuner/'})
            # Validate CSV data

            # Schedule Accounts in CSV // Save to models
            if CSVAuthResult == True:
                df = data
                MSGObj = Charge.ProcessCharge(df, username_input, password_input)
                if MSGObj:
                    return render(request, 'error.html',MSGObj)
                else:
                    return render(request, 'success.html')
            # Schedule Accounts in CSV // Save to models

        except IntegrityError as e:
            print ("ERROR WITH GETTING POST DATA")
            return render(request, 'error.html',
                          {'error_msg': 'Error with importing post method data.', 'detail_error_msg': e, 'redirectURL':'/runexpresstuner/'})
    return render (request, 'run_expresstuner.html')

def upload_history(request):
    Maintenance.check_expirations()
    return render (request, 'upload_history.html')

def how_to_use(request):
    Maintenance.check_expirations()
    return render (request, 'how_to_use.html')


def downloads_dispatcher(request, method_name):

    if method_name == "scheduled_pending":
        return DownloadLogic.scheduled_pending()
    if method_name == 'all_pending':
        return DownloadLogic.all_pending()
    if method_name == 'charged':
        return DownloadLogic.charged()
    if method_name == 'failed':
        return DownloadLogic.failed()
    else:
        print ("error with the download dispatcher")