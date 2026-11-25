"""Order pipeline checkout processor."""
from inventory_service.stock import reserve_inventory

def process_checkout(order_id: str, sku: str, quantity: int) -> dict:
    """Process an order checkout.
    
    DEFECT:
    1. Calls reserve_inventory with reversed positional arguments: (quantity, sku).
    2. Checks res.get("is_reserved") instead of res.get("status") == "CONFIRMED".
    """
    # DEFECT: Positional argument mismatch (quantity passed as sku, sku passed as quantity)
    res = reserve_inventory(quantity, sku)  # Should be reserve_inventory(sku, quantity)
    
    if not res.get("status") == "CONFIRMED":
        return {"order_id": order_id, "status": "FAILED", "reason": "Inventory reservation failed"}
        
    return {
        "order_id": order_id,
        "sku": sku,
        "quantity": quantity,
        "status": "COMPLETED",
    }
