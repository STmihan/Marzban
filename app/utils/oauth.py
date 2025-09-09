import requests
from typing import Optional, Dict, Any
from config import GOOGLE_OAUTH_CLIENT_ID, GOOGLE_OAUTH_CLIENT_SECRET, GOOGLE_OAUTH_REDIRECT_URI


class GoogleOAuth:
    def __init__(self):
        self.client_id = GOOGLE_OAUTH_CLIENT_ID
        self.client_secret = GOOGLE_OAUTH_CLIENT_SECRET
        self.redirect_uri = GOOGLE_OAUTH_REDIRECT_URI
        self.scope = "openid email profile"

    def get_authorization_url(self, state: str) -> str:
        base_url = "https://accounts.google.com/o/oauth2/v2/auth"
        params = {
            "client_id": self.client_id,
            "redirect_uri": self.redirect_uri,
            "scope": self.scope,
            "response_type": "code",
            "state": state,
            "access_type": "offline"
        }

        query_string = "&".join([f"{k}={v}" for k, v in params.items()])
        return f"{base_url}?{query_string}"

    async def exchange_code_for_token(self, code: str) -> Optional[Dict[str, Any]]:
        token_url = "https://oauth2.googleapis.com/token"
        data = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "code": code,
            "grant_type": "authorization_code",
            "redirect_uri": self.redirect_uri
        }

        response = requests.post(token_url, data=data)
        if response.status_code == 200:
            return response.json()
        return None

    async def get_user_info(self, access_token: str) -> Optional[Dict[str, Any]]:
        user_info_url = "https://www.googleapis.com/oauth2/v2/userinfo"
        headers = {"Authorization": f"Bearer {access_token}"}

        response = requests.get(user_info_url, headers=headers)
        if response.status_code == 200:
            return response.json()
        return None