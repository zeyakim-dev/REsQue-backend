from pathlib import Path
from typing import List

import typer

app = typer.Typer()

def create_domain_structure(base_path: Path, domain_name: str):
    domain_path = base_path / domain_name
    folders = [
        "infrastructure",
        "domain",
        "usecase",
        "interface",
        "interface/api",
        "interface/repositories"
    ]
    
    for folder in folders:
        folder_path = domain_path / folder
        folder_path.mkdir(parents=True, exist_ok=True)
    
    typer.echo(f"Created folder structure for domain: {domain_name}")


@app.command("create")
def create_domains(names: List[str] = typer.Argument(..., help="List of domain names to create")):
    if not names:
        typer.echo("Error: Please provide at least one domain name.")
        raise typer.Exit(code=1)
    
    if len(names) > len(set(names)):
        typer.echo("Error: Duplicate domain names detected.")
        raise typer.Exit(code=1)
    
    root_path = Path.cwd()  # 현재 작업 디렉토리 (루트)
    domains_path = root_path / "app" / "domains"

    domains_path.mkdir(parents=True, exist_ok=True)
    
    for name in names:
        create_domain_structure(domains_path, name)
    
    is_single = len(names) == 1
    typer.echo(f"Successfully created domain{'s' if not is_single else ''}: {', '.join(names)}")
    return True