import os.path
import pytest
from click.testing import Result, CliRunner
from data_selector import __version__, cli
from tests.utils import check


def test_version_displays_library_version():
    # arrange
    runner: CliRunner = CliRunner()

    # act
    result: Result = runner.invoke(cli.cli, ["version"])

    # assert
    assert (
        __version__ == result.output.strip()
    ), "Version number should match library version."


def get_arguments(test_path: str) -> list[list[str]]:
    input_file = os.path.join(test_path, "test.csv")
    name = os.path.basename(input_file).replace(".csv", "")
    columns_to_keep = os.path.join(test_path, "keep_col_test.json")
    values_to_keep = os.path.join(test_path, "values_keep_test.json")
    return [
        [
            "-i",
            os.path.abspath(input_file),
            "-out",
            name,
            "-f",
            "-keep",
            os.path.abspath(columns_to_keep),
            "-values",
            os.path.abspath(values_to_keep),
        ]
    ]


@pytest.mark.parametrize("arguments", get_arguments("./tests/data/inputs_test"))
def test_converter(tmpdir_factory, arguments):
    runner: CliRunner = CliRunner()
    ref_folder = os.path.abspath("tests/data/ref_outputs")
    out_folder = str(tmpdir_factory.mktemp("data"))
    with runner.isolated_filesystem(temp_dir=out_folder):
        result: Result = runner.invoke(
            cli=cli.cli, args=["selector"] + arguments, catch_exceptions=False
        )
        if result.exit_code != 0:
            print(result.output)

        # assert
        assert result.exit_code == 0, "Exit code should return 0"
        check(out_folder, ref_folder)
