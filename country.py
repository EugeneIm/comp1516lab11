#This file contains the country CLASS. 
#Define a constructor that takes 3 parameters;
    #country name
    #capital name
    #and a population

#IN the constructor, assign the parameter values to the sinstance variables, unless the population is 
#less than 2 mill; in that case, raise ValueError with a message in the format:
    #Population ... is too low

print_detail() #This method prints data in this format:
    #The capital of Canada (pop.1234567) is Ottowa

birth() #This method adds 1 to the objects own self's population

death() #This method subtracts 1 from the objects own self population

disaster() #For countries with a population of 100m or higher, this method subtracts 100m 
           #If population < 100m, after disaster(), the population == 0. 

