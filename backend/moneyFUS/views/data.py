from django.http import JsonResponse


def data(request):
    data = [{"id": 1, "date": "2024-10-21", "content": "TESTTEST"}]
    return JsonResponse(data, safe=False)
