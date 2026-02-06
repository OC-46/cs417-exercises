from datetime import datetime, date, timedelta
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

def format_relative(date_str: str) -> str:
    """
    Given a date string in YYYY-MM-DD format, return a human-readable string
    describing how far it is from today.
    
    Args:
        date_str: A date string in YYYY-MM-DD format
        
    Returns:
        A human-readable string describing the relative date:
        - "today" if it's today's date
        - "X days ago" if it's in the past
        - "in X days" if it's in the future
    """
    target_date = datetime.strptime(date_str, "%Y-%m-%d").date()
    today = date.today()
    
    delta = (target_date - today).days
    
    if delta == 0:
        return "today"
    elif delta < 0:
        days_ago = abs(delta)
        if days_ago == 1:
            return "1 day ago"
        else:
            return f"{days_ago} days ago"
    else:  # delta > 0
        if delta == 1:
            return "in 1 day"
        else:
            return f"in {delta} days"