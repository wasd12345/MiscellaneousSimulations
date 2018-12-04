"""
Simulating the "combinatorics of spaghetti hoops"

Some generalizations of the combinatorics problems from:
http://www.admin.cam.ac.uk/whatson/detail.shtml?uid=c97f2a30-93ae-472f-908b-8d27e5c73cd4

Abstract: Starting with n cooked spaghetti strands, tie randomly chosen ends 
together to produce a collection of spaghetti hoops. What is the expected 
number of hoops? What can be said about the distribution of the number of hoops
of length 1, 2, …? What is the behaviour of the longest hoops when n is large?
What is the probability that all the hoops have different lengths? Questions
like this appear in many guises in many areas of mathematics, the connection 
being their relation to the Ewens Sampling Formula (ESF). I will describe a 
number of related examples, including prime factorisation, random mappings and 
random permutations, illustrating the central role played by the ESF. I will 
also discuss methods for simulating decomposable combinatorial structures by 
exploiting another wonder of the ESF world, namely the Feller Coupling. 
Analysis of a children’s playground game shows that apparently small departures
from the Feller model can open up a number of unsolved problems.
"""


# PARAMETERS
# n = total number of objects
# e_i = number of endpoints on the ith object
# E = total number of endpoints summed across all objects
# C = number of different colors of objects
# c_i = color of ith object
# or c_i_j = color of jth endpoint of ith object, if colors allowed to vary across endpoints within an object
# [or more generally, if K attributes per object (e.g. color, weight, texture):
# <c1_i_j, ..., cK_i_j> 

# SELECTION RULES:
# P_i_j is probability of choosing jth endpoint of ith object
# [or more generally P(i,j| ij_-1, ij_-2, ... ), i.e. if not independently 
# sampled, given the history of previous endpoints selected]

# SAMPLING PROCEDURE
# 1. Sample until all endpoints ar matched (only possible if E is even)
# 2. Sample a fixed number of endpoints
# 3. Sample until some condition met (quota on #unique objects, quota on number
#    of objects of a certain kind, ...)

# MEASURED QUANTITIES
# Various moments (mean, variance, ...) of:
# 1. Number of total hoops (connected components)
# 2. Number of hoops containing a given number of objects {1,...,n}
# 3. Number of hoops containing e.g. B blue objects and R red objects ...
# 4. Functions considering other graph properties





# =============================================================================
# Standard problem
# (as described above in abstract)
# e_i = 2 for all objects i=1,...,n
# C = 1 (only 1 type of object)
# =============================================================================
# Simulate expected value and variance of:
#    Total number of hoops
#    Number of hoops of each length (1,...,n}
#    Size of the largest hoop





# =============================================================================
# Variation 1
#
# What if each piece of spaghetti is an octopus?
#
# Sample in the same way (until all endpoints are joined), but now each object
# has some number E of endpoints (instead of 2 for spaghetti, e.g. 8 for an 
# octopus, or any integer in general). Assume all objects still have the same 
# value of E (number of endpoints). 
# Interesting things happen: for odd E, no object can connect only with itself,
# it must connect with at least 1 other object (1 or 3 other objects). But for
# even E, an object could fully connect with itself.
#
# Now each "hoop" is a tangle of objectsthat is completely disjoint from all
# other tangles of objects. I.e. it is a connected component of a graph.
# =============================================================================





# =============================================================================
# Variation 2
# 
# No self-loops
#
# As in simple case, but now a single spaghetti cannot have it's own endpoints joined
# =============================================================================



# =============================================================================
# Variation 3
#
# Non-uniform selection probabilities
#
# Each endpoint has arbitrary selection probability (but still sampled 
# independently, i.e. selecting endpoint e_
# =============================================================================




