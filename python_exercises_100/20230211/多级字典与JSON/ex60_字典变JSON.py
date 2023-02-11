"""
把如下字典，变成JSON格式，存入一个文件 p060.json
d = {'employees': [{'firstName': 'John', 'lastName': 'Doe'},
               {'firstName': 'Anna', 'lastName': 'Smith'},
               {'firstName': 'Peter', 'lastName': 'Jones'}],
 'owners': [{'firstName': 'Jack', 'lastName': 'Petter'},
            {'firstName': 'Jessy', 'lastName': 'Petter'}]}
"""
import json

d = {'employees': [{'firstName': 'John', 'lastName': 'Doe'},
                   {'firstName': 'Anna', 'lastName': 'Smith'},
                   {'firstName': 'Peter', 'lastName': 'Jones'}],
     'owners': [{'firstName': 'Jack', 'lastName': 'Petter'},
                {'firstName': 'Jessy', 'lastName': 'Petter'}]}
with open('p060.txt', 'w') as f:
    f.write(json.dumps(d, indent=2))
