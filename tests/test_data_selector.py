#!/usr/bin/env python3
import pandas as pd
from pandas import DataFrame as df
import json
import os
from src.data_selector.cli import cli
import src.data_selector.selector as selector
from src.data_selector.__init__ import __version__
from click.testing import Result, CliRunner


def test_delete_column():
    # arrange
    data_frame: df = pd.read_csv(os.getcwd() + "/tests/data/inputs/test.csv")
    list_of_names: list[str] = data_frame.columns.to_list()

    # act
    data_frame = selector.delete_column(data_frame, ["ARTIST_RAW", "SONG_RAW"])

    # assert
    assert list_of_names != data_frame.columns.to_list()
    assert data_frame.columns.to_list() == [
        "Song_Clean",
        "ARTIST_CLEAN",
        "CALLSIGN",
        "TIME",
        "UNIQUE_ID",
        "COMBINED",
        "First?",
    ]


def test_select_column():
    # arrange
    data_frame: df = pd.read_csv(os.getcwd() + "/tests/data/inputs/test.csv")
    list_of_names: list[str] = data_frame.columns.to_list()

    # act
    data_frame = selector.select_column(data_frame, ["ARTIST_RAW", "SONG_RAW"])

    # assert
    assert str(list_of_names) != str(data_frame.columns.to_list())
    assert data_frame.columns.to_list() == ["ARTIST_RAW", "SONG_RAW"]


def test_select_data_and_column():
    # arrange
    data_frame: df = pd.read_csv(os.getcwd() + "/tests/data/inputs/test.csv")
    list_of_names: list[str] = data_frame.columns.to_list()
    number_of_rows_control: int = len(data_frame.index)
    with open(os.getcwd() + "/tests/data/inputs/data_col_param.json") as d:
        param_dict: dict = json.load(d)

    # act
    data_frame = selector.select_data_and_column(
        data_frame, param_dict
    )

    # assert
    assert str(list_of_names) != str(data_frame.columns.to_list())
    assert data_frame.columns.to_list() == ['Song Clean', 'First?', 'temp_test']
    assert number_of_rows_control >= len(data_frame.index)


def test_version_displays_library_version():
    # arrange
    runner: CliRunner = CliRunner()

    # act
    result: Result = runner.invoke(cli, ["version"])

    # assert
    assert (
        __version__ == result.output.strip()
    ), "Version number should match library version."
