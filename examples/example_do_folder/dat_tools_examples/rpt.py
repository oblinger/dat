import json

from dvc_dat import Dat
from dvc_dat import dat_tools as dt


def load_points_json(dat: Dat):  # noqa
    with open(f"{dat.get_path()}/points.json") as f:
        return json.load(f)


#

simple = {
    "main": {"do": "dt.dat_report"},
    "dat_report": {
        "title": "Retail Data Matrix",
        "source": "Datasets/Retail Data",
        "metrics": ["rpt.load_points_json"],
        "show": False,
    }
}


# this is the default report
main = {
    "main": {"do": "dt.dat_report"},
    "dat_report": {
        "title": "RPT",
        "source": "Datasets/Retail Data",
        "metrics": ["rpt.load_points_json"],
        "docs": ["list"],
        "sheets": ["Store", "Month"],
        "show": False,
    }
}


def my_test_code(dat: Dat):
    df = dt.dat_report(dat)
    print(df)
    dt.to_excel(df, title="My Test", show=False)
    return df


my_test = {
    "main": {"do": my_test_code},
    "dat_report": {
        "title": "My Test",
        "source": "Datasets/Retail Data/Berkeley",
        "metrics": ["rpt.load_points_json"],
        "sheets": ["Store"],
        "show": False,
    }
}


def fully_manual():
    df = dt.from_dat("Datasets/Retail Data", ["rpt.load_points_json"])
    print(df)
    dt.to_excel(df, title="fully manual test", show=False)
    return df
