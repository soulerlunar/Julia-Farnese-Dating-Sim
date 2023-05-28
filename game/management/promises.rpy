init python:

    BROKEN_PROMISE_PENALTY = -20

    class Promise:
        def __init__(self, name, promiser, promisee, value):
            self.name = name
            self.promiser = promiser
            self.promisee = promisee
            self.value = value

        def make(self):
            self.promiser.make_promise(self)
            self.promisee.receive_promise(self)

        def annul(self):
            self.promiser.unmake_promise(self)
            self.promisee.lose_promise(self)
        
        def broken(self):
            promiser = self.promiser
            promisee = self.promisee

            promiser.unmake_promise(self)
            promisee.lose_promise(self)
            promisee.add_opinion(promiser, BROKEN_PROMISE_PENALTY) #Should lose opinion of promiser when a promise is broken
    
    class PromiseCategory:
        def __init__(self, name, influences=[],contradictions=[]):
            self.name = name #name of the promise
            self.influences = {} #people influenced by this promise
            self.contradictions = [] #Other promises this one contradicts, just names

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
            if promisee.name in self.influences:
                promise = Promise(self.name, promiser, promisee, self.influences[promisee.name])
            else:
                promise = Promise(self.name, promiser, promisee, 0)
            return promise

        def contradicts(self, p_name):
            if p_name in self.contradictions:
                return True
            else:
                return False