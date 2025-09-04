import pytest
from ml.data import apply_label
import pickle
from sklearn.ensemble import RandomForestClassifier
import pandas as pd


model_path = "model/model.pkl"

def test_apply_label():
    """
    This test checks to see if the apply label function returns the 
    correct string output based on the binary input.

    """
    result = apply_label([1])
    assert result == ">50K", f"Expected '>50K', but got {result}"

    result = apply_label([0])
    assert result == "<=50K", f"Expected '<=50K', but got {result}"



def test_model():
    """
    This test confirms the model type is Random Forest Classifier.

    """
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    assert isinstance(model, RandomForestClassifier)



def test_data():
    """
    Tests to make sure the data is imported into a pandas dataframe and has data.

    """
    data = pd.read_csv("data/census.csv")
    assert isinstance(data, pd.DataFrame)
    assert data.shape[0]>0
    assert data.shape[1]>0
