init python:
    
    julia_name = "julia"

    class NPC:
        def __init__(self, name, character, self_op = 90, julia_op = 30, candidate = False):
            self.c = character #the character setter
            self.name = name #internal name for tracking purposes
            self.candidate = candidate #boolean whether is a papal candidate or not
            self.opinions = {} #dicionary of character names and opinion values
            # opinions must be between 0 and 100
            self.papal_ops = {}
            self.trusted = [] #A list of trusted confidants

            self.opinions[character.name] = self_op #sets the opinion on self
            self.opinions[julia_name] = julia_op #sets the opinion on self

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
            if not p_name in self.opinions:
                self.opinions[p_name] = 0

            self.opinions[person] += opinion_mod
            self.normalize_op(person)

        # Gets the opinion on a person
        # 
        # return: opinion score
        def get_opinion(self, person):
            p_name = person.name
            return self.opinions[p_name]

        # Sets the papability opinion on the given person
        # Params: 
        #   - person: an NPC to set thoughts on papability
        #   - opinion: an int to set opinion to
        # 
        def set_papal_op(self, person, opinion):
            self.papal_ops[person.name] = opinion

        # Adds a value to an opinion on papability for a person
        # Params: 
        #   - person: an NPC to set opinion on
        #   - opinion_mod: an int to modify the opinon
        # 
        def add_papal_op(self, person, opinion_mod):
            p_name = person.name
            if not p_name in self.papal_ops:
                self.papal_ops[p_name] = 0

            self.opinions[person] += opinion_mod
            self.normalize_op(person)

        # Gets the opinion on a candidate's papability
        # 
        # return: papal opinion score
        def get_papal_op(self, person):
            p_name = person.name
            return self.papal_ops[p_name]

        def get_candidacy_score(self, person):
            return self.get_opinion(person) * self.get_papal_op(person)

        # Passes an opinion onto another NPC
        # Params:
        # - confidant: an NPC to confide to
        # - thought: a tuple (person, opinion) to share
        #
        def confide(self, confidant, thought):
            multiplier = 0
            conf_op = confidant.get_opinion(self) #confidant's opinion of confider
            if conf_op >= 60:
                multiplier = conf_op / 80
            else:
                multiplier = (conf_op / 80) ** 2

            confidant.add_opinion(thought[0],thought[1] * multipler)


    class Voter(NPC):
        def __init__(self, name, character, self_op = 90, julia_op = 30, candidate = True):
            super().__init__(name, character, self_op, julia_op, candidate)
            self.leading = name #who is the voter's leading choice
        
        #gets the opinion on the leading candidate
        #
        # return: opinion on leading candidate
        def get_leading_op(self):
            return self.get_candidacy_score(self.leading)

        # Updates the tracked leading candidate if person is a candidate and is
        # scoring better than current leading candidate
        # Params:
        #   - person: person to check
        #   - opinion: opinion on them
        #
        # Returns: True if updated, false if not
        def comp_leading(self, person):
            if not person.candidate:
                return False
            if self.get_candidacy_score(person) > self.get_leading_op():
                self.leading = candidate.name
                return True
            else:
                return False

        # NPC Set opinion, but also updates leading candidate
        def set_opinion(self, person, opinion):
            super().set_opinion(person, opinion)
            self.comp_leading(person)

        # NPC Add opinion, but also updates leading candidate
        def add_opinion(self, person, opinion_mod):
            super().add_opinion(person, opinion_mod)
            self.comp_leading(person)

        # NPC Set papability opinion, but also updates leading candidate
        def set_opinion(self, person, opinion):
            super().set_papal_op(person, opinion)
            self.comp_leading(person)

        # NPC Add papability opinion, but also updates leading candidate
        def add_opinion(self, person, opinion_mod):
            super().add_papal_op(person, opinion_mod)
            self.comp_leading(person)

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