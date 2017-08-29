import random

class Markov:
    def __init__(self):
        self.Text = ""

    def LoadText(self,Filename):
        file = open(Filename,"r")
        self.Text += file.read().replace("\n"," ")
        

    def Analyse(self,Prefix_Length = 2):
        TextList = self.Text.split(" ")
        TextList = list(filter(lambda w : w not in ["","m","h"] , TextList))
        self.Analysis = {}
        for x in range(len(TextList)):
            if x >= 2:
                key = []
                for y in range(x-Prefix_Length,x):
                    key.append(TextList[y])
                self.Analysis.setdefault(tuple(key),[]).append(TextList[x])
            
            

    def Write(self,Seed,Prefix_Length = 2,Length = 100, Stability = 100):
        WrittenList = Seed.split(" ")
        while len(WrittenList) < Length:
            ListLength = len(WrittenList)
            key = []
            for y in range(ListLength-Prefix_Length,ListLength):
                key.append(WrittenList[y])

            key = tuple(key)
            if key in self.Analysis and random.randint(0,Stability) != 0:
                word = random.choice(self.Analysis[key])
            else:
                word = random.choice(random.choice(list(self.Analysis.values())))
            WrittenList.append(word)
        Text = ""
        for word in WrittenList:
            Text += word + " "

        return Text

    
                
