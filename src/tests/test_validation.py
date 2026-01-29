from src.validation import validate_weight


def test_weight_under_minimum():
    result = validate_weight(weight=5, min_weight=10, max_weight=20)
    assert result == "UNDER"
  
def test_weight_over_maximum():
    result = validate_weight(weight=25, min_weight=10, max_weight=20)
    assert result == "OVER"


def test_weight_within_range():
    result = validate_weight(weight=15, min_weight=10, max_weight=20)
    assert result == "OK"
  
def test_invalid_weight():
    result = validate_weight(weight=0, min_weight=10, max_weight=20)
    assert result == "INVALID"
