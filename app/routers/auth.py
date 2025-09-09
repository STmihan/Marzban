# from fastapi import APIRouter, Depends, HTTPException
# from app.db import Session, get_db
#
# router = APIRouter(prefix="/auth", tags=["Authentication"])
#
#
# @router.get("/google/login")
# async def google_login():
#     if not GOOGLE_OAUTH_ENABLED:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="Google OAuth is not enabled"
#         )
#
#     oauth = GoogleOAuth()
#     state = secrets.token_urlsafe(32)
#     authorization_url = oauth.get_authorization_url(state)
#
#     response = RedirectResponse(url=authorization_url)
#     response.set_cookie(key="oauth_state", value=state, httponly=True, secure=True)
#     return response
#
#
# @router.get("/google/callback")
# async def google_callback(
#         request: Request,
#         code: str = None,
#         state: str = None,
#         error: str = None,
#         db: Session = Depends(get_db)
# ):
#
#
# @router.get("/google/status")
# async def google_oauth_status():
#     return {
#         "enabled": GOOGLE_OAUTH_ENABLED,
#         "client_id": GOOGLE_OAUTH_CLIENT_ID if GOOGLE_OAUTH_ENABLED else None
#     }
