# Université de Paris-Cité

#### installation :

- pip install -r requirements.txt
- apt install sqlite3

#### run:

- gunicorn app:app -b 0.0.0.0:8000
- gunicorn app:app -b 0.0.0.0:8000 -D

### Brouillon: Call Api

```Javascript
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

- POST /users: Creates a new user.
- GET /users: Returns a list of all users.
- GET /users/<user_id>: Returns a specific user by ID.
- PUT /users/<user_id>: Updates a specific user by ID.
- DELETE /users/<user_id>: Deletes a specific user by ID.

### Machine Endpoint API

- GET /machines: Retrieve a list of all machines in the database.
- GET /machines/:id: Retrieve a specific machine by ID.
- POST /machines: Create a new machine.
- PUT /machines/:id: Update an existing machine by ID.
- DELETE /machines/:id: Delete a machine by ID.

---

### Tasks:

#### RBAC :

https://flask-rbac.readthedocs.io/en/latest/
brouillon_roles.py

- add rbac to backend
- protect admin routes
- hide admin forms in frontend (ex: user should not see adminStuff)

#### Myprofile API:

- should contains user's details & reset password form.
- create api endpoint using the code below and Chatgpt
- create the correspendant HTML page to consume the API

```
  #define the func
  @jwt.user_identity_loader
  def user_identity_lookup(user):
    return user.id

  #call the func
  @app.route('/myprofile', methods=['GET'])
  def myprofile():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    return jsonify(user)
```

#### Correction de l'UX

- faire des tests sur le frontend et corrgier les beugs UX;
- example: clique sur button ajouter, puis faut faire F5 pour avoir les données
- example: en cas de message d'erreur, faut l'afficher sur l'interface
