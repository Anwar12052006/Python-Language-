marks = {
    "Harry": 100,
    "Anwar": 99,
    "Tabassum": 98,
    0: "Harry"
}

print(marks.items())
print(marks.keys())
print(marks.values())

print(marks.get("Harry2")) # print none
print(marks["Harry2"]) # return error