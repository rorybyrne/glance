"""
File: naive_branch.py
Author: synek
Email: rory@syze.ai
Github: https://github.com/synek
Description: A naive view which simply lists branches.
"""

from typing import List
from glance.view.base import View


class NaiveBranchView(View):
    """Naive view to list branhes"""

    def __init__(self, repos: List[str]):
        """Initialize"""
        super().__init__(repos)

    def render(self):
        for repo in self.repos:
            print(repo)

