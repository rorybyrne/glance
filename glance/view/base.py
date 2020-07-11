"""
Base class for Views

@author Rory Byrne <rory@syze.ai>
"""

from typing import Dict, List
from abc import abstractmethod


class View:

    def __init__(self, repos: List[str]):
        self.repos = repos

    @abstractmethod
    def render(self):
        raise NotImplementedError()

    def populate(self):
        raise NotImplementedError()

    @classmethod
    def from_yam(cls, path: str) -> 'View':
        """Parses a YAML file into a View.

        @param path:    The path to the YAML file
        @return: A View instance.
        """
        raise NotImplementedError("Should be implemented in subclasses.")

    @abstractmethod
    def from_dict(self, view_dict: Dict) -> 'View':
        """Parses a Dict into a View.

        @param view_dict:   A Dict defining the view.
        @return: A View instance.
        """
        raise NotImplementedError()

