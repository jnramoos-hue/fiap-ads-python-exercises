# Importing the module that handles driver's licenses
import driver_licenses

# Asking the user for the category
typed_category = input("Enter the driver's license category: ")

# Using the validade_category method to check if what was typed is valid
driver_licenses.validate_category(typed_category)

# Including a new fake category at runtime
driver_licenses.categories.append("SPECIAL")

# Using the validade_category method to check whether what was typed is valid
driver_licenses.validate_category(typed_category)

