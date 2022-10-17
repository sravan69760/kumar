from flask import Flask,request,render_template

application = Flask(__name__)

@application.route('/')
def hello_world():
    return render_template('login.html')
database={'harsha':'123','vishnu':'123','karthik':'iamnew'} # change your username and password

@application.route('/form_login',methods=['POST','GET'])
def login():
    name1=request.form['username']
    pwd=request.form['password']
    if name1 not in database:
        return render_template('login.html',info='Invalid User')
    else:
        if database[name1]!=pwd:
            return render_template('login.html',info='Invalid Password')
        else:
            return render_template('home.html',name=name1)

if __name__ == '__main__':
    application.run()
