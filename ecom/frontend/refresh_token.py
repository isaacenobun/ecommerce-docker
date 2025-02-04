from django.http import JsonResponse
import requests

def refresh(refresh_url,json):
    """Quickly refresh your access token given that the refresh token hasn't expired yet.

    Args:
        refresh_url (url): Refresh Url
        json (dictionary): Dictionary with 'refresh' as key and the refresh token as value

    Returns:
        access_token (string): The new access token
    """
    
    refresh_response = requests.post(refresh_url, json=json)
    new_tokens = refresh_response.json()
    
    new_access_token = new_tokens.get("access")
    if not new_access_token:
        return JsonResponse({"error": "Failed to refresh access token"}, status=400)
    
    return new_access_token