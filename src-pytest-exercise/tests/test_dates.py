import pytest
import pytest
from datetime import date, timedelta
from timeutils.dates import days_between, is_weekend, format_relative
def test_days_between_same_day():
    """Two identical dates should be 0 days apart."""
    assert days_between("2025-03-15", "2025-03-15") == 0
def test_days_between_one_week():
    """A known pair exactly 7 days apart."""
    assert days_between("2025-03-01", "2025-03-08") == 7
def test_days_between_order_independent():
    """Swapping the arguments should give the same result."""
    assert days_between("2025-01-01", "2025-06-15") == days_between("2025-06-15", "2025-01-01")
def test_is_weekend_saturday():
    """March 15, 2025 is a Saturday."""
    assert is_weekend("2025-03-15") is True
def test_is_weekend_weekday():
    """March 17, 2025 is a Monday."""
    assert is_weekend("2025-03-17") is False
def test_days_between_invalid_format():
    """A badly formatted string should raise ValueError."""
    with pytest.raises(ValueError):
        days_between("not-a-date", "2025-03-15")

def test_format_relative_today():
    today = date.today().strftime("%Y-%m-%d")
    assert format_relative(today) == "today"

def test_format_relative_past():
    three_days_ago = (date.today() - timedelta(days=3)).strftime("%Y-%m-%d")
    assert format_relative(three_days_ago) == "3 days ago"

def test_format_relative_future():
    five_days_future = (date.today() + timedelta(days=5)).strftime("%Y-%m-%d")
    assert format_relative(five_days_future) == "in 5 days"

def test_format_relative_yesterday():
    yesterday = (date.today() - timedelta(days=1)).strftime("%Y-%m-%d")
    assert format_relative(yesterday) == "1 day ago"

def test_format_relative_tomorrow():
    tomorrow = (date.today() + timedelta(days=1)).strftime("%Y-%m-%d")
    assert format_relative(tomorrow) == "in 1 day"