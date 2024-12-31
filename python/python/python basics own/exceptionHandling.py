#Create Classes for Product, Cart, and Order:

     # Product: Holds details about the product like name, price, and stock.
     # Cart: Handles adding products and calculating the total price.
     # Order: Handles the checkout process and simulates payment.
     # Exception Handling:

     # Invalid Price: When a non-numeric price is entered, raise a ValueError.
     # Insufficient Stock: If a user attempts to add more products than available, raise an InventoryError.
     # Invalid Payment: Handle errors like insufficient funds or payment timeouts with custom exceptions.