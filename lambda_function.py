import datetime

def lambda_handler(event, context) -> dict:
    """
    lambda_handler() calls calculateValidTaxYear() and passes its return value to responseMapper().
    :return: A dictionary value representing a network response returned by responseMapper()
    """
    return responseMapper(calculateValidTaxYear())

def calculateValidTaxYear() -> dict:
    """
    calculateValidTaxYear() fetches the current date and returns the 
    valid tax years for that date for Tax Day 2022

    :return: Returns a dictionary containing a custom Response Key 
    that maps to a dictionary of valid tax years for the current date
    
    Abiding by the MVC philosophy, this function should never return or be informed of
    any response codes that pertain to its return value. Rather a Response Key is utilized
    that handler functions will convert to an appropriate response
    """ 
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

def responseMapper(response: dict) -> dict:
    """
    responseMapper() parses the parameter passed and maps the dict value to a custom response body
    based on the Response Key passed in the response.
    Response Key = 0 when the response parameter is a success response
    Response Key = 1 when the response parameter is an error response

    :param : A dictionary containing a custom Response Key and a Value
    :return: Returns a response with a Status Code and Body containing the value parsed in the parameter
    """ 
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