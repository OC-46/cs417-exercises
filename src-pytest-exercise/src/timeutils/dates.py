from datetime import datetime
def days_between(date1: str, date2: str) -> int:
"""Return the absolute number of days between two ISO-format date strings.
Args:
date1: A date string in YYYY-MM-DD format.
date2: A date string in YYYY-MM-DD format.
Returns:
The absolute difference in days.
Raises:
ValueError: If either string doesn't match YYYY-MM-DD format.
"""
fmt = "%Y-%m-%d"
d1 = datetime.strptime(date1, fmt)
d2 = datetime.strptime(date2, fmt)
return abs((d2 - d1).days)
def is_weekend(date_str: str) -> bool:
"""Check whether a date falls on a Saturday or Sunday.
Args:
date_str: A date string in YYYY-MM-DD format.
Returns:
True if the date is a Saturday or Sunday, False otherwise.
Raises:
ValueError: If the string doesn't match YYYY-MM-DD format.
"""
fmt = "%Y-%m-%d"
dt = datetime.strptime(date_str, fmt)
return dt.weekday() >= 5