__author__ = 'gibransoto'
from django.shortcuts import render
import pandas as pd
import pandas_validator as pv
import requests
from core import static as StaticFiles
from bs4 import BeautifulSoup
from bs4.element import Comment
from core import http_builder as HTTP_Builder

from django.utils import timezone
from datetime import datetime, timedelta


class SampleDataFrameValidator(pv.DataFrameValidator):
    column_num = 2

def AuthenticateCSV(csv_input,username_input, password_input,request):
    try:

        # Validate File Type
        if not csv_input.name.endswith('.csv'):
            print("This is not a csv file..error")
            data = {'error_msg': "There was a problem with the file type entered.", 'detail_error_msg': "The file must be a csv."}
            return False, data
        # Validate File Type

        # Validate File Size: if file is too large, return
        if csv_input.multiple_chunks():
            print("error input file is too large!")
            data = {'error_msg': "There was a problem with the file type entered.",
                    'detail_error_msg': "The file entered is too large, try processing smaller batches."}
            return False, data
        # Validate File Size: if file is too large, return

        # Validate CSV format
        validator = SampleDataFrameValidator()
        df = pd.read_csv(csv_input)
        if validator.is_valid(df) == False:
            print("error csv has the wrong amount of columns!")
            data = {'error_msg': "There was a problem with the file type entered.",
                                                  'detail_error_msg': "The csv is not formatted properly, check insturctions on how to properly format."}
            return False, data
        # Validate CSV format


        # Static GET request variables
        GET_Data = StaticFiles.StaticGetData()
        producttype_input = GET_Data['producttype_input']
        newsletterid_input = GET_Data['newsletterid_input']
        customerid_input = GET_Data['customerid_input']
        # Static GET request variables

        # Validation of each row in the CSV
        for index, row in df.iterrows():

            # Validate account for "already signed up' or 'if account exists in ecomm'
            email_input = row['email']
            # GetAttrObj = HTTP_Builder.GetRequestBuilder(email_input, producttype_input, newsletterid_input,
            #                                             customerid_input)
            # URL = HTTP_Builder.UrlBuilder(GetAttrObj)

        #     # Try/Except for connection http connection issues
        #     try:
        #         response1 = requests.get(URL, auth=(username_input, password_input))
        #     except:
        #         data = {'error_msg': "There was a network connection error.",
        #                                               'detail_error_msg': "Was not able to connect to: " + URL}
        #         return False, data
        #     # Try/Except for connection http connection issues
        #
        #     SoupOutput = BeautifulSoup(response1.content, 'html.parser')
        #     HtmlTextOutput = (StaticFiles.text_from_html(SoupOutput))
        #     if "Customer has one or more active subscriptions" in HtmlTextOutput:
        #         print("Row fails validation")
        #         data = {'error_msg': "There was a problem validating your file.",
        #                                               'detail_error_msg': str(email_input) + " has already signed up!"}
        #         return False, data
        #     if "CHOSE AVAILABLE PRODUCT CODE:" not in HtmlTextOutput:
        #         print("Row fails validation")
        #         data = {'error_msg': "There was a problem validating your file.",
        #                                               'detail_error_msg': "Check your input file. " +email_input + " may not be a valid user."}
        #         return False, data
        #
        #     # Validate if price point matches an order code
        #     try:
        #         productid_input = StaticFiles.PricePointToProductID(row['price'])
        #         if productid_input == False:
        #             data = {'error_msg': "There was an issue with an account entered.",
        #                                                   'detail_error_msg': "The price point entered did not match an order."}
        #             return False, data
        #     except:
        #         data = {'error_msg': "There was an issue with an account entered.",
        #                                               'detail_error_msg': "The price point entered did not match an order."}
        #         return False, data
        #     # Validate if price point matches an order code
        #
        #     print (URL, HtmlTextOutput)
        #     print(email_input +" email was validated!")
        #     # Validate account for "already signed up' or 'if account exists in ecomm'
        #
        # print ("Every Row was validated!")
        return True, df

    except:
        print("Failue in Authenticating CSV file")
        data = {'error_msg': "There was a problem validating your file.",
                                              'detail_error_msg': "Check your input file format. Ran except."}
        return False, data
        # Validation of each row in the CSV


def AuthenticateUser(Auth_user, Auth_pass):

    # Try/Except for connection http connection issues
    try:
        response1 = requests.get('', auth=(Auth_user, Auth_pass))
    except:
        return False, 'Was not able to connect to '
    # Try/Except for connection http connection issues

    SoupOutput = BeautifulSoup(response1.content, 'html.parser')
    HtmlTextOutput = (StaticFiles.text_from_html(SoupOutput))
    if "Access denied!" in HtmlTextOutput:
        print("Not logged in")
        return False, HtmlTextOutput
    if "Logged in as:" in HtmlTextOutput:
        print("logged in")
        return True, HtmlTextOutput
    else:
        print("Error with AuthenticateUser")
        return False, HtmlTextOutput


# This function takes in a CSVRecord and attaches a 'fingerprint' identifying the last person to modify the obj and datestamp
def SetFingerprint(CSVRecord, username_input, type):
    today = timezone.now().date()

    if type == 'expiration':
        CSVRecord.action_date = today
        CSVRecord.last_modified_by = 'ExpressTuner'
        return CSVRecord

    else:
        CSVRecord.action_date = today
        CSVRecord.last_modified_by = username_input
        return CSVRecord
# This function takes in a CSVRecord and attaches a 'fingerprint' identifying the last person to modify the obj and datestamp

