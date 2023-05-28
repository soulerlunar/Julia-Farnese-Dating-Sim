init python:
    
    julia_name = "julia"

    class NPC:
        def __init__(self, name, character, self_op = 90, julia_op = 30, candidate = False):
            self.c = character #the character setter
            self.name = name #internal name for tracking purposes
            self.candidate = candidate #boolean whether is a papal candidate or not
            self.opinions = {} #dicionary of character names and opinion values
            # opinions must be between 0 and 100
            self.opinions[character.name] = self_op #sets the opinion on self
            self.opinions[julia_name] = julia_op #sets the opinion on self
            self.trusted = [] #A list of trusted confidants

        # Normalizes an NPCs opinion
        # Params: person - an NPC to normalize opinion on
        #
        # return True if normalized, False if not
        def normalize_op(self, person):
            p_name = person.name
            if not p_name in self.opinions:
                #If opinion does not exist, cannot be normalized
                return False

            opinion = self.opinions[person.name]
            if opinion > 100:
                self.opinions[p_name] = 100
                return True
            elif opinion < 0:
                self.opinions[p_name] = 0
                return True
            else:
                return False

        # Sets the opinion on the given person
        # Params: 
        #   - person: an NPC to set opinion on
        #   - opinion: an int to set opinion to
        # 
        def set_opinion(self, person, opinion):
            self.opinions[person.name] = opinion
            self.normalize_op(person)

        # Adds a value to an opinion on a person
        # Params: 
        #   - person: an NPC to set opinion on
        #   - opinion_mod: an int to modify the opinon
        # 
        def add_opinion(self, person, opinion_mod):
            p_name = person.name
            if p_name in opinions:
                self.opinions[p_name] = 0

            self.opinions[person] += opinion_mod
            self.normalize_op(person)

        # Gets the opinion on the candidate
        # 
        # return: opinion score
        def get_opinion(self, person):
            p_name = person.name
            return self.opinions[p_name]

        # Passes an opinion onto another NPC
        # Params:
        # - confidant: an NPC to confide to
        # - thought: a tuple (person, opinion) to share
        #
        def confide(self, confidant, thought):
            multiplier = 0
            conf_op = confidant.get_opinion(self) #confidant's opinion of confider
            if conf_op >= 60:
                multiplier = conf_op / 100
            else:
                multiplier = (conf_op / 100) ** 2

            confidant.add_opinion(thought[0],thought[1] * multipler)


    class Voter(NPC):
        def __init__(self, name, character, self_op = 90, julia_op = 30, candidate = True):
            super().__init__(name, character, self_op, julia_op, candidate)
            self.leading = name #who is the voter's leading choice
        
        #gets the opinion on the leading candidate
        #
        # return: opinion on leading candidate
        def get_leading_op(self):
            return self.opinions[self.leading]

        # Updates the tracked leading candidate if person is a candidate
        # Params:
        #   - person: person to check
        #   - opinion: opinion on them
        #
        # Returns: True if updated, false if not
        def update_leading(self, person, opinion):
            if person.candidate and opinion > self.get_leading_op():
                self.leading = candidate.name
                self.leading_op = opinion
                return True
            else:
                return False

        # NPC Set opinion, but also updates leading candidate
        def set_opinion(self, person, opinion):
            super().set_opinion(candidate, opinion)
            self.update_leading(person, opinion)

        # NPC Add opinion, but also updates leading candidate
        def add_opinion(self, person, opinion_mod):
            super().add_opinion(candidate, opinion_mod)
            self.update_leading(person, opinion)

        #TODO
        def cast_vote(self):
            return self.leading

    class Partner(Voter):
        def __init__(self, name, character, self_op = 100, julia_op = 30, candidate = True):
            super().__init__(name, character, self_op, julia_op, candidate)

        #All love functions are just an easy way to modify the opinion on Julia
        def set_love(self, love):
            self.opinions[julia_name] = love

        def add_love(self, love_mod):
            self.opinions[julia_name] += love_mod

        def get_love(self):
            return self.opinions[julia_name] 