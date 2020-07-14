"""
This module is used for abstracted uses of the multiprocess library.
"""

import multiprocessing as mp
from typing import Callable, Optional


def multiprocess_me(size: int,
                    func: Callable,
                    data: list,
                    output: bool = True) -> Optional[list]:
    """
    multiprocess_me is used to multiprocess across a list of dicts.

    :param size:  The amount of parallelism.
    :param func: the function to use on each dict
    :param data: a list of dicts.
    :param output: Should multiprocess_me return a list of Dict?
    :return:
    """
    if not isinstance(data, list):
        raise Exception("Data must be a a dict")
    pool = mp.Pool(size)
    updated_data: list = pool.map(func, data)
    pool.close()
    pool.join()
    if output:
        return updated_data
    return None
