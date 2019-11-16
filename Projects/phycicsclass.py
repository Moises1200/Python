


###################################################################################################
#Creating a simple function to print x*y
def add(x,y):
    c = x*y
    print(c)


add(4,5)

###################################################################################################
def greet():
    print("hello")
    print("Good Morning")
greet()

###################################################################################################
#Function to convert fahrenheit to celsius
def f_to_c(f_temp):
  c_temp=(f_temp-32)*5/9
  return c_temp

f100_in_celsius = f_to_c(0)
print(f100_in_celsius)



###################################################################################################
#Function to convert Celsius to Fahrenheit
def c_to_f(c_temp):
  f_temp = c_temp*(9/5) +32
  return f_temp
c0_in_fahrenheit = c_to_f(30)
print(c0_in_fahrenheit)

###################################################################################################
#Calculate Force for Train
train_mass = 22680
train_acceleration = 10
train_distance = 100

bomb_mass = 1


def get_force(mass,acceleration):
  return mass*acceleration

train_force = get_force(train_mass,train_acceleration)

print(train_force)

print("The GE train supplies " + str(train_force) +" Netwon of force")
###################################################################################################

#Get Energy for Train

def get_energy(mass,c=3*10**8):
  return mass*c**2

bomb_energy=get_energy(bomb_mass)

print("A 1kg bomb supplies " + str(bomb_energy) + " Joules")

###################################################################################################
#Get work function
def get_work(mass,acceleration,distance):
  force=get_force(mass,acceleration)
  return force*distance


train_work = get_work(train_mass,train_acceleration,train_distance)
print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance))



def mult_by_four(number):
  multiplied = number * 4
  return multiplied
#math = mult_by_four(9)
#print(str(math))
print(mult_by_four(10))

###################################################################################################

#Create an average function
def average(num1,num2):
    average = (num1+num2)/2
    return average

total_average=average(10,15)
print(str(total_average))

###################################################################################################

# Write your tenth_power function here:
def tenth_power(num):
    power = num ** 10
    return power


total_value = tenth_power(10)

print(tenth_power(90))

###################################################################################################

# Write your square_root function here:
def square_root(num):
    square = num ** .5
    return square


# Uncomment these function calls to test your square function:
print(square_root(16))
# should print 4
print(square_root(100))
# should print 10


# Write your square_root function here:
def square_root(num):
    return num ** 0.5

# Uncomment these function calls to test your square_root function:
print(square_root(16))
# should print 4
print(square_root(100))
# should print 10

###################################################################################################

# Write your tip function here:
def tip(total, percentage):
    tip_amount = (total * percentage) / 100
    return tip_amount


# Uncomment these function calls to test your tip function:
print(tip(10, 25))
# should print 2.5
print(tip(0, 100))
# should print 0.0

###################################################################################################
# Write your win_percentage function here:
def win_percentage(wins, loses):
    total = (wins) / (wins + loses) * 100
    return total


# Uncomment these function calls to test your win_percentage function:
print(win_percentage(5, 5))
# should print 50
print(win_percentage(10, 0))
# should print 100

#Write your lose_percentage function here
def lose_percentage(wins,loses):
    total = (loses)/(wins+loses)*100
    return total

print(lose_percentage(100,60))
###################################################################################################
# Write your first_three_multiples function here:
def first_three_multiples(num):
  print(num*1)
  print(num*2)
  print(num*3)
  return num*3
# Uncomment these function calls to test your first_three_multiples function:
first_three_multiples(10)
# should print 10, 20, 30, and return 30
first_three_multiples(0)
# should print 0, 0, 0, and return 0
###################################################################################################
# Write your dog_years function here:
def dog_years(name, age):
  return name+", you are "+str(age*7)+" years old in dog years"

# Uncomment these function calls to test your dog_years function:
print(dog_years("Lola", 16))
# should print "Lola, you are 112 years old in dog years"
print(dog_years("Baby", 0))
# should print "Baby, you are 0 years old in dog years"

###################################################################################################

# Write your remainder function here:
def remainder(num1, num2):
  return (2*num1)%(num2/2)

# Uncomment these function calls to test your remainder function:
print(remainder(15, 14))
# should print 2
print(remainder(9, 6))
# should print 0

###################################################################################################
# Write your lots_of_math function here:
def lots_of_math(a, b, c, d):
  first = a+b
  second = c-d
  third = first*second
  fourth = third%a
  print(first)
  print(second)
  print(third)
  return fourth

# Uncomment these function calls to test your lots_of_math function:
print(lots_of_math(1, 2, 3, 4))
# should print 3, -1, -3, 0
print(lots_of_math(1, 1, 1, 1))
# should print 2, 0, 0, 0
###################################################################################################

