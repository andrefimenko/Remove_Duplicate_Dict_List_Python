raw_data = [{"key1": "value1"}, {"key2": "value2"}, {"key1": "value1"}, {"key1": "value2"}]

res = [dict(j) for j in {tuple(i.items()) for i in raw_data}]

print(res)