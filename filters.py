import pandas as pd
import numpy as np


# ── Load & Engineer Features ──────────────────────────────────────────────────
def load_data(filepath: str) -> pd.DataFrame:
    """
    Load the Uber NYC dataset and engineer all required columns.
    Expected file: uber-raw-data-apr14.csv (or any month variant)
    Columns in raw file: Date/Time, Lat, Lon, Base
    """
    df = pd.read_csv(filepath)

    # Parse datetime
    df["Date/Time"] = pd.to_datetime(df["Date/Time"], errors="coerce")
    df.dropna(subset=["Date/Time"], inplace=True)

    # Drop rows with missing lat/lon
    df.dropna(subset=["Lat", "Lon"], inplace=True)

    # Remove obvious coordinate outliers (keep NYC bounding box)
    df = df[(df["Lat"] >= 40.4) & (df["Lat"] <= 41.0)]
    df = df[(df["Lon"] >= -74.3) & (df["Lon"] <= -73.6)]

    # Feature engineering
    df["Hour"]       = df["Date/Time"].dt.hour
    df["Month"]      = df["Date/Time"].dt.month
    df["DayNum"]     = df["Date/Time"].dt.dayofweek          # 0=Mon
    df["DayOfWeek"]  = df["Date/Time"].dt.day_name()
    df["WeekOfYear"] = df["Date/Time"].dt.isocalendar().week.astype(int)
    df["Date"]       = df["Date/Time"].dt.date

    # Strip whitespace from Base
    df["Base"] = df["Base"].astype(str).str.strip()

    return df.reset_index(drop=True)


# ── Apply All Filters ─────────────────────────────────────────────────────────
def apply_filters(
    df: pd.DataFrame,
    date_range: tuple   = None,
    bases: list         = None,
    hour_range: tuple   = (0, 23),
    days: list          = None,
    search_text: str    = ""
) -> pd.DataFrame:
    """
    Apply all sidebar filters to the raw dataframe.
    All parameters are optional — passing None uses the full range.

    Parameters
    ----------
    df          : raw dataframe from load_data()
    date_range  : (start_date, end_date) — Python date objects
    bases       : list of Base strings to keep
    hour_range  : (min_hour, max_hour) inclusive
    days        : list of day names e.g. ["Monday","Tuesday"]
    search_text : keyword to filter Base column (case-insensitive)

    Returns
    -------
    Filtered DataFrame
    """
    filtered = df.copy()

    # ── Date / Time Range Filter ──────────────────────────────────────────────
    if date_range is not None and len(date_range) == 2:
        start, end = pd.Timestamp(date_range[0]), pd.Timestamp(date_range[1])
        end = end + pd.Timedelta(days=1)   # inclusive end
        filtered = filtered[
            (filtered["Date/Time"] >= start) &
            (filtered["Date/Time"] <  end)
        ]

    # ── Category Filter — Base ────────────────────────────────────────────────
    if bases is not None and len(bases) > 0:
        filtered = filtered[filtered["Base"].isin(bases)]

    # ── Numerical Range Slider — Hour ─────────────────────────────────────────
    if hour_range is not None:
        filtered = filtered[
            (filtered["Hour"] >= hour_range[0]) &
            (filtered["Hour"] <= hour_range[1])
        ]

    # ── Multi-Select Filter — Day of Week ─────────────────────────────────────
    if days is not None and len(days) > 0:
        filtered = filtered[filtered["DayOfWeek"].isin(days)]

    # ── Search / Text Filter — Base keyword ───────────────────────────────────
    if search_text and search_text.strip() != "":
        keyword = search_text.strip().lower()
        filtered = filtered[filtered["Base"].str.lower().str.contains(keyword, na=False)]

    return filtered.reset_index(drop=True)


# ── Utility: KPI helpers ──────────────────────────────────────────────────────
def get_kpis(df: pd.DataFrame) -> dict:
    """Return a dictionary of key metrics for KPI cards."""
    if len(df) == 0:
        return {
            "total": 0, "peak_hour": "N/A", "peak_day": "N/A",
            "top_base": "N/A", "avg_hour": 0
        }
    return {
        "total":      len(df),
        "peak_hour":  df.groupby("Hour").size().idxmax(),
        "peak_day":   df.groupby("DayOfWeek").size().idxmax(),
        "top_base":   df["Base"].value_counts().idxmax(),
        "avg_hour":   round(df["Hour"].mean(), 1),
    }
