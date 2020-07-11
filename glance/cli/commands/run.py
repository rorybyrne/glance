"""
Run

@author Rory Byrne <rory@syze.ai>
"""

import click

from glance.view.naive_branch import NaiveBranchView


@click.command()
@click.option('--repos', help="A comma-separated list of repositories")
@click.option('--org', help="A Github Organization")
def run(repos: str, org: str) -> None:
    view = NaiveBranchView(repos.split(','))
    view.populate()
    view.render()
