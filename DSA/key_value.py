dicti = {
    "k1": "v1",
    "k2": "v2"
}

print(dicti)

dicti["k3"] = "v3"

print(dicti)

dicti["k2"]="v4"

print(dicti)


# if a key does not exists, get method returns None or the default value i.e not found in our case but if i try dicti["k5"], it will return key error.
v5 = dicti.get('k5',"not found")
print(v5)

# v5 = dicti['k5']
# print(v5)


dicti.update({"k5":"v5"})

print("v1" in dicti)


pol_eng_dictionary = {
    "zamek": "castle",
    "woda": "water",
    "gleba": "soil"
    }

copy_dictionary = pol_eng_dictionary.copy()

print(pol_eng_dictionary)
print(copy_dictionary)