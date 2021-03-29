from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import builder
import mysql.connector
from collections import OrderedDict




class loginPage(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        

        # db = mysql.connector.connect(
        #     host = "localhost",
        #     user = "devBase",
        #     password = "1234",
        #     database = "posdb"
            
        # )
        # cursor = db.cursor()
        # #query = "CREATE TABLE users (first_name VARCHAR(20) NOT NULL, last_name VARCHAR(20) NOT NULL, username VARCHAR(20) NOT NULL, password int UNSIGNED NOT NULL, userId int PRIMARY KEY AUTO_INCREMENT)"

        # cursor.execute("INSERT INTO users (first_name, last_name, username, password) VALUES (%s,%s,%s,%s)", ("John", "Doe", "jonny", 1234))
        # cursor.execute("INSERT INTO users (first_name, last_name, username, password) VALUES (%s,%s,%s,%s)", ("Jane", "Doe", "janey", 2345))
        # cursor.execute("INSERT INTO users (first_name, last_name, username, password) VALUES (%s,%s,%s,%s)", ("Peter", "Stone", "pete", 3456))
        # cursor.execute("INSERT INTO users (first_name, last_name, username, password) VALUES (%s,%s,%s,%s)", ("David", "Shepherd", "dave", 4567))
        # cursor.execute("INSERT INTO users (first_name, last_name, username, password) VALUES (%s,%s,%s,%s)", ("Mattew", "Preacher", "matt", 5678))
        # db.commit()

        
        users = loginPage.login()
        print(users)

        username = self.ids.username_inp.text
        password = self.ids.password_inp.text
        text_info = self.ids.disp.text

        

    def login():

        user_db = mysql.connector.connect(
            host = "localhost",
            user = "devBase",
            password = "1234",
            database = "posdb"
            
        )
        #ordered dictionary -- will contain the data table
        _users = OrderedDict()
        _users["first_name"] = {}
        _users["last_name"] = {}
        _users["username"] = {}
        _users["password"] = {}
        _users["userId"] = {}

        first_name = []
        last_name = []
        username = []
        password = []
        userId = []

        u_cursor = user_db.cursor()
        query = "SELECT * FROM users"
        u_cursor.execute(query)
        users = u_cursor.fetchall()
        for user in users:
            first_name.append(user[0])
            last_name.append(user[1])
            username.append(user[2])
            password.append(user[3])
            userId.append(user[4])

        table_idx = len(first_name)
        idx = 0
        while table_idx > idx:
            _users["first_name"][idx] = first_name[idx]
            _users["last_name"][idx] = last_name[idx]
            _users["username"][idx] = username[idx]
            _users["password"][idx] = password[idx]
            _users["userId"][idx] = userId[idx]
            idx += 1

        return _users

    


class LoginApp(App):
    def build(self):
        return loginPage()

if __name__ == "__main__":
    LP = LoginApp()
    LP.run()