# Use Correct Data Structure
# For better efficency, one can use the built in data structure, which is more optimised, tested and better

score_of_batsmen = [22, 44, 52, 33, 22, 57, 1, 0, 100, 82, 1]

def remove_duplicates_from_scores(score_of_batsmen):
    pass
    # Implement logic to remove duplicates

#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#

# In the above program snippet, instead our own logic, one can use the build-in set, which removes the duplicates of its elements automatically
# This will save our time, and one can learn here, to use the correct data structure for right purpose
# If one wants, to implement the logic on our own, without using the predifined data structure, then one can proceed and make their own

def remove_duplicates_from_scores_using_set(score_of_batsmen):
    score_of_batsmen_set = set()
    score_of_batsmen_set = score_of_batsmen
    return score_of_batsmen_set




