"""
如下是一个多级字典，也就是说每个字典的KEY的VALUE，也是个数据结构
怎么访问 employees 的第二个人，修改他的 lastName
将值从 Smith 改成 Smooth
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
d['employees'][1]['lastName'] = 'Smoth'
print(d['employees'][1]['lastName'])
