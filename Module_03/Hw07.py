def first(size, *elements):
    size += len(elements)
    return size

def second(size, **dicts):
    size += len(dicts)
    return size

print(first(5, "first", "second", "third"))
print(first(1, "Alex", "Boris"))
print(second(3, comment_one="first", comment_two="second", comment_third="third"))
print(second(10, comment_one="Alex", comment_two="Boris"))