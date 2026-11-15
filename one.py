# PS No. 41 - Restaurant Billing System

# 1. Menu in a dictionary and ordered items in a list
menu = {
    "Dosa": 80,
    "Idli": 40,
    "Thali": 150,
    "Tea": 20
}

ordered_items = []

# 2. Functions to calculate subtotal, discount, GST and grand total
def calculate_subtotal(orders):
    subtotal = 0
    for item in orders:
        subtotal = subtotal + item[2]
    return subtotal

def calculate_discount(subtotal):
    if subtotal > 500:
        return subtotal * 0.10
    else:
        return 0.0

def calculate_gst(subtotal, discount):
    after_discount = subtotal - discount
    return after_discount * 0.05

def calculate_total(subtotal, discount, gst):
    return (subtotal - discount) + gst


# 3. Starting Heading & Menu Format
print("=========================================")
print("       RESTAURANT BILLING SYSTEM         ")
print("=========================================")
print("Available Menu: Dosa Rs.80 | Idli Rs.40 | Thali Rs.150 | Tea Rs.20")
print("Type 'Generate bill' (or press Enter) when finished.\n")

# 4. Main loop to take inputs according to all 4 Test Cases
while True:
    user_input = input("Order item: ").strip()
    
    # Exit loop and print bill if user types 'Generate bill' or presses Enter after ordering
    if user_input.lower() == "generate bill" or (user_input == "" and len(ordered_items) > 0):
        break
        
    if user_input == "":
        continue

    # Check if user typed "Order Thali x4, Dosa x2, Tea x2" (Test Case 4)
    if user_input.lower().startswith("order "):
        user_input = user_input[6:].strip()

    # Split by comma in case multiple items are entered at once
    parts = user_input.split(",")
    
    for part in parts:
        part = part.strip()
        if part == "":
            continue
            
        # Check if quantity is written with 'x' like "Thali x4" (Test Case 4)
        if "x" in part.lower():
            clean_part = part.replace("X", "x")
            words = clean_part.split("x")
            item_name = words[0].strip().capitalize()
            qty_str = words[1].strip()
            inline_order = True
        else:
            item_name = part.capitalize()
            qty_str = ""
            inline_order = False
            
        # Test Case 3(a): Validate item name
        if item_name not in menu:
            print("Item not on the menu. Available: Dosa, Idli, Thali, Tea")
            continue
            
        # Loop until a valid quantity is entered
        while True:
            if qty_str == "":
                if len(parts) > 1:
                    qty_str = input(f"Quantity for {item_name}: ").strip()
                else:
                    qty_str = input("Quantity: ").strip()
                
            # Check if input is a whole number
            if qty_str.startswith("-"):
                is_number = qty_str[1:].isdigit()
            else:
                is_number = qty_str.isdigit()
                
            # Test Case 3(c): Quantity is 'abc' or not a whole number
            if not is_number or qty_str == "":
                print("Invalid quantity. Enter a whole number.")
                qty_str = ""
                continue
                
            qty = int(qty_str)
            
            # Test Case 3(b): Quantity is 0 or negative
            if qty < 1:
                print("Quantity must be at least 1.")
                qty_str = ""
                continue
                
            break
            
        # Calculate item amount and save to list
        amount = menu[item_name] * qty
        ordered_items.append([item_name, qty, amount])
        
        # Test Case 1: Print "Dosa x2 added | Amount: 160" for normal input
        if not inline_order:
            print(f"{item_name} x{qty} added | Amount: {amount}")


# 5. Print the Final Bill with Heading & Neat Formatted Layout
if len(ordered_items) > 0:
    print("\n-----------------------------------------")
    print("                FINAL BILL               ")
    print("-----------------------------------------")
    
    sub = calculate_subtotal(ordered_items)
    disc = calculate_discount(sub)
    gst = calculate_gst(sub, disc)
    total = calculate_total(sub, disc, gst)
    
    # Print the item breakdown line if multiple items were ordered (Test Case 4)
    if len(ordered_items) > 1:
        summary = []
        for item in ordered_items:
            summary.append(f"{item[0]} x{item[1]} = {item[2]}")
        print(" | ".join(summary))
        
    # Match exact output format of Test Case 2 and Test Case 4
    if disc > 0:
        print(f"Subtotal: {sub} | Discount (10%): {disc:.2f}")
        print(f"GST (5%): {gst:.2f}")
        print(f"Grand Total: {total:.2f}")
    else:
        print(f"Subtotal: {sub} | Discount: {disc:.2f}")
        print(f"GST (5%): {gst:.2f} | Grand Total: {total:.2f}")
        
    print("-----------------------------------------")
else:
    print("\nNo items ordered. Bill cannot be generated.")