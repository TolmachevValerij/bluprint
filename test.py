from requests import get, post, delete


print(post('http://localhost:5000/api/v2/jobs', json={'job': 'teacher', 'work_size': '12',
                                                       'collaborators': '2', 'start_date': '2020-03-14 13:28:09', 'end_date': '2025-03-14 13:28:09',
                                                       'is_finished': 'True',
                                                       'team_leader': '1', 'category': 'cultury'}).json())

print(post('http://localhost:5000/api/v2/jobs').json())
print(post('http://localhost:5000/api/v2/jobs/1').json())
print(delete('http://localhost:5000/api/v2/jobs/3').json())
