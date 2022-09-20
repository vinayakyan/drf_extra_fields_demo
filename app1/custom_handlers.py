from django.http import JsonResponse


def handler404(request, *args, **kwargs):
    data = {"message": "Resource you're looking for does not exist",
            "status": 200}
    return JsonResponse(data=data)