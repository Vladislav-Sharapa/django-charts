from datetime import datetime

def get_week_number(date):
    date_obj = datetime.strptime(date, "%m/%d/%Y")
    week_number = date_obj.isocalendar()[1]
    return week_number