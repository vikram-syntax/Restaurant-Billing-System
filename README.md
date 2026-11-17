# Restaurant Billing System (PS No. 41)

## Overview
An interactive command-line Python application designed to manage restaurant orders, validate inputs, apply automated discounts, calculate GST, and generate structured final bills.

## Project Details
* **Project Title:** Restaurant Billing System (Problem Statement No. 41)
* **Name:** Vikram Kumar
* **Class / Section:** BTech CSE AI/ML
* **ERP:** RU-26-00795

## Features
* **Menu Management:** Supports a built-in dictionary menu with predefined items and prices (Dosa, Idli, Thali, Tea).
* **Flexible Ordering:** Allows single-item prompts, multiple comma-separated items, inline quantity shortcuts (e.g., `Order Thali x4, Dosa x2`), and quick bill generation.
* **Robust Validation:** Validates item names against the menu and ensures entered quantities are valid positive whole numbers.
* **Automated Calculations:** 
  * Computes subtotal based on item quantities.
  * Applies a 10% discount automatically if the subtotal exceeds ₹500.
  * Applies a 5% GST on the discounted amount.
  * Generates a clean final grand total.

## Requirements
* Python 3.x (No external libraries or `pip install` packages required; runs entirely on standard built-in Python libraries).

## Steps to Run
1. Open your terminal, command prompt, or VS Code PowerShell.
2. Navigate to the directory containing the script.
3. Run the Python script using the command:
   ```bash
   python restaurant_billing.py
