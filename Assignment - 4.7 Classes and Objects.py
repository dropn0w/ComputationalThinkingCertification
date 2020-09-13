# First you need to create your class, basically it is the same way
# that you have seen during the video class

class County :
  def __init__(self, init_name, init_population, init_voters):
    self.name = init_name
    self.population = init_population
    self.voters = init_voters

# Now you need to create the fonction to find the highest porcentage of voters

def highest_turnout(data) :
  highest_turnout = 0
  highest_test = 0
  for i in data :
    highest_test = i.voters / i.population
    if highest_test > highest_turnout :
      highest_turnout = highest_test
      name_highest_turnout = i.name

 # Now, you just need to set the tuples to get the resultat that they want

  return name_highest_turnout, highest_turnout

# your program will be evaluated using these objects
# it is okay to change/remove these lines but your program
# will be evaluated using these as inputs

allegheny = County("allegheny", 1000490, 645469)
philadelphia = County("philadelphia", 1134081, 539069)
montgomery = County("montgomery", 568952, 399591)
lancaster = County("lancaster", 345367, 230278)
delaware = County("delaware", 414031, 284538)
chester = County("chester", 319919, 230823)
bucks = County("bucks", 444149, 319816)
data = [allegheny, philadelphia, montgomery, lancaster, delaware, chester, bucks]


result = highest_turnout(data) # do not change this line!
print(result) # prints the output of the function
# do not remove this line!
