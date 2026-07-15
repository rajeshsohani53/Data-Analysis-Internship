countries = ["India", "USA", "UK", "Germany", "Japan", "Australia"]
print("Original list:", countries)

countries_copy = countries.copy()
print("Copied list:", countries_copy)
print("Are they equal?", countries == countries_copy)
print("Are they the same object?", countries is countries_copy)
