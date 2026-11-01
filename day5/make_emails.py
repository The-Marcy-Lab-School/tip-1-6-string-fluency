# Day 5 Make: the email list
# People typed their emails into the sign-up form by hand. Before sending the
# welcome message, clean each one and see which email services people use.
# Requirements are in the README.

emails = [
    "  Ana.Ruiz@Gmail.com",
    "bo@marcylabschool.org ",
    "JORDAN.LEE@gmail.com",
    " priya@Yahoo.com ",
]

# In:
# Out:


def clean_email(email):
    return email  # replace this line


def domain(email):
    return email  # replace this line


print(clean_email("  Ana.Ruiz@Gmail.com"))   # expected ana.ruiz@gmail.com
print(domain("ana.ruiz@gmail.com"))          # expected gmail.com

# Then: print each cleaned email's domain, and how many are gmail.com.
