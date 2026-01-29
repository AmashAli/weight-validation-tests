def validate_weight(weight, min_weight, max_weight):
    """
    Validates a weight against minimum and maximum thresholds.
    Returns one of: 'UNDER', 'OK', 'OVER', 'INVALID'
    """
    if weight is None or weight <= 0:
        return "INVALID"

    if min_weight <= 0 or max_weight <= 0:
        return "INVALID"

    if weight < min_weight:
        return "UNDER"
    elif weight > max_weight:
        return "OVER"
    else:
        return "OK"
