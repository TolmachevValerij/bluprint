from requests import get, post, delete

print(get('http://localhost:5000/api/v2/users').json())
print(get('http://localhost:5000/api/v2/users/5').json())
print(get('http://localhost:5000/api/v2/users/52').json())
print(get('http://localhost:5000/api/v2/users/q').json())

print(post('http://localhost:5000/api/v2/users').json())
print(post('http://localhost:5000/api/v2/users', json={'name': 'Sonya'}).json())
print(post('http://localhost:5000/api/v2/users', json={'name': 'Sonya', 'position': 'junior programmer',
                                                       'surname': 'Wolf', 'age': 17, 'address': 'module_3',
                                                       'speciality': 'computer sciences',
                                                       'hashed_password': 'wolf', 'email': 'wolf@mars.org'}).json())

print(delete('http://localhost:5000/api/v2/users/999').json())
print(delete('http://localhost:5000/api/v2/users/10').json())
