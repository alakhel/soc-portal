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
