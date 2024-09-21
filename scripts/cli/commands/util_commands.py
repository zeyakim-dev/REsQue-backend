import os
from pathlib import Path
from typing import List

import typer
from rich import print
from rich.tree import Tree

app = typer.Typer()


def read_ignore_patterns(ignore_file: Path) -> List[str]:
    if ignore_file.exists():
        with ignore_file.open() as f:
            return [
                line.strip() for line in f if line.strip() and not line.startswith("#")
            ]
    return []


def should_ignore(path: Path, ignore_patterns: List[str]) -> bool:
    return any(path.match(pattern) for pattern in ignore_patterns)


def build_directory_tree(
    directory: Path, tree: Tree, ignore_patterns: List[str], root_dir: Path
) -> None:
    for item in sorted(
        directory.iterdir(), key=lambda x: (not x.is_dir(), x.name.lower())
    ):
        if should_ignore(item.relative_to(root_dir), ignore_patterns):
            continue
        if item.is_dir():
            branch = tree.add(f"[bold blue]{item.name}[/bold blue]")
            build_directory_tree(item, branch, ignore_patterns, root_dir)
        else:
            tree.add(f"[green]{item.name}[/green]")


@app.command("tree")
def tree_command(
    ignore_file: str = typer.Option(".treeignore", help="Path to the ignore file")
):
    """
    Display the directory tree from the current working directory, excluding items specified in .treeignore file.
    """
    root_dir = Path.cwd()  # Get the current working directory (pwd)
    ignore_file_path = root_dir / ignore_file
    ignore_patterns = read_ignore_patterns(ignore_file_path)

    tree = Tree(f"[bold red]{root_dir.name}[/bold red]")
    build_directory_tree(root_dir, tree, ignore_patterns, root_dir)
    print(tree)
