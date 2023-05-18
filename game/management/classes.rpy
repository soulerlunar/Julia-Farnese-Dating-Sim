init python:
    print()
    class NPC:
        def __init__(self, character, self_op = 10):
            self.c = character
            self.opinions = {}
            self.opinions[character.name] = self_op

        def set_opinion(self, candidate, opinion):
            self.opinions[candidate] = opinion

        def add_opinion(self, candidate, opinion_mod):
            self.opinions[candidate] += opinion_mod

        def get_opinion(self, candidate):
            return self.opinions[candidate]

    class Voter(NPC):
        def __init__(self, character, self_op = 10):
            super().__init__(character, self_op)
            self.leading = character.name
            self.leading_op = self.opinions[character.name]

        def set_opinion(self, candidate, opinion):
            super().set_opinion(candidate, opinion)
            if opinion > self.leading_op:
                self.leading = candidate
                self.leading_op = opinion

        def set_opinion(self, candidate, opinion_mod):
            super().add_opinion(candidate, opinion_mod)
            if self.opinions[candidate] > self.leading_op:
                self.leading = candidate
                self.leading_op = opinion

        def cast_vote(self):
            return self.leading

    class Partner(Voter):
        def __init__(self, character, base_love, self_op = 10):
            self.love = base_love
            super().__init__(character, self_op)

        def set_love(self, love):
            self.love = love

        def add_love(self, love_mod):
            self.love = love_mod

        def get_love(self):
            return self.love