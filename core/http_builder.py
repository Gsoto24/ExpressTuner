__author__ = 'gibransoto'
from bs4 import BeautifulSoup


def CleanGetEmail(DirtyEmail):
    CleanEmail = DirtyEmail.replace("@", "%40")

    return CleanEmail
def GetRequestBuilder(email_input,producttype_input,newsletterid_input,customerid_input):
    GetAttrObj = dict(
        ProductType = producttype_input,
        NewsletterID = newsletterid_input,
        CustomerID=customerid_input,
        CleanEmail = CleanGetEmail(email_input)
    )
    return GetAttrObj

# def UrlBuilder(GetAttrObj):
    # UrlRoot = "https://charge-tuners.zacks.com/administration/charge/step2.php?"
    # ProductType = "product_type="+ GetAttrObj['ProductType']
    # Newsletter_id = "newsletter_id=" + str(GetAttrObj['NewsletterID'])
    # Customer_id = "customer_id="
    # Email = 'email=' + GetAttrObj['CleanEmail']
    #
    # URL = UrlRoot + '&' + ProductType +'&' + Newsletter_id + '&' + Customer_id + '&' + Email
    # return URL

def GetPostData(response, productid_input, opt_price_input, process_payment_input,send_email_input):
    soup = BeautifulSoup(response.content,'html.parser')

    PostDataObj = dict(
        CustomerID_POST = soup.find(attrs={"name": "customer_id"}).get('value'),
        Adid_POST = soup.find(attrs={"name": "adid"}).get('value'),

        # This is dictated by code type on excel input
        ProductID_POST = productid_input,
        Opt_Price_POST = opt_price_input,
        # This is dictated by code type on excel input

        # soup.find(attrs={"name": "process_payment"}).get('value')
        Process_Payment_POST = process_payment_input,
        Send_Email_POST = send_email_input,
        Newsletter_ID_POST = soup.find(attrs={"name": "newsletter_id"}).get('value')
        )
    return PostDataObj