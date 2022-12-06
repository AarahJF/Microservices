from flask import request,Flask

import json,socket
from dict_ import Pdict

pa= Flask(__name__)

class Qdict(Pdict):#child class for failure login
    def getdict(echo,password,success):
        returnDictionary = Pdict(echo).getdict()
        returnDictionary["password"] = password
        returnDictionary["success"] =success
        return returnDictionary

##Password Service
@pa.route('/check_password',methods=['POST'])
def check_password():
    password = request.json['password']
    password_length=len(password)

    l, u, p, d = 0, 0, 0, 0

    if (password_length >= 8):
        for i in password:
            # counting lowercase alphabets
            if (i.islower()):
                l+=1           
            # counting uppercase alphabets
            if (i.isupper()):
                u+=1           
            # counting digits
            if (i.isdigit()):
                d+=1           
            # counting  special characters
            if(i=='@'or i=='$' or i=='_'):
                p+=1          
    if (l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==password_length):
        returnDictionary = Qdict.getdict(str(socket.gethostname()),password,True)
        return json.dumps(returnDictionary)
    else:
        returnDictionary = Qdict.getdict(str(socket.gethostname()),password,False)
        return json.dumps(returnDictionary)

if __name__ == '__main__':
    pa.run(debug=True, host='0.0.0.0', port=5000)
