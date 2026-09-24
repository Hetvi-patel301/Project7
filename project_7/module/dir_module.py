import math
def explore_module_attributes(n):
    print(f"Available Attributes in {n} Module:")
    l1 = []
    attributes = dir(n)
    for item in attributes:
        l1.append(item)
    print(l1)