"""
Professional CLI Calculator for Platform Engineering.
Uses Click for robust command-line interface.
"""

import click
from rich.console import Console
from rich.table import Table
from rich import print as rprint

from calculator import operations

console = Console()


@click.group()
def cli():
    """Professional CLI Calculator for Platform Engineering."""
    pass


@cli.command()
@click.argument("a", type=float)
@click.argument("b", type=float)
def add(a, b):
    """Add two numbers: A + B"""
    result = operations.add(a, b)
    console.print(f"[green]Result:[/green] {a} + {b} = {result}")
    return result


@cli.command()
@click.argument("a", type=float)
@click.argument("b", type=float)
def subtract(a, b):
    """Subtract two numbers: A - B"""
    result = operations.subtract(a, b)
    console.print(f"[green]Result:[/green] {a} - {b} = {result}")
    return result


@cli.command()
@click.argument("a", type=float)
@click.argument("b", type=float)
def multiply(a, b):
    """Multiply two numbers: A * B"""
    result = operations.multiply(a, b)
    console.print(f"[green]Result:[/green] {a} × {b} = {result}")
    return result


@cli.command()
@click.argument("a", type=float)
@click.argument("b", type=float)
def divide(a, b):
    """Divide two numbers: A / B"""
    try:
        result = operations.divide(a, b)
        console.print(f"[green]Result:[/green] {a} ÷ {b} = {result}")
        return result
    except ZeroDivisionError as e:
        console.print(f"[red]Error:[/red] {e}")
        raise click.Abort()


@cli.command()
@click.argument("a", type=float)
@click.argument("b", type=float)
def power(a, b):
    """Raise A to the power of B: A ** B"""
    result = operations.power(a, b)
    console.print(f"[green]Result:[/green] {a} ^ {b} = {result}")
    return result


@cli.command()
@click.argument("a", type=float)
def sqrt(a):
    """Calculate square root of A"""
    try:
        result = operations.sqrt(a)
        console.print(f"[green]Result:[/green] √{a} = {result}")
        return result
    except ValueError as e:
        console.print(f"[red]Error:[/red] {e}")
        raise click.Abort()


@cli.command()
def list_operations():
    """List all available operations"""
    table = Table(title="Available Operations", show_header=True, header_style="bold magenta")
    table.add_column("Command", style="cyan")
    table.add_column("Description")
    table.add_column("Usage")
    
    operations_info = [
        ("add", "Add two numbers", "calculator add 5 3"),
        ("subtract", "Subtract two numbers", "calculator subtract 10 4"),
        ("multiply", "Multiply two numbers", "calculator multiply 7 6"),
        ("divide", "Divide two numbers", "calculator divide 15 3"),
        ("power", "Raise to power", "calculator power 2 8"),
        ("sqrt", "Square root", "calculator sqrt 25"),
    ]
    
    for cmd, desc, usage in operations_info:
        table.add_row(cmd, desc, usage)
    
    console.print(table)


def main():
    """Entry point for the calculator CLI."""
    return cli()


if __name__ == "__main__":
    main()