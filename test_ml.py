import pytest
from ml.data import apply_label
import pickle
from sklearn.ensemble import RandomForestClassifier

# TODO: add necessary import

# TODO: implement the first test. Change the function name and input as needed
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


# TODO: implement the second test. Change the function name and input as needed
def test_model():
    """
    # add description for the second test
    """
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    assert isinstance(model, RandomForestClassifier)


# TODO: implement the third test. Change the function name and input as needed
def test_three():
    """
    # add description for the third test
    """
    # Your code here
    pass
