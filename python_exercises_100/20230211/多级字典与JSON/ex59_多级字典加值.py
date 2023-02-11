"""
如下是一个多级字典，也就是说每个字典的KEY的VALUE，也是个数据结构
怎么给 employees 添加一个人：'firstName': 'Albert', 'lastName': 'Bert'
d = {"employees": [{"firstName": "John", "lastName": "Doe"},
                   {"firstName": "Anna", "lastName": "Smith"},
                   {"firstName": "Peter", "lastName": "Jones"}],
     "owners": [{"firstName": "Jack", "lastName": "Petter"},
                {"firstName": "Jessy", "lastName": "Petter"}]}
"""
d = {"employees": [{"firstName": "John", "lastName": "Doe"},
                   {"firstName": "Anna", "lastName": "Smith"},
                   {"firstName": "Peter", "lastName": "Jones"}],
     "owners": [{"firstName": "Jack", "lastName": "Petter"},
                {"firstName": "Jessy", "lastName": "Petter"}]}
d["employees"].append({'firstName': 'Albert', 'lastName': 'Bert'})
print(d['employees'])