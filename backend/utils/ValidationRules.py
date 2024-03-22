from cerberus.validator import Validator 
from cerberus.errors import BasicErrorHandler
import cerberus.errors as errors
from datetime import datetime

class ValidationRules:
    def __init__(self):
        self.user_schema = {
            'username': {
                'type': 'string',
                'minlength': 6,
                'empty': False
            },
            'email': {
                'type': 'string',
                'minlength': 6,
                'regex': '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
            },            
            'dateOfBirth': {
                'type': 'string',
                'minlength': 10,
                'maxlength': 10,
                'check_with': self.date_check
            },
            'password': {
                'type': 'string',
                'minlength': 8,
                'empty': False
            },
        }

    def validate_user(self, document):
        errorTypes = []
        val_main = Validator(self.user_schema, error_handler=CustomErrorHandler)
        result = val_main.validate(document, self.user_schema)

        if "username" in val_main.errors.keys():
            errorTypes.append("Username error")

        if "email" in val_main.errors.keys():
            errorTypes.append("Email error")

        if "dateOfBirth" in val_main.errors.keys():
            errorTypes.append("DOB error")

        #summary errors here if any
        errors = []
        for err in val_main.errors:
            errors.append({"field": err, "description": val_main.errors[err]})

        return {
            "success": result and len(errors) == 0,
            "errors": errors,
            "types": errorTypes
        }
        
    def date_check(self, field, value, error):
        toVerify = value
        try:
            datetime.strptime(toVerify, "%m/%d/%Y")

        except Exception as err:
            return error(field, "%s: Wrong date format" % field) 

class CustomErrorHandler(BasicErrorHandler):
    messages = BasicErrorHandler.messages.copy()
    messages[errors.MIN_LENGTH.code] = "Min length for {field} is {constraint}"
    messages[errors.ANYOF.code] = "At least one of these should be achieved: "