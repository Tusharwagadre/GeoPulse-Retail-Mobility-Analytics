"""Small reusable data-quality helpers for GeoPulse."""

import pandas as pd


def profile_dataframe(df: pd.DataFrame) -> dict:
    """Return basic structural and missing-value information for a DataFrame."""
    if not isinstance(df, pd.DataFrame):
        raise TypeError("df must be a pandas DataFrame")
    return {
        "row_count": int(len(df)),
        "column_count": int(len(df.columns)),
        "columns": [str(column) for column in df.columns],
        "duplicate_rows": int(df.duplicated().sum()),
        "missing_by_column": {
            str(column): int(count)
            for column, count in df.isna().sum().items()
        },
        "dtypes": {str(column): str(dtype) for column, dtype in df.dtypes.items()},
    }
