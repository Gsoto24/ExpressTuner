from core import models as CoreModels
from core import authfile as AuthFiles
from datetime import datetime

# This code is ran on each page load, quite expensive could be ran on as a cron task

# Checks all attemtpting status accounts for expirations
def check_expirations():
    AttemptingStatusQS  = CoreModels.CSVRecord.objects.filter(status_code = 1)
    today = datetime.now().date()
    for Obj in AttemptingStatusQS:

        if Obj.expiration <= today:
            Obj.status_code = 2
            Obj = AuthFiles.SetFingerprint(Obj, 'computer', 'expiration')
            Obj.status_text = "--Expired--"
            Obj.save()
# Checks all attemtpting status accounts for expirations
