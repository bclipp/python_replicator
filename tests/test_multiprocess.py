"""
tests for the multiprocess
"""

import pandas as pd
import pytest

import replicant.multiprocess as mult

TESTDATA = [pd.DataFrame(
    columns=["This",
             "is",
             "a",
             "test",
             "to",
             "check",
             "a_function"],
    data=[[5, 2, "b", 3, 4, 5, 3],
          [7, 2, "b", 3, 4, 5, 3],
          [8, 2, "b", 3, 4, 5, 3],
          [3, 2, "b", 3, 4, 5, 3],
          [2, 2, "b", 3, 4, 5, 3],
          [8, 2, "b", 3, 4, 5, 3],
          [2, 2, "b", 3, 4, 5, 3],
          [8, 2, "b", 3, 4, 5, 3],
          [19, 2, "b", 3, 4, 5, 3],
          [53, 2, "b", 3, 4, 5, 3],
          [11, 2, "b", 3, 4, 5, 3],
          [16, 2, "b", 3, 4, 5, 3]])]


def this_me(x):
    return x["This"]


@pytest.mark.parametrize("data_frame", TESTDATA)
def test_multiprocess_me_side_effect(data_frame):
    """
    Used to test the multiprocess function without a return
    """
    data: list = list(data_frame.T.to_dict().values())
    mult.multiprocess_me(1, print, data, False)


@pytest.mark.parametrize("data_frame", TESTDATA)
def test_multiprocess_me_side_return(data_frame):
    """
    Used to test the multiprocess funciton without a return
    """
    data: list = list(data_frame.T.to_dict().values())
    mult.multiprocess_me(1, this_me, data, True)


def test_multiprocess_not_data_frame_input():
    """
    Used to test the multiprocess funciton with a bad input
    """
    data: str = "this is not a DataFrame"
    try:
        mult.multiprocess_me(1, this_me, data, False)
    except Exception:
        assert True
