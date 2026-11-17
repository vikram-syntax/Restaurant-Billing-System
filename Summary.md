# Project Summary: Restaurant Billing System (PS No. 41)

## 1. Project Overview
The **Restaurant Billing System (Problem Statement No. 41)** is a Python-based command-line application that automates restaurant order-taking and billing. Built using Python dictionaries and lists, it manages a predefined menu (`Dosa`, `Idli`, `Thali`, `Tea`), accepts orders in multiple formats, validates user inputs, and generates a structured receipt.

The billing engine calculates the subtotal, applies a **10% discount** on orders exceeding **₹500**, adds **5% GST** on the discounted amount, and displays the formatted grand total.

---

## 2. Difficulties Faced & Solutions

### Difficulty 1: Handling Multiple Input Formats
* **Challenge:** Supporting both step-by-step inputs (entering the item name, then quantity separately) and single-line multi-item orders (e.g., `Order Thali x4, Dosa x2, Tea x2`) without breaking the input loop.
* **Solution:** Added string preprocessing in the main loop to strip the optional `"order "` prefix, split entries by commas (`,`), and separate item names from quantities using `"x"` (case-insensitive). Used an `inline_order` boolean flag to toggle separate quantity prompts.

### Difficulty 2: Input Validation Without Crashing
* **Challenge:** Non-numeric strings (`"abc"`), zero/negative numbers, or misspelled items caused `ValueError` or `KeyError` crashes during `int()` casting or dictionary lookups.
* **Solution:**
  * Normalized item inputs via `.strip().capitalize()` and checked `if item_name not in menu:` before price lookup.
  * Validated quantities using `.isdigit()` inside a nested `while True` loop to safely reject negative, zero, or non-numeric entries until a valid positive integer (`>= 1`) is entered.

### Difficulty 3: Discount & GST Calculation Order
* **Challenge:** Ensuring the **5% GST** is applied *after* deducting the **10% discount**, and dynamically formatting the receipt depending on whether a discount was triggered.
* **Solution:** Modularized billing logic into dedicated functions (`calculate_subtotal`, `calculate_discount`, `calculate_gst`, `calculate_total`), passing the discounted subtotal directly to `calculate_gst()`, and used conditional formatting (`:.2f`) for clean output alignment.

---

## 3. Working Test Cases
* **Test Case 1:** Standard Single-Item Ordering & Basic Billing
* **Test Case 2:** Subtotal Exceeding ₹500 (10% Discount + 5% GST Applied)
* **Test Case 3:** Input Validation (Invalid Item Name, Zero/Negative & Non-Numeric Quantities)
* **Test Case 4:** Multi-Item Inline Ordering (`Order Thali x4, Dosa x2, Tea x2`)
