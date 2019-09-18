__author__ = 'gibransoto'
from core import static as StaticFiles
from core import models as CoreModels
from core import authfile as AuthFiles

def schedule(df, username_input):
    # Returns 'Attempt Dates' and an 'expiration' date on account
    First_AttemptDate, Second_AttemptDate, ExpirationDate, Date_Loaded = StaticFiles.GetPRObjExpiration()
    # Returns 'Attempt Dates' and an 'expiration' date on account

    for index, row in df.iterrows():
        email_input = row['email']
        productid_input = StaticFiles.PricePointToProductID(row['price'])
        if productid_input == False:
            continue
        opt_price_input = row['price']

        # Tries to find the Account in the system and modify it before creating a new one
        try:
            CSVRecord = CoreModels.CSVRecord.objects.get(email=email_input)
            CSVRecord.product_id = productid_input
            CSVRecord.price = opt_price_input

            # Simply skips the account as its already being attempted
            if CSVRecord.status_code == 1:
                print ("error " + email_input+ " has already been loaded and is currently on attempting status.")
            # Simply skips the account as its already being attempted

            # Modifies current CSVRecord obj
            else:
                CSVRecord.status_code = 1
                CSVRecord.attempts = 0
                CSVRecord.scheduled_date = Date_Loaded
                CSVRecord.firstattempt = First_AttemptDate
                CSVRecord.secondattempt = Second_AttemptDate
                CSVRecord.expiration = ExpirationDate
                CSVRecord = AuthFiles.SetFingerprint(CSVRecord, username_input, 'schedule')
                CSVRecord.save()
            # Modifies current CSVRecord obj

        # Tries to find the Account in the system and modify it before creating a new one


        # Did not find an Account so Creates a new one
        except:
            CSVRecord = CoreModels.CSVRecord(email=email_input,
                                             product_id=productid_input,
                                             price=opt_price_input,
                                             status_code=1,
                                             scheduled_date=Date_Loaded,
                                             firstattempt = First_AttemptDate,
                                             secondattempt = Second_AttemptDate,
                                             expiration=ExpirationDate,
                                             )
            CSVRecord = AuthFiles.SetFingerprint(CSVRecord, username_input, 'schedule')
            CSVRecord.save()
        # Did not find an Account so Creates a new one