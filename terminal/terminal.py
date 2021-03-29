from os import name
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
import mysql.connector
from collections import OrderedDict


#Builder.load_file("terminal.kv")

class TerminalPage(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # self.ids.product_view.data = [{'text': str(x)} for x in range(100)]
    
        db = mysql.connector.connect(
                host = "localhost",
                user = "devBase",
                password = "1234",
                database = "posdb"
                
        )
        cursor = db.cursor()

        # An ordered dictionary that will hold the data table
        _products = OrderedDict()
        _products["name"] = {}
        _products["price"] = {}
        _products["category"] = {}
        _products["stock"] = {}
        # lists to temporarily hold the query results
        name = []
        price = []
        category = []
        stock = []
        query = "SELECT * FROM products"
        cursor.execute(query)
        products = cursor.fetchall()
        for item in products:
            name.append(item[0])
            price.append(item[1])
            category.append(item[2])
            stock.append(item[3]) 
        #create an index and populate the ordered dict
        num = 0
        col_len = len(name)
        while col_len > num:
            _products["name"][num] = name[num]
            _products["price"][num] = price[num]
            _products["category"][num] = category[num]
            _products["stock"][num] = stock[num]
            num +=1

        print(_products)

        products = _products
        cols_title = [x for x in products.keys()]
        rows_length = len(products[cols_title[1]])
        dataTable = []
        for c in cols_title:
            dataTable.append({"text": str(c),'size_hint_y':None,'height':50,'bcolor':(.06,.45,.45,1)})
        
        for idx in range(rows_length):
            for c in cols_title:
                dataTable.append({"text": str(products[c][idx]),"size_hint_y":None, "height":50, "color":(1,1,1,1)})

        self.ids.product_view.data = dataTable

   

   


class TerminalApp(App):
    def build(self):
        return TerminalPage()

if __name__ == "__main__":
    TA = TerminalApp()
    TA.run()




 #cursor.execute("CREATE TABLE products (name VARCHAR(20) NOT NULL, price int UNSIGNED NOT NULL, category VARCHAR(20) NOT NULL, stock int UNSIGNED NOT NULL, userId int PRIMARY KEY AUTO_INCREMENT)")
    #cursor.execute("ALTER TABLE products DROP product_id")

    # cursor.execute("INSERT INTO products (name, price, category, stock) VALUES (%s,%s,%s,%s)", ("Jane", 490, "Doe", 20))
    # cursor.execute("INSERT INTO products (name, price, category, stock) VALUES (%s,%s,%s,%s)", ("mouse", 250, "computer assesory", 10))
    # cursor.execute("INSERT INTO products (name, price, category, stock) VALUES (%s,%s,%s,%s)", ("Peter", 490, "Stone", 20))
    # cursor.execute("INSERT INTO products (name, price, category, stock) VALUES (%s,%s,%s,%s)", ("David", 490, "Shepherd", 20))
    # cursor.execute("INSERT INTO products (name, price, category, stock) VALUES (%s,%s,%s,%s)", ("Mattew", 490, "Preacher", 20))
    # cursor.execute("INSERT INTO products (name, price, category, stock) VALUES (%s,%s,%s,%s)", ("John", 490, "Doe", 20))
    # cursor.execute("INSERT INTO products (name, price, category, stock) VALUES (%s,%s,%s,%s)", ("Jane", 490, "Doe", 20))
    # cursor.execute("INSERT INTO products (name, price, category, stock) VALUES (%s,%s,%s,%s)", ("Peter", 490, "Stone", 20))
    # cursor.execute("INSERT INTO products (name, price, category, stock) VALUES (%s,%s,%s,%s)", ("David", 490, "Shepherd", 20))
    # cursor.execute("INSERT INTO products (name, price, category, stock) VALUES (%s,%s,%s,%s)", ("Mattew", 490, "Preacher", 20))
    # cursor.execute("INSERT INTO products (name, price, category, stock) VALUES (%s,%s,%s,%s)", ("John", 490, "Doe", 20))
    # cursor.execute("INSERT INTO products (name, price, category, stock) VALUES (%s,%s,%s,%s)", ("Jane", 490, "Doe", 20))
    # cursor.execute("INSERT INTO products (name, price, category, stock) VALUES (%s,%s,%s,%s)", ("Peter", 490, "Stone", 20))
    # cursor.execute("INSERT INTO products (name, price, category, stock) VALUES (%s,%s,%s,%s)", ("David", 490, "Shepherd", 20))
    # cursor.execute("INSERT INTO products (name, price, category, stock) VALUES (%s,%s,%s,%s)", ("Mattew", 490, "Preacher", 20))
    # cursor.execute("INSERT INTO products (name, price, category, stock) VALUES (%s,%s,%s,%s)", ("John", 490, "Doe", 20))
    # cursor.execute("INSERT INTO products (name, price, category, stock) VALUES (%s,%s,%s,%s)", ("Jane", 490, "Doe", 20))
    # cursor.execute("INSERT INTO products (name, price, category, stock) VALUES (%s,%s,%s,%s)", ("Peter", 490, "Stone", 20))
    # cursor.execute("INSERT INTO products (name, price, category, stock) VALUES (%s,%s,%s,%s)", ("David", 490, "Shepherd", 20))
    # cursor.execute("INSERT INTO products (name, price, category, stock) VALUES (%s,%s,%s,%s)", ("Mattew", 490, "Preacher", 20))
    # cursor.execute("INSERT INTO products (name, price, category, stock) VALUES (%s,%s,%s,%s)", ("John", 490, "Doe", 20))
    # cursor.execute("INSERT INTO products (name, price, category, stock) VALUES (%s,%s,%s,%s)", ("Jane", 490, "Doe", 20))
    # cursor.execute("INSERT INTO products (name, price, category, stock) VALUES (%s,%s,%s,%s)", ("Peter", 490,"Stone", 20))
    # cursor.execute("INSERT INTO products (name, price, category, stock) VALUES (%s,%s,%s,%s)", ("David", 490, "Shepherd", 20))
    # cursor.execute("INSERT INTO products (name, price, category, stock) VALUES (%s,%s,%s,%s)", ("Mattew", 490, "Preacher", 20))