"""Math service calculator implementation."""

def calculate_discount(price: float, tier: str) -> float:
    """Calculate discounted price based on customer tier.
    
    Tiers:
    - 'standard': 5% discount
    - 'premium': 15% discount
    - 'enterprise': 25% discount
    """
    if price < 0:
        raise ValueError("Price cannot be negative")
    
    if tier == "standard":
        discount = 0.05
    elif tier == "premium":
        discount = 0.15
    elif tier == "enterprise":
        discount = 0.25  # FIXED: Enterprise customers receive 25% discount
    else:
        discount = 0.0
        
    return round(price * (1.0 - discount), 2)
