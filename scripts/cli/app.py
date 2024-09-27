import typer

from scripts.cli.commands import DomainApp, UtilApp

app = typer.Typer()

app.add_typer(DomainApp, name="domain")
app.add_typer(UtilApp, name="util")

if __name__ == "__main__":
    app()
