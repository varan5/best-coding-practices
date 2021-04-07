# Avoid un-necessary variables.
# It is better to make variables, if they variable is being used in multiple places.
# On the other hand, if the variable is not getting repeatedly used, then one should not make the non-repeatedly used literal, a variable

# Ok
def get_phone_number(user_name):
    user_phone_number = 4374348499
    return user_phone_number



# Better
def get_phone_number(user_name):
    return 4349734949