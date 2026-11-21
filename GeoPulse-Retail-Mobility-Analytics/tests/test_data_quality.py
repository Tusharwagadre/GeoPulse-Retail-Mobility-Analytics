import pandas as pd

from src.data_quality import profile_dataframe


def test_profile_dataframe_reports_basic_quality_metrics():
    df = pd.DataFrame({"area": ["A", "A", None], "visits": [1, 1, 3]})
    result = profile_dataframe(df)

    assert result["row_count"] == 3
    assert result["column_count"] == 2
    assert result["duplicate_rows"] == 1
    assert result["missing_by_column"]["area"] == 1
