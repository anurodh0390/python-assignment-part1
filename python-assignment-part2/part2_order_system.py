# --- Task 1: Data Setup ---

# Nested Dictionary for Menu
menu = {
    "Paneer Tikka": {"category": "Starters", "price": 240.0, "available": True},
    "Chicken Wings": {"category": "Starters", "price": 310.0, "available": True},
    "Veg Soup": {"category": "Starters", "price": 180.0, "available": False},
    "Butter Chicken": {"category": "Mains", "price": 450.0, "available": True},
    "Dal Tadka": {"category": "Mains", "price": 280.0, "available": True},
    "Garlic Naan": {"category": "Mains", "price": 60.0, "available": True},
    "Gulab Jamun": {"category": "Desserts", "price": 120.0, "available": True},
    "Ice Cream": {"category": "Desserts", "price": 150.0, "available": False}
}

# Dictionary for Inventory (Stock)
inventory = {
    "Paneer Tikka": 10,
    "Chicken Wings": 5,
    "Veg Soup": 0,
    "Butter Chicken": 8,
    "Dal Tadka": 15,
    "Garlic Naan": 25,
    "Gulab Jamun": 20,
    "Ice Cream": 0
}

# Task 1: Menu Exploration 
print("Available Menu")
available_items = []
category_counts = {}

for item, details in menu.items():
    # Check if available is True
    if details["available"]:
        available_items.append(item)
        print(f"- {item} ({details['category']}): ₹{details['price']}")
        
        # Category count update karna
        cat = details["category"]
        category_counts[cat] = category_counts.get(cat, 0) + 1

print(f"\nTotal Available Items: {len(available_items)}")
print(f"Items per Category: {category_counts}")

#Task 2: Order Processing
def process_order(customer_name, order_list):
    print(f"\n--- Processing Order for {customer_name} ---")
    bill = 0
    final_items = []
    
    for item in order_list:
        # Check if item exists, is available, and has stock
        if item in menu and menu[item]["available"] and inventory.get(item, 0) > 0:
            price = menu[item]["price"]
            bill += price
            inventory[item] -= 1 # Stock update
            final_items.append(item)
            print(f"Added {item}: ₹{price}")
        else:
            print(f"Order Failed: {item} is out of stock or unavailable.")
            
    return final_items, bill

# Testing the function
items, total = process_order("Anurodh", ["Paneer Tikka", "Garlic Naan", "Veg Soup"])
print(f"Order Summary: {items} | Total Bill: ₹{total}")

#Task 3: Inventory Alerts
print("\n--- Low Stock Alert (Restock Needed) ---")
low_stock_items = []

for item, stock in inventory.items():
    if stock < 5:
        low_stock_items.append(item)
        print(f"Alert: {item} is low on stock! (Current: {stock})")

if not low_stock_items:
    print("All items are well-stocked.")

#Task 4: Simple Sales Analysis
# Sample sales data (Order IDs and their totals)
sales_log = [240.0, 310.0, 60.0, 450.0, 120.0]

total_revenue = sum(sales_log)
average_order_value = total_revenue / len(sales_log)

print(f"\n--- Sales Summary ---")
print(f"Total Orders Processed: {len(sales_log)}")
print(f"Total Revenue Generated: ₹{total_revenue}")
print(f"Average Order Value: ₹{average_order_value:.2f}")