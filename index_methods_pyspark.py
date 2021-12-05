"""
Multilateral methods using native PySpark functionality. 

Provides the following function:

* :func:`multilateral_methods_pyspark`
"""
from typing import Sequence, List, Optional

import pandas as pd
import numpy as np
from pyspark.sql import (
    DataFrame as SparkDF,
    functions as F,
)

from helpers_pyspark import _weights_calc
from multilateral_methods import time_dummy_pyspark
from wls import wls

__author__ = ['Dr. Usman Kayani']

def multilateral_methods_pyspark(
    df: SparkDF,
    method: str,
    price_col: str = 'price',
    quantity_col: str = 'quantity',
    date_col: str = 'month',
    product_id_col: str = 'id',
    characteristics: Optional[Sequence[str]] = None,
) -> pd.DataFrame:
    """
    Calculate multilateral index numbers in PySpark.

    Currently supported: Time Product Dummy (TPD) and Time Hedonic Dummy (TDH).

    Parameters
    ----------
    df : Spark DataFrame
        Contains price and quantity columns, a time series column, and a product
        ID column as a minimum. A characteristics column should also be present
        for hedonic methods.
    price_col : str, defaults to 'price'
        User-defined name for the price column.
    quantity_col : str, defaults to 'quantity'
        User-defined name for the quantity column.
    date_col : str, defaults to 'date'
        User-defined name for the date column.
    product_id_col: str, defaults to 'id'
        User-defined name for the product id column.
    characteristics: list of str, defaults to None
        The names of the characteristics columns.
    method: str
        Options: {TPD', 'TDH'}
        The multilateral method to apply.

    Returns
    -------
    pd.DataFrame
        A pandas dataframe of the index values.
    """
    if method not in {'TPD', 'TDH'}:
        raise ValueError(
            "Invalid method or not implemented yet."
        )
    
    # Get timeseries for output index.
    time_series = [i.month for i in df.select(date_col).distinct().collect()]
    
    # Calculate weights for each item in each period.
    df = df.withColumn(
        'weights',
        _weights_calc(price_col, quantity_col, date_col)
    )
      
    if method == 'TPD':
        index_vals = time_dummy_pyspark(
            df,
            len(time_series),
            price_col,
            date_col,
            product_id_col,
        )
    elif method == 'TDH':
        if not characteristics:
            raise ValueError(
                "Characteristics required for TDH."
            )
        else: 
            index_vals = time_dummy_pyspark(
                df,
                len(time_series),
                price_col,
                date_col,
                product_id_col,
                characteristics,
            )

    return (
        pd.DataFrame(
            index_vals, 
            index=time_series
        )
        .rename({0: 'index_value'}, axis=1)
    )

