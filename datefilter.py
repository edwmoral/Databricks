import csv
from datetime import datetime


def check_file(_start_date, _end_date):
    results = []
    with open( 'MOCK_DATA.csv', "r") as rawdata:
        csvFile = csv.DictReader(rawdata)
        for line in csvFile:   
            if _start_date <= getdate(line["date"]) <= _end_date: 
                print(line)
                results.append(line)
    return  results

def getdate(c) :
    x = datetime.strptime(c, "%m/%d/%Y")
    return x.date()

start_date = getdate(input("Press enter starting date(mm/dd/yyyy) \n") )
end_date =getdate(input("Press enter end date(mm/dd/yyyy) \n"))

results = check_file(start_date, end_date)
print(f"Identified {len(results)}  reports within specified timestamps")
