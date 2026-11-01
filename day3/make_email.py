# Day 3 Make: is this an email address?
# The same sign-up form also asks for an email. Before sending a welcome
# message, the pantry checks that the entry could be an email address.
# Requirements are in the README.

# In:
# Out:


def is_valid_email(email):
    return True  # replace this line


print(is_valid_email("ana.ruiz@gmail.com"))   # expected True
print(is_valid_email("ana.ruiz gmail.com"))   # expected False (no @)
print(is_valid_email("@gmail.com"))           # expected False (starts with @)
print(is_valid_email("ana.ruiz@gmail."))      # expected False (ends with .)
print(is_valid_email("ana ruiz@gmail.com"))   # expected False (has a space)
print(is_valid_email(""))                     # expected False
