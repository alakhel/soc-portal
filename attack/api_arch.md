# 1. Home
curl -X GET http://127.0.0.1:8000/

# 2. Create user
curl -X POST http://127.0.0.1:8000/api/users -H 'Content-Type: application/json' -d '{"prenom": "John", "nom": "Doe", "username": "admin1", "password": "mypassword", "groupe": "admin"}'

# 3. List users
curl -X GET http://127.0.0.1:8000/api/users

# 4. Get user by ID
curl -X GET http://127.0.0.1:8000/api/users/{{user_id}}

# 5. Update user by ID
curl -X PUT http://127.0.0.1:8000/api/users/{{user_id}} -H 'Content-Type: application/json' -d '{"prenom": "Jane", "nom": "Doe", "username": "admin1", "password": "P@ssword", "groupe" : "user"}'

# 6. Delete user by ID
curl -X DELETE http://127.0.0.1:8000/api/users/{{user_id}}

# 7. Create computer
curl -X POST http://127.0.0.1:8000/api/computers -H 'Content-Type: application/json' -d '{"hostname": "PC1", "ip": "192.168.1.2", "groupe": "workstation"}'

# 8. List computers
curl -X GET http://127.0.0.1:8000/api/computers

# 9. Get computer by ID
curl -X GET http://127.0.0.1:8000/api/computers/{{computer_id}}

# 10. Update computer by ID
curl -X PUT http://127.0.0.1:8000/api/computers/{{computer_id}} -H 'Content-Type: application/json' -d '{"hostname": "PC2", "ip": "192.168.1.3", "groupe": "Blue"}'

# 11. Delete computer by ID
curl -X DELETE http://127.0.0.1:8000/api/computers/{{computer_id}}

# 12. Login
curl -X POST http://127.0.0.1:8000/api/login -H 'Content-Type: application/json' -d '{"username": "admin1", "password": "newpassword123"}'

# 14. Get user
curl -X GET http://127.0.0.1:8000/api/user -H 'Authorization: Bearer {{AT}}'