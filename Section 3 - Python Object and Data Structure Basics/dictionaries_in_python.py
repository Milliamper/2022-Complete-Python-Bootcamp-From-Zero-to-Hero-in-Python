# unordered mapping for storing objects
# kulcs:érték párokat tárol
# arra való, hogy index nélkül tudjunk objektumokat megkapni

my_dictionary = {"key1": "value1", "key2": "value2"}
print(my_dictionary)

print(my_dictionary["key1"])

prices_lookup = {"alma": "300 Ft/kg", "csoki": 600}

# add new key:value pair - ugyan így lehet felülírni is
prices_lookup["körte"] = 450
print(prices_lookup)

d = {"k1": 123, "k2": [0, 1, 2], "k3": {"insideKey": 100}}
print(d["k3"]["insideKey"])

my_dict = {"key1":["a","b","c"]}
make_c_upper = my_dict["key1"][2].upper()
print(make_c_upper)

print(prices_lookup.keys())
