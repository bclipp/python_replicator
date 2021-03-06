"""
tests for the multiprocess
"""
from typing import Optional, Any, List

import pandas as pd
import pytest

import replicators.multiprocess as mult

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


def return_this(anything: dict):
    """
    returns the value in the "This" key.
    :param anything:
    :return:
    """
    return anything["This"]


@pytest.mark.parametrize("data_frame", TESTDATA)
def test_multiprocess_me_side_effect(data_frame: pd.DataFrame):
    """
    Used to test the multiprocess function without a return
    """
    data: list = list(data_frame.T.to_dict().values())
    mult.multiprocess_me(1, print, data, False)


@pytest.mark.parametrize("data_frame", TESTDATA)
def test_multiprocess_me_side_return(data_frame: pd.DataFrame):
    """
    Used to test the multiprocess function without a return
    """
    data: Optional[Any] = list(data_frame.T.to_dict().values())
    got: Optional[List[Any]] = mult.multiprocess_me(1, return_this, data, True)
    want: list = [5, 7, 8, 3, 2, 8, 2, 8, 19, 53, 11, 16]
    assert got == want


def test_multiprocess_not_data_frame_input():
    """
    Used to test the multiprocess function with a bad input
    """
    data: str = "this is not a DataFrame"
    try:
        mult.multiprocess_me(1, print, data, False)
    except mult.NotDict:
        assert True
