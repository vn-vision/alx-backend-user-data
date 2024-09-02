"""
Class Auth: - manage API authentication
"""
from flask import request
from typing import List, TypeVar


class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Returns
        - True if:
            path is not in the list of excluded paths
            path is None
            excluded paths list is None or empty
        - False if:
            path is in excluded paths list
        """

        if path is None or excluded_paths is None or excluded_paths == []:
            return True

        # remove all trailing / in paths in the excluded paths
        excluded_paths = [path.rstrip('/') for path in excluded_paths]
        path = path.rstrip('/')

        return path not in excluded_paths

    def authorization_header(self, request=None) -> str:
        """
        Returns None if request is None
            request doesn't contain the header key Authorization
        return value of the header request Authorization
        """
        if request is None:
            return None

        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns None
        """
        return None
