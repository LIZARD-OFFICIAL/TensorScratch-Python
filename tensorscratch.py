import json
class TensorScratchModel:
    def __init__(self,dataset={}):
        self.dataset = dataset
    def optimize(self):
        self.dataset = {ele[0] : ele[1]  for ele in sorted(list(self.dataset.items()), key = lambda key : len(key[0]))}
    def train(self,data,*,overwrite=False):
        if overwrite:
            self.dataset = data
        else:
            self.dataset.update(data)
    def __str__(self):
        return f"{self.dataset}"
class Conversion:
    def intent_to_tsm(filepath):
        flnm = filepath
        with open(flnm,"r") as file:
            myf = file.read()
        intents = json.loads(myf)["intents"]
        result = {}
        for index,item in enumerate(intents):
            response = item["responses"]
        for index,item in enumerate(item["patterns"]):
            result.update({item:response})
        result = json.dumps(result)
        with open(flnm, 'w') as file:
            file.write(result)

Model = TensorScratchModel()
Model.train({"Hello":["Hi"],"Hi":["Hello"]},overwrite=True)
print(Model)
print(type(["lol"])==list())