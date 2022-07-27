import click
import src.data_selector.__init__ as init
from src.data_selector.selector import select


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
    help="Data file to convert"
)
@click.option(
    "-o",
    "--output",
    "output_file",
    type=str,
    default="test",
    help="Name for the output files"
)
@click.option(
    "-f",
    "--force",
    "overwrite",
    type=bool,
    is_flag=True,
    default=False,
    help="Overwrite existing files"
)
@click.option(
    "-fi",
    "--format_in",
    "file_format_in",
    type=str,
    required=True,
    help="File format of the input (csv, json).",
)
@click.option(
    "-fo",
    "--format_out",
    "file_format_out",
    type=str,
    required=False,
    default='csv',
    help="File format of the output (csv, json).",
)
@click.option(
    "-s",
    "--file_sep",
    "file_sep",
    type=str,
    required=False,
    default=',',
    help="File separator (csv).",
)
@click.option(
    "-S",
    "--select",
    "path_columns_to_keep",
    type=str,
    required=False,
    help="Path to file with columns to keep."
)
@click.option(
    "-D",
    "--delete",
    "path_columns_to_delete",
    type=click.Path(),
    required=False,
    help="Path to file with columns to delete."
)
@click.option(
    "-sD",
    "--dataColumn",
    "path_to_data_and_columns",
    type=str,
    default=None,
    help="Path to file with columns and data to keep."
)
def select_cli(
    input_file: str,
    output_file: str,
    overwrite: bool,
    file_format_in: str,
    file_format_out: str,
    path_columns_to_keep: str,
    path_columns_to_delete: str,
    path_to_data_and_columns: str,
    file_sep: str,
    data_frame=None
):
    """Start service to select Data to Keep/Delete"""
    select(
        input_file,
        output_file,
        overwrite,
        file_format_in,
        file_format_out,
        path_columns_to_keep,
        path_columns_to_delete,
        path_to_data_and_columns,
        file_sep,
        data_frame
    )


if __name__ == "__main__":
    cli()
