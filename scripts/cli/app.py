import typer

from scripts.cli.commands import domain_commands as domain
from scripts.cli.commands import util_commands as util

app = typer.Typer()

app.add_typer(domain.app, name="domain")
app.add_typer(util.app, name="util")

if __name__ == "__main__":
    app()