from flask import request, Flask

import json,socket
from dict_ import Pdict

li = Flask(__name__)

class Ldict(Pdict):#child class for failure login
    def getdict(echo,email,password,success):
        returnDictionary = Pdict(echo).getdict()
        returnDictionary["email"] = email
        returnDictionary["password"]=password
        returnDictionary["success"] =success
        return returnDictionary

##Login service
@li.route('/login')
def login():
    returnDictionary = Pdict(str(socket.gethostname())).getdict()
    return json.dumps(returnDictionary)

@li.route('/login', methods=['POST'])
def login_post():

    email = request.json['email']
    password = request.json['password']
    
    returnDictionary=Ldict.getdict(str(socket.gethostname()),email,password,True)
    return json.dumps(returnDictionary)
    
if __name__ == '__main__':
    li.run(debug=True, host='0.0.0.0', port=5000)