"""this a thing to test if something works"""
from models.quote import Quote

quo = Quote(0, 1234, 1, "contado", 3, 0,
            "15/08/2024", 1, 1, 1, "todo en orden")
q = quo.to_dict()
print(q)
