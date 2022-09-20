from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    response = exception_handler(exc=exc, context= context)
    print("helloo")
    if response is not None:
        response.data['message'] = "There is an Error"
        response.data['status_code'] = 200
    return response