import json

with open('data/test_dataids.json') as f:
    data = json.load(f)

print(len(data))
with open('data/test_dataids.txt','w') as out:
    out.writelines([','.join(line)+'\n' for line in data])