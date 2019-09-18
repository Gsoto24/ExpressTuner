__author__ = 'gibransoto'
from django.utils import timezone
from datetime import datetime, timedelta
from bs4.element import Comment

# Static POST request variables
def StaticPostData():
    POST_Static = dict(process_payment_input=1,
                       send_email_input=0)
    return  POST_Static

# Static GET request variables
def StaticGetData():
    GET_Static = dict(producttype_input='newsletter',
                      newsletterid_input=197,
                      customerid_input='', )
    return GET_Static

def GetPRObjExpiration():
    FirstAttempt = 0
    SeccondAttempt = 3
    SetExpiration = 7

    today = datetime.now().date()
    First_Attempt = today + timedelta(days=FirstAttempt)
    Second_Attempt = today + timedelta(days=SeccondAttempt)
    Expiration = today + timedelta(days=SetExpiration)
    Date_Loaded = today

    return First_Attempt, Second_Attempt, Expiration, Date_Loaded

def PricePointToProductID(Input):

    Int_input = int(Input)
    if Int_input == 29:
        return 1650
    if Int_input == 249:
        return 1578
    if Int_input == 398:
        return 1579
    if Int_input == 498:
        return 1751
    else:
        return False


# Stackoverflow Soup Text Code
def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True

def text_from_html(soup):
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)
    return u"-".join(t.strip() for t in visible_texts)
# Stackoverflow Soup Text Code