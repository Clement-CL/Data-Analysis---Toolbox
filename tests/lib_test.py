# -*- coding: UTF-8 -*-

# Import from standard library
import os
import clem_toolbox
import pandas as pd
# Import from our lib
from clem_toolbox.lib import clean_data
from clem_toolbox.lib import haversine
import pytest


def test_clean_data():
    datapath = os.path.dirname(os.path.abspath(clem_toolbox.__file__)) + '/data'
    df = pd.read_csv('{}/data.csv.gz'.format(datapath))
    first_cols = ['id', 'civility', 'birthdate', 'city', 'postal_code', 'vote_1']
    assert list(df.columns)[:6] == first_cols
    assert df.shape == (999, 142)
    out = clean_data(df)
    assert out.shape == (985, 119)

def test_haversine():
    test_result = 70.00789153218594
    assert haversine(48.865070, 2.380009, 48.235070, 2.393409) == test_result
