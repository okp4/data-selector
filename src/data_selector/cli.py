import click
import data_selector.__init__ as init
from data_selector.selector import select_data


@click.group()
def cli():
    """Data selection interactive tool."""
    pass


@cli.command
def version():
    """Print the application version information"""
    click.echo(init.__version__)


@cli.command()
@click.option(
    "-i",
    "--input",
    "input_file",
    type=click.Path(dir_okay=False, file_okay=True, exists=True, readable=True),
    required=True,
    help="Data file to convert",
)
@click.option(
    "-out",
    "--output",
    "out_file",
    type=str,
    required=True,
    help="name for the output files",
)
@click.option(
    "-f",
    "--force",
    "overwrite",
    type=bool,
    is_flag=True,
    default=False,
    help="Overwrite existing files",
)
@click.option(
    "-s",
    "--file_sep",
    "file_sep",
    type=str,
    required=False,
    default=",",
    help="File separator (csv).",
)
@click.option(
    "-row",
    "--nb_rows",
    "nb_rows",
    type=int,
    required=False,
    help="Number of rows to import from input_file.",
)
@click.option(
    "-keep",
    "--columns_to_keep",
    "path_columns_to_keep",
    type=click.Path(dir_okay=False, file_okay=True, exists=True, readable=True),
    required=False,
    help="Path to file with columns to keep.",
)
@click.option(
    "-delete",
    "--columns_to_delete",
    "path_columns_to_delete",
    type=click.Path(dir_okay=False, file_okay=True, exists=True, readable=True),
    required=False,
    help="Path to file with columns to delete.",
)
@click.option(
    "-values",
    "--values_to_keep",
    "path_to_values_to_keep",
    type=click.Path(dir_okay=False, file_okay=True, exists=True, readable=True),
    default=None,
    help="Path to file with columns and data to keep.",
)
def selector(
    input_file: str,
    out_file: str,
    overwrite: bool,
    file_sep: str,
    nb_rows: int,
    path_columns_to_keep: str,
    path_columns_to_delete: str,
    path_to_values_to_keep: str,
):
    """Start service to select Data to Keep/Delete"""
    select_data(
        input_file,
        out_file,
        overwrite,
        file_sep,
        nb_rows,
        path_columns_to_keep,
        path_columns_to_delete,
        path_to_values_to_keep,
    )


if __name__ == "__main__":
    cli()
