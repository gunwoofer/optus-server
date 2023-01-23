import pytest

from optus_server.optimize import divide_date_by_month, divide_date_by_week


@pytest.fixture
def date_range_month():
    return [['2023-01-30', '2023-01-31'], ['2023-02-01', '2023-02-02']]

def test_divide_date_by_month_2_month(date_range_month):
    arrival_date = "2023-01-30"
    departure_date = "2023-02-02"
    assert divide_date_by_month(arrival_date, departure_date) == date_range_month


@pytest.fixture
def date_range_month_2():
    return [[
        '2023-01-01',
        '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05', '2023-01-06', '2023-01-07', '2023-01-08',
        '2023-01-09', '2023-01-10', '2023-01-11', '2023-01-12', '2023-01-13', '2023-01-14', '2023-01-15',
        '2023-01-16', '2023-01-17', '2023-01-18', '2023-01-19', '2023-01-20', '2023-01-21', '2023-01-22',
        '2023-01-23', '2023-01-24', '2023-01-25', '2023-01-26', '2023-01-27', '2023-01-28', '2023-01-29',
        '2023-01-30', '2023-01-31']]

def test_divide_date_by_month_full_month(date_range_month_2):
    arrival_date = "2023-01-01"
    departure_date = "2023-01-31"
    assert divide_date_by_month(arrival_date, departure_date) == date_range_month_2


@pytest.fixture
def date_range_week():
    return [['2023-01-30', '2023-01-31','2023-02-01', '2023-02-02']]

def test_divide_date_by_week(date_range_week):
    arrival_date = "2023-01-30"
    departure_date = "2023-02-02"
    assert divide_date_by_week(arrival_date, departure_date) == date_range_week


@pytest.fixture
def date_range_week_2():
    return [
        ['2023-01-01'],
        ['2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05', '2023-01-06', '2023-01-07', '2023-01-08'],
        ['2023-01-09', '2023-01-10', '2023-01-11', '2023-01-12', '2023-01-13', '2023-01-14', '2023-01-15'],
        ['2023-01-16', '2023-01-17', '2023-01-18', '2023-01-19', '2023-01-20', '2023-01-21', '2023-01-22'],
        ['2023-01-23', '2023-01-24', '2023-01-25', '2023-01-26', '2023-01-27', '2023-01-28', '2023-01-29'],
        ['2023-01-30', '2023-01-31']
    ]

def test_divide_date_by_week_2(date_range_week_2):
    arrival_date = "2023-01-01"
    departure_date = "2023-01-31"
    assert divide_date_by_week(arrival_date, departure_date) == date_range_week_2