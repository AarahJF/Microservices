import re
from flask import request, Flask

import json,socket
from dict_ import Pdict

em = Flask(__name__)

class Mdict(Pdict):#child class for failure login
    def getdict(echo,email,success):
        returnDictionary = Pdict(echo).getdict()
        returnDictionary["email"] = email
        returnDictionary["success"] =success
        return returnDictionary


##Email service
@em.route('/check_email',methods=['POST'])
def check_email():  
    email = request.json['email']
    #make regular expression to validate email
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        
    if(re.fullmatch(regex, email)):        
        returnDictionary=Mdict.getdict(str(socket.gethostname()),email,True)
        return json.dumps(returnDictionary)
    else:
        returnDictionary=Mdict.getdict(str(socket.gethostname()),email,False)
        return json.dumps(returnDictionary)

if __name__ == '__main__':
    em.run(debug=True, host='0.0.0.0', port=5000)
