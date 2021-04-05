nestedObject = {"a": {"b": {"c": "d"}}}
nestedObject2 = {"x": {"y": {"z": "a"}}}

def getValue(nestedObject, key):
  keys = key.split('/')
  value = nestedObject
  for subKey in keys:
    if isinstance(value, dict) and (subKey in value):
      value = value[subKey]
    else:
      raise Exception("Given key is not valid")


  return value


print(getValue(nestedObject, "a/b/c"))
print(getValue(nestedObject, "a/b"))
print(getValue(nestedObject, "a"))
print(getValue(nestedObject2, "x/y/z"))
print(getValue(nestedObject2, "x/y"))
print(getValue(nestedObject2, "x"))
