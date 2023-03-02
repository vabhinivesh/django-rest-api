from rest_framework.response import Response

keys = {'200': "OK", '304': "Not Modified", '400': "Bad Request", '401': "Unauthorized", '403': "Forbidden",
        '404': "Not Found", '409': "Conflict", '500': "Internal Server Error"}


def get_message(key):
    return keys.get(key)


def handle_success(data=None):
    return Response(data=data, status=200)


def handle_error(status=400):
    return Response(data={'status': get_message(status)}, status=status)


def handle_server_error(status=500):
    return Response(data={'status': get_message(status)}, status=status)
