import os
import pandas as pd


def check(result_path: str, ref_path):
    path: str = os.path.join(result_path, os.listdir(result_path)[0])
    csv_out = os.path.join(path, os.listdir(path)[0])
    name = os.path.basename(csv_out)
    csv_ref = os.path.join(ref_path, name)
    assert os.path.isfile(
        csv_ref
    ), f"referenced json file with name {name} do not exists"

    df_ref: pd.DataFrame = pd.read_csv(csv_ref, low_memory=False)
    df_out: pd.DataFrame = pd.read_csv(csv_out, low_memory=False)
    assert df_ref.equals(
        df_out
    ), f"CSV {csv_out} should be the same than the reference CSV {csv_ref}"
