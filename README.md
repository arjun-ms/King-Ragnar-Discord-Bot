
<h1 align="center">
    King Ragnar Discord Bot
</h1>

### To-Do
- [x] greet a newly joined member in a channel (random message)
- [x] while adding a reaction to a message send a message to a channel (<user> gave reaction to <user>)
- [x] parameterized command (eg - !role <role_name>), create a role named the parameter recieved and assign it to the user.
- [x] using a parameterized command(eg - !register <name>) insert the name to database, if same name tries to register again send error message to channel.
- [x] with a role restricted command retrieve all names in the database ( eg - !names)

#### Commands
- `!register yourname` - to add yourname to the db
- `!names` - to list all names in db(requires `nikhil` role)
- `!role rolename` - to get the specified role  
 
**MySQL** To Create Table
```
CREATE TABLE users (
id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(255)
)
```