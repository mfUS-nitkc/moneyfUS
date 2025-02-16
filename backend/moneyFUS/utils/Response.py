from rest_framework.response import Response

def create_response(content, status):
  return Response({'success': True, **content}, status=status)

def create_error_response(detail, status):
  return Response({"success": False, **detail}, status=status)