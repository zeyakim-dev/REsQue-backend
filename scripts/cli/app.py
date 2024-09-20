import typer

from scripts.cli.commands import domain_commands as domain

app = typer.Typer()

app.add_typer(domain.app, name="domain")

if __name__ == "__main__":
    app()