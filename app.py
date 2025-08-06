from flask import Flask,render_template,jsonify,request
from flask_mysqldb import MySQL




# @app.route('/')
# def hello_world():
#     return 'Hello World'


app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'roottoor'
app.config['MYSQL_DB'] = 'thanu_ece'
mysql = MySQL(app)
   

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/myweb',methods=['GET'])
def myweb():
   return render_template("index.html")



@app.route('/notmyName')
def printMyname():
 return "your name "

@app.route('/home')
def loadHomeHtml():
     return render_template("home.html")



@app.route('/about')
def loadaboutHtml():
 return render_template("about.html")
  
@app.route('/contact')
def loadcontactHtml():
 return render_template("contact.html")

@app.route('/user_detail')
def userDetail():
   sql = "SELECT * FROM user"
   cur = mysql.connection.cursor()
   cur.execute(sql)
   results = cur.fetchall()
   cur.close()
   return jsonify (results)

# @app.route("/add",methods=["POST"])
# def addUser():
#    id = request.form['id']
#    email = request.form['email']
#    name = request.form['name']
#    cur = mysql.connection.cursor()
#    sql = "insert into user(id,email,name) values(%s,%s,%s)"
#    val = [id,email,name]
#    cur.execute(sql,val)
#    mysql.connection.commit()
#    cur.close()
#    return "register success"

# @app.route("/register_form",methods=["POST"])
# def register_form():
#    return render_template("register.html")

@app.route("/update",methods=["POST"])
def updateuser():
   id = request.form['id']
   email = request.form['email']
   cur = mysql.connection.cursor()
   sql = "update user set email=%s where id=%s"
   val = [email,id]
   cur.execute(sql,val)
   mysql.connection.commit()
   cur.close()
   return "update success"

@app.route("/update_form",methods=["GET"])
def update_form():
   return render_template("update.html")

@app.route("/delete",methods=["POST"])
def deleteuser():
   id = request.form['id']
   cur = mysql.connection.cursor()
   sql = "delete from user where id=%s"
   val = [id]
   cur.execute(sql,val)
   mysql.connection.commit()
   cur.close()
   return "delete success"

@app.route("/delete_form",methods=["GET"])
def delete_form():
   return render_template("delete.html")




if __name__ == '__main__':
    
    app.run()
