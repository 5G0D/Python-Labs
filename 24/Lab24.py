import json
from array import *

res = []

with open('in.json','r') as f:
    a = f.read()
    data = json.loads(a)
    for d in data:
        if d['completed'] == 1:
            flag = True
            for o in res:
                if d['userId'] == o['userId']:
                    flag = False
                    o['task_completed'] += 1
            if flag:
                res.append( { 'task_completed' : 1,
                              'userId' :  d['userId']})  
with open ('out.json','w') as out:
    b = json.dump(res, out,indent=3)