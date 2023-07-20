from django.http import JsonResponse
import requests

def azure_request_view(request):
    url = "https://login.microsoftonline.com/9f17a5ad-b8a1-4066-973b-71d37bf44778/oauth2/v2.0/token"

    payload = {
        "scope": "https://graph.microsoft.com/.default",
        "grant_type": "client_credentials",
        "client_secret": "ggQ8Q~oRUwT3cQFfP1O0OR_N2Ihqxa_S3aXrVb8E",
        "client_id": "0ea844aa-a6cc-4f8d-8151-d8292d1c340e"
    }

    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    response = requests.post(url, data=payload, headers=headers)
    data = response.json()

    if "access_token" in data:
        token = data["access_token"]
        return JsonResponse({"token": token})
    else:
        return JsonResponse({"error": "Failed to obtain access token"})
