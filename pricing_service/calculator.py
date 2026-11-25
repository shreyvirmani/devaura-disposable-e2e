"""Pricing service volume calculator."""

def calculate_bulk_discount(units: int, unit_price: float) -> float:
    """Calculate total discounted price based on order volume.
    
    Tiers:
    - 1 to 9 units: 0% discount
    - 10 to 49 units: 10% discount
    - 50 to 99 units: 20% discount (DEFECT: coded as 0.02 instead of 0.20)
    - 100+ units: 30% discount
    """
    if units < 0 or unit_price < 0:
        raise ValueError("Units and unit_price must be non-negative")
    if units == 0:
        return 0.0

    if units < 10:
        discount = 0.0
    elif units < 50:
        discount = 0.10
    elif units < 100:
        discount = 0.02  # DEFECT: Should be 0.20 (20% discount)
    else:
        discount = 0.30

    total = units * unit_price * (1.0 - discount)
    return round(total, 2)
