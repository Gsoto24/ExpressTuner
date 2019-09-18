from core import static as StaticFiles
from core import http_builder as HTTP_Builder
import requests
from bs4 import BeautifulSoup
from core import models as CoreModels
from core import authfile as AuthFiles


def OrderResultProcessor(StrInput):
    if "ORDER HAS BEEN CREATED!" in StrInput:
        return True, StrInput
    else:
        return False, StrInput

def ProcessCharge(df, username_input, password_input):

    # Static POST request variables
    POST_data = StaticFiles.StaticPostData()
    process_payment_input = POST_data['process_payment_input']
    send_email_input = POST_data['send_email_input']
    # Static POST request variables


    # Static GET request variables
    GET_Data = StaticFiles.StaticGetData()
    producttype_input = GET_Data['producttype_input']
    newsletterid_input = GET_Data['newsletterid_input']
    customerid_input = GET_Data['customerid_input']
    # Static GET request variables



    # Attempting to charge each row of input csv data
    for index, row in df.iterrows():



        email_input = row['email']
        productid_input = StaticFiles.PricePointToProductID(row['price'])
        opt_price_input = row['price']

        # CODE TO CHARGE EACH ACCOUNT -- OUTPUT -- ACCEPTED & OUTPUTTEXT
        #
        #
        # GetAttrObj = HTTP_Builder.GetRequestBuilder(email_input, producttype_input, newsletterid_input, customerid_input)
        # URL = HTTP_Builder.UrlBuilder(GetAttrObj)
        # response1 = requests.get(URL, auth=(username_input, password_input))
        # PostDataObj = HTTP_Builder.GetPostData(response1, productid_input, opt_price_input, process_payment_input, send_email_input)
        #
        # response2 = requests.post("",
        #                           data={'customer_id': PostDataObj['CustomerID_POST'],
        #                                 'adid': PostDataObj['Adid_POST'],
        #                                 'product_id': PostDataObj['ProductID_POST'],
        #                                 'opt_price': PostDataObj['Opt_Price_POST'],
        #                                 'process_payment': PostDataObj['Process_Payment_POST'],
        #                                 'send_mail': PostDataObj['Send_Email_POST'],
        #                                 'newsletter_id': PostDataObj['Newsletter_ID_POST']
        #                                 }, auth=(username_input, password_input)
        #                           )
        # soup2 = BeautifulSoup(response2.content, 'html.parser')
        # HtmlTextOutput = (StaticFiles.text_from_html(soup2))
        # Accepted, OutputText = OrderResultProcessor(HtmlTextOutput)

        # CODE TO CHARGE EACH ACCOUNT -- OUTPUT -- ACCEPTED & OUTPUTTEXT
        Accepted = False
        OutputText = "Testing -- Testing"

        # Conditional setting CSVRecord obj's status_code to 0 if charged, otherwise keeping it a 1 for attempting.
        if Accepted == True:
            RecordStatus = 0
        else:
            RecordStatus = 1
        # Conditional setting CSVRecord obj's status_code to 0 if charged, otherwise keeping it a 1 for attempting.

        try:
            print (email_input)
            CSVRecord = CoreModels.CSVRecord.objects.get(email=email_input)
            CSVRecord.product_id = productid_input
            CSVRecord.price = opt_price_input
            CSVRecord.status_text = OutputText
            CSVRecord.status_code = RecordStatus
            CSVRecord.attempts += 1
            CSVRecord  = AuthFiles.SetFingerprint(CSVRecord, username_input, 'charge')
            CSVRecord.save()
        except:
            MSGObj = {'error_msg': "This account was not scheduled. " + email_input, 'detail_error_msg': "Schedule the account to process charge attempts.", 'redirectURL': '/runexpresstuner/'}
            return MSGObj
    # Attempting to charge each row of input csv data