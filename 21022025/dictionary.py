dict_ = {
    "myName":"Alex",
    "age":20,
}

print("dict_: ", dict_)

dict_["myName"] = "Olivia"
print("After modified - dict_: ", dict_)

print("getting dict_: age ", dict_.get("age"))

print(dict_.keys())
print(dict_.values())
print(dict_.items())