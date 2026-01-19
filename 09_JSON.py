import json

x= '{"name": "John", "age": 30, "city": "New York"}'

#convert JSON into Python:
y = json.loads(x)

print(y)
print(type(y))



# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)
print(type(y))


print(json.dumps({"name": "John", "age": 30}))
print((json.dumps(["apple", "bananas"])))