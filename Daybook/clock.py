"""Daybook's "now", in the user's time zone rather than the server's (Streamlit Cloud runs on UTC)."""

from datetime import datetime
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError


def zone(name):
    """ZoneInfo for a name like "Asia/Kolkata", or None if it's empty or unknown."""
    try:
        return ZoneInfo(name) if name else None
    except (ZoneInfoNotFoundError, ValueError):
        return None


def now(tz=None):
    """The current wall-clock time in tz (or the server's own zone), without tzinfo, as reminders are stored."""
    return datetime.now(tz).replace(tzinfo=None) if tz else datetime.now()
