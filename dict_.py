class Pdict:
    def __init__(self,echo):
        self.echo=echo
    
    def getdict(self):
        returnDictionary = {}
        returnDictionary["echo"] = self.echo
        return returnDictionary