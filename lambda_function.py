import datetime

def lambda_handler():
    return responseMapper(calculateValidTaxYear())

def calculateValidTaxYear():
    try:
        taxDay = datetime.datetime(2022, 4, 18) #initialize Tax Day as datetime
        currDate = datetime.datetime.now() #gets current date as datetime
        taxDateToString = taxDay.strftime("%m/%d/%Y") #convert dateTime to string
        taxYear = taxDateToString.split('/')[-1] #capture the year value of Tax Day as a String

        if currDate >= taxDay: # if the currentDate has passed or is Tax Day
            return  {0 : {"Valid Tax Years" : [taxYear] }} #return the current year we are in which will equal the current Tax year (this is a given)
    
        return {0: {"Valid Tax Years" : [str(int(taxYear) - 1), taxYear]}} #currentDate has not passed Tax Day, thus return last year and this year
    
    except Exception as ex:
        return {1: ex}

def responseMapper(response):
    if 0 in response:
        return {
            "Status": 200,
            "Body": response[0]
        }
    if 1 in response:
        return {
            "Status": 500,
            "Body": {"Internal Server Error": str(response[1])}
        }