
class rank:
    # return_Rank takes in current_Points, and max_Points as parameters, then returns the correspending integer
    # to the rank that the player is at.
    # Must be between 0.00 and 1.00
    def return_Rank(current_Points, max_Points):
        #precondition check for between 0.00 and 1.00
        if current_Points / max_Points <0 or current_Points / max_Points >1:
            return 0 #out of bounds


        if current_Points / max_Points >=0 and current_Points / max_Points <=.03:
            return 1 #Beginner
        elif current_Points / max_Points >=.03 and current_Points / max_Points <.07:
            return 2 #Novice
        elif current_Points / max_Points >=.07 and current_Points / max_Points <.12:
            return 3 #Okay
        elif current_Points / max_Points >=.12 and current_Points / max_Points <.23:
            return 4 #Good
        elif current_Points / max_Points >=.23 and current_Points / max_Points <.35:
            return 5 #Solid
        elif current_Points / max_Points >=.35 and current_Points / max_Points <.56:
            return 6 #Nice
        elif current_Points / max_Points >=.56 and current_Points / max_Points <.72:
            return 7 #Great
        elif current_Points / max_Points >=.72 and current_Points / max_Points <1:
            return 8 #Amazing
        elif current_Points / max_Points == 1:
            return 9 #Genius