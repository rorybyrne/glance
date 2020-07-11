"""
Commandline Entry Point

@author Rory Byrne <rory@syze.ai>
"""

import click

from glance.cli.commands.run import run

@click.group()
@click.version_option()
def cli():
    pass

cli.add_command(run)

