from flask import request,Flask
import json,socket
from dict_ import Pdict

app=Flask(__name__) 

class Cdict(Pdict):#child class for profile
    def getdict(echo,name,role):
        returnDictionary = Pdict(echo).getdict()
        returnDictionary["name"] = name
        returnDictionary["role"] = role
        return returnDictionary

##Profile service
@app.route('/')
def echo():
    returnDictionary = Pdict(str(socket.gethostname())).getdict()
    return json.dumps(returnDictionary)

@app.route('/profile',methods=['POST'])
def profile():
    email = request.json['email']
    role = request.json['role']
    returnDictionary=Cdict.getdict(str(socket.gethostname()),email,role)
    return json.dumps(returnDictionary)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)