import pytest

from analysis import sdc


@pytest.mark.parametrize("data_in,data_out", [(6, 0), (7, 0), (8, 8)])
def test_redact_le_seven(data_in, data_out):
    assert sdc.redact_le_seven(data_in) == data_out


@pytest.mark.parametrize("data_in,data_out", [(1, 0), (3, 5), (5, 5), (7, 5), (9, 10)])
def test_round_to_nearest_five(data_in, data_out):
    assert sdc.round_to_nearest_five(data_in) == data_out
