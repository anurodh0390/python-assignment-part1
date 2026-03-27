# Python Assignment - Part 2: Restaurant Menu & Order Management

This repository contains a Python-based Restaurant Management System that utilizes advanced data structures like nested dictionaries and lists to handle menu exploration, order processing, and inventory tracking.

## 📁 Project Structure
- `part2_order_system.py`: The main script containing the logic for menu management and sales analysis.
- `README.md`: Documentation for the project (this file).

## 🚀 Tasks Implemented

### Task 1: Menu Exploration
- Managed a nested dictionary containing item categories, prices, and availability.
- Filtered and displayed only available items that are currently in stock.
- Calculated the number of items available per category (Starters, Mains, Desserts).

### Task 2: Order Processing
- Created a robust function to handle customer orders.
- Implemented logic to verify item existence, availability, and real-stock levels before processing.
- Automatically updated the `inventory` (stock) levels after each successful order.

### Task 3: Inventory Management & Alerts
- Developed an automated alerting system to identify items with low stock (threshold < 5).
- Provided clear notifications for items that need immediate restocking.

### Task 4: Sales Analysis
- Analyzed sales logs to calculate total revenue generated.
- Calculated the Average Order Value (AOV) to understand customer spending patterns.

## 🛠️ Concepts Used
- **Nested Dictionaries**: To store complex item data.
- **Dictionary Methods**: Using `.get()`, `.items()`, and `.keys()`.
- **List Comprehension**: For efficient data filtering.
- **Functional Programming**: Encapsulating logic within reusable functions.

## 🧑‍💻 Author
**Anurodh Dhanwik**