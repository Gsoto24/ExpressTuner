__author__ = 'gibransoto'
from core import models as CoreModels
from django.db.models import Q
from datetime import datetime,timedelta
from django.utils.encoding import smart_str
from django.http import HttpResponse
import csv


def scheduled_pending():
    today = datetime.now().date()
    CsvRecordQS = CoreModels.CSVRecord.objects.filter(status_code = 1).filter(Q(firstattempt = today) | Q(secondattempt = today))
    response = export_csv(CsvRecordQS)
    return response

def all_pending():
    CsvRecordQS = CoreModels.CSVRecord.objects.filter(status_code = 1)
    response = export_csv(CsvRecordQS)
    return response

def charged():
    today = datetime.now().date()
    month_ago = today - timedelta(days=30)
    CsvRecordQS = CoreModels.CSVRecord.objects.filter(status_code = 0).filter(action_date__range=[month_ago, today])
    response = export_csv(CsvRecordQS)
    return response

def failed():
    today = datetime.now().date()
    month_ago = today - timedelta(days=30)
    CsvRecordQS = CoreModels.CSVRecord.objects.filter(status_code = 2).filter(action_date__range=[month_ago, today])
    response = export_csv(CsvRecordQS)
    return response



def export_csv(queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=UploadedFile.csv'
    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8'))  # BOM (optional...Excel needs it to open UTF-8 file properly)
    writer.writerow([
        smart_str(u"email"),
        smart_str(u"productid"),
        smart_str(u"price"),
        smart_str(u"status_code"),
        smart_str(u"attempts"),
        smart_str(u"scheduled_date"),
        smart_str(u"firstattempt"),
        smart_str(u"secondattempt"),
        smart_str(u"expiration"),
        smart_str(u"last_modified_by"),
        smart_str(u"action_date"),


    ])
    for obj in queryset:

        # Transformations for human readability
        StatusCode = obj.status_code
        StatusCode_Readable = dict(obj.status)[StatusCode]
        # Transformations for human readability

        writer.writerow([
            smart_str(obj.email),
            smart_str(obj.product_id),
            smart_str(obj.price),
            smart_str(StatusCode_Readable),
            smart_str(obj.attempts),
            smart_str(obj.scheduled_date),
            smart_str(obj.firstattempt),
            smart_str(obj.secondattempt),
            smart_str(obj.expiration),
            smart_str(obj.last_modified_by),
            smart_str(obj.action_date),
        ])

    return response
export_csv.short_description = u"Export CSV"
