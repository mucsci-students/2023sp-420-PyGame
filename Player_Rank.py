
class rank:
    # return_Rank takes in current_Points, and max_Points as parameters, then returns the correspending integer
    # to the rank that the player is at.
    # Must be between 0.00 and 1.00
    def return_Rank(currentPoints, maxPoints):

        difference = currentPoints/maxPoints
        #precondition check for between 0.00 and 1.00
        if difference <0 or difference >1:
            return 0 #out of bounds


        if difference >= 0 and difference < .03:
            return 1 #Beginner
        elif difference >= .03 and difference < .07:
            return 2 #Novice
        elif difference >= .07 and difference < .12:
            return 3 #Okay
        elif difference >= .12 and difference < .23:
            return 4 #Good
        elif difference >= .23 and difference < .35:
            return 5 #Solid
        elif difference >= .35 and difference < .56:
            return 6 #Nice
        elif difference >= .56 and difference < .72:
            return 7 #Great
        elif difference >= .72 and difference < 1:
            return 8 #Amazing
            
        return 9 #Genius