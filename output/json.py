import json
from typing import List

import numpy as np
import pandas as pd
from pandas import Series

from log import logger


def print_json(series: List[Series]) -> None:
    """Imprime uma lista de Series como um objeto JSON.

    Args:
        series: Lista de Series para imprimir
    """
    try:
        # Converte NaN/None para Python None antes da serialização JSON
        cleaned_series = [
            s.replace(np.nan, pd.NA) if hasattr(s, "replace") else s for s in series
        ]

        json_output = []
        for series_obj in cleaned_series:
            # Converte NaN/None para Python None antes da serialização JSON
            clean_series = series_obj.copy()
            mask_nan = pd.isna(clean_series)
            if mask_nan.any():
                clean_series[mask_nan] = None
            json_output.append(json.dumps(clean_series.to_dict()))

        logger.info(json.dumps(json_output, indent=2))
    except Exception:
        logger.error("### FAILED TO PARSE JSON!!! ###")
