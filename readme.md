# Université de Paris-Cité

pip install fask
pip install gunicorn
gunicorn app:app

### Call Api

```
fetch('/dashboard', {
      headers: { 'Authorization': `Bearer ${token}` }
    })
    .then(response => response.json())
    .then(data => {
      // Handle the response data
      console.log(data);
    });
```

### User Endpoint API

POST /users: Creates a new user.
GET /users: Returns a list of all users.
GET /users/<user_id>: Returns a specific user by ID.
PUT /users/<user_id>: Updates a specific user by ID.
DELETE /users/<user_id>: Deletes a specific user by ID.

#

sqlite3 database.db

CREATE TABLE user (
id INTEGER PRIMARY KEY,
prenom TEXT,
nom TEXT,
login TEXT,
password TEXT,
groupe TEXT
);
