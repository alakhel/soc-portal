# Université de Paris-Cité

installation :
pip install fask, gunicorn

run:
gunicorn app:app

### Brouillon: Call Api

```
fetch('/dashboard', {
      headers: { 'Authorization': `Bearer ${token}` }
    })
    .then(response => response.json())
    .then(data => {
      // Handle the response data
      console.log(data);
    });

// for redirect
        return redirect(url_for('login'))



```

### User Endpoint API

POST /users: Creates a new user.
GET /users: Returns a list of all users.
GET /users/<user_id>: Returns a specific user by ID.
PUT /users/<user_id>: Updates a specific user by ID.
DELETE /users/<user_id>: Deletes a specific user by ID.
