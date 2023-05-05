import glob
import json

def get_file(path):
    f = open(path)
    data = json.load(f)
    f.close()
    return data

total_len = 0
total_years = 0
for file in glob.glob("./saves/*.json"):
    try:
        total_years+=1
        data = get_file(file)
        total_len += len(data)
    
    except:
        continue    

print(total_len, 'across', total_years, 'years')