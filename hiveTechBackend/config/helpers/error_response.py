from rest_framework.response import Response


def error_response(message, status_code):
    return Response({'message': message}, status=status_code)
