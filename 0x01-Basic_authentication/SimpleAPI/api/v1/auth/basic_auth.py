from api.v1.auth.auth import Auth
import re
import base64
from models.user import User
from typing import TypeVar


class BasicAuth(Auth):
    """
    Handles basic authentication
    """

    def extract_base64_authorization_header(
            self,
            authorization_header: str) -> str:
        """ Returns the Base64 part of the Authorization"""
        if authorization_header is None or\
                not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith('Basic '):
            return None

        values = re.split("Basic ", authorization_header)
        if not values and not values[1]:
            return None
        return values[1]

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str) -> str:
        """ Base64 decoder """
        if base64_authorization_header is None or\
                type(base64_authorization_header) is not str:
            return None

        try:
            decoded = base64.b64decode(base64_authorization_header)
            decoded = decoded.decode('utf-8')
        except Exception as e:
            return None

        return decoded

    def extract_user_credentials(
            self,
            decoded_base64_authorization_header: str) -> (str, str):
        """ Returns the email and password from base64 decoded value """
        if decoded_base64_authorization_header is None or\
                type(decoded_base64_authorization_header) is not str:
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None

        values = re.split(':', decoded_base64_authorization_header)
        if values:
            return values[0], values[1]

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """ Returns User instance based in his email and password """
        if user_email is None or user_pwd is None:
            return None
        if type(user_email) is not str or type(user_pwd) is not str:
            return None

        user = User.search({'email': user_email})
        if not user:
            return None

        if not user[0].is_valid_password(user_pwd):
            return None
        return user[0]

    def current_user(self, request=None) -> TypeVar('User'):
        """Retrieves the user from a request.
        """
        auth_header = self.authorization_header(request)
        b64_auth_token = self.extract_base64_authorization_header(auth_header)
        auth_token = self.decode_base64_authorization_header(b64_auth_token)
        email, password = self.extract_user_credentials(auth_token)
        return self.user_object_from_credentials(email, password)
