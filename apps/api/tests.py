from django.test import TestCase

# Create your tests here.

per_set = set()
print(type(per_set), per_set)

per_set.add(1)
per_set.add(2)
per_set.add(1)
per_set.add(3)
print(list(per_set))