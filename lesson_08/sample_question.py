
pets = ['tortoise', 'parrot', 'guinea pig', 'lizard']
pets.pop(2)
pets = ['bulldog', 'persian cat', 'sunbird']

# Discuss whether there is any occurrence of
# automatic garbage collection in the example.
# Explain your answers with the aid of (a) diagram(s).
#

# At line 1, the variable pets point to a list of 4 string objects
#      diagram 1
#
# At line 2, string object 'guinea pig' at position 2 is no longer
# referenced. Hence, garbage collection occurs here.
#      diagram 2
#
# At line 3, pets was reassigned to a new list object containing
# ['bulldog', 'persian cat', 'sunbird']. The old list object is
# no longer referenced. Hence, the old list object is garbage
# collected.
#       diagram 3
