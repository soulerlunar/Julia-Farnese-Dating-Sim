init python:
    #Allows a 
    # def confide(confindee, confidant):

    # def update_trusted(npc):
    #     trusted = npc.trusted

    #     for t in trusted:
    #         t.


    # Determines who voted for who
    # Params:
    # - voters: a list of voter class people
    #
    # returns: a dictionary of who voted for who
    def get_votes(voters):

        votes = {}

        print("Getting votes")
        for v in voters:
            votes[v.name] = v.leading
            print(str(v.name) + ": " + str(v.leading))

        return votes

    # Counts votes from a dictionary of votes cast
    # Params:
    #  
    # Returns: how many votes each person got
    def count_votes(votes):

        results = {}

        #loops through items in dict
        for v in votes.items():
            if not v[1] in results:
                results[v[1]] = 1
            else:
                results[v[1]] += 1

        return results

    # Params:
    # - votes: dictionary of candidates and how many votes they got
    # 
    # returns: winner from list
    def get_winner(votes):
        top_votes = max(votes.values())
        vote_sum = sum(votes.values())
    
        if top_votes > vote_sum/2:
            return max(votes, key=votes.get)
        else:
            return None


