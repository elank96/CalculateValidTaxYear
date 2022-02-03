import datetime

def lambda_handler():
    return {
        "Status": 200,
        "Body": calculateValidTaxYear() 
        }

def calculateValidTaxYear():
    taxDay = datetime.datetime(2022, 4, 18) #initialize Tax Day as datetime
    currDate = datetime.datetime.now() #gets current date as datetime
    taxDateToString = taxDay.strftime("%m/%d/%Y") #convert dateTime to string
    taxYear = taxDateToString.split('/')[-1] #capture the year value of Tax Day as a String

    if currDate >= taxDay: # if the currentDate has passed or is Tax Day
        return  {"Valid Tax Years" : [taxYear] } #return the current year we are in which will equal the current Tax year (this is a given)
   
    return {"Valid Tax Years" : [str(int(taxYear) - 1), taxYear]} #currentDate has not passed Tax Day, thus return last year and this year


print(lambda_handler())