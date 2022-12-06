from flask import request,Flask
import json,socket
from dict_ import Pdict

role= Flask(__name__)
email_roles={}
class Rdict(Pdict):#child class for failure login
    def getdict(echo,email,role,success):
        returnDictionary = Pdict(echo).getdict()
        returnDictionary["email"]=email
        returnDictionary["role"]=role
        returnDictionary["success"] =success
        return returnDictionary

##Role Based Access Service
@role.route('/check_role',methods=['POST'])
def check_role():
    email = request.json['email']
    role=request.json['role']
    if(email in email_roles):
        if(email_roles[email]==role):
            returnDictionary = Rdict.getdict(str(socket.gethostname()),email,role,True)
            return json.dumps(returnDictionary)
        else:
            returnDictionary = Rdict.getdict(str(socket.gethostname()),email,role,False)
            return json.dumps(returnDictionary)
    else:
        email_roles[email]=role
        returnDictionary = Rdict.getdict(str(socket.gethostname()),email,role,False)
        return json.dumps(returnDictionary)

if __name__ == '__main__':
    role.run(debug=True, host='0.0.0.0', port=5000)
