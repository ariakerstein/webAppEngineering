# User Instructions
# 
# Write a function 'sub1' that, given a 
# string, embeds that string in 
# the string: 
# "I think X is a perfectly normal thing to do in public."
# where X is replaced by the given 
# string.
#

t1 = "I think %s is a perfectly normal thing to do in public."
def sub1(s):
    return t1 % s


print sub1("fucking") 
# => "I think running is a perfectly normal thing to do in public."    
# sub1("sleeping") 
# => "I think sleeping is a perfectly normal thing to do in public."
