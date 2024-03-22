from flask import jsonify, make_response

class GenericResponses:
    def success():
        responseData = {'message': 'OK', 'code': 'SUCCESS'}
        return make_response(jsonify(responseData), 201)
    
    def specific_error_msg(msg):
        responseData = {'message': msg, 'code': 'FAILURE'}
        return make_response(jsonify(responseData), 201)    
    
    def specific_error(msg, details):
        responseData = {'message': msg, 'details': details, 'code': 'FAILURE'}
        return make_response(jsonify(responseData), 201)    
    
    def error(ex):
        responseData = {'type': str(type(ex)), 'message': str(ex), 'code': 'FAILURE'}
        return make_response(jsonify(responseData), 500)