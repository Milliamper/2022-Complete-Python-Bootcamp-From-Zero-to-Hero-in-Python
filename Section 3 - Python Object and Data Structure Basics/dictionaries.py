# key:value pairs
# szótárakból kulcsok alapján kapjuk meg az egyes elemeket, míg listákból az index helyük alapján
# indexing and slicing

dictionary = {"key1":"value1", "key2":"value2"}
print(dictionary)
print("Első kulcshoz tartozó érték: ", dictionary["key1"])

prices = {"alma":400, "narancs":600, "tej": 640}
print("Alma ára: ", prices["alma"])

d = {"k1":123, "k2":[0,1,2], "k3":{"insideKey":69}}

print(d["k3"]["insideKey"])

d["k4"] = "pörkölt"

print(d)
print(d.keys())
print(d.values())
print(d.items())