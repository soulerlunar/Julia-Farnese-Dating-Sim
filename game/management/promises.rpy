init python:
    class Promise:
        def __init__(name, promiser, value):
            self.name = name
            self.promiser = promiser
            self.value = value
    
    class PromiseCategory:
        def __init__(self, name, influences=[],contradictions=[]):
            self.name = name #name of the promise
            self.influences = {} #people influenced by this promise
            self.contradictions = [] #Other promises this one contradicts

            for i in influences:
                self.add_influenced(i[0], i[1])
            
            for p in contradictions:
                self.add_contradiction(p)

        def add_influenced(self, person, value):
            self.influences[person.name] = value

        def add_contradiction(self, promise):
            if not promise.name in self.contradictions:
                self.contradictions.append(promise.name)
                promise.contradictions.append(self.name)

        def generate_promise(self, promiser, promisee):
            promise = Promise(self.name, promiser, self.influence[promisee.name])
            return promise