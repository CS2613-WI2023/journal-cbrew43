#define the Renter Class

class Renter(object):
  def __init__(self, name, room_number, days_booked):
    self.name = name
    self.room_number = room_number
    self.days_booked = days_booked

  def rental_choices(days_booked):
    pass
  
  def get_name(self):
    return self.name

  def get_room_number(self):
    return self.room_number
  
  def get_days_booked(self):
    return self.days_booked

  def print_info():
    return "something"
  

#Class responsible for Short Term Rental Calculation
class ShortTermRenter(Renter):
  def rental_choices(self, days_booked):
    p_room = (119.00*1.15)
    p_breakfast = 5.99
    print("Would they like to purchase the breakfast plan? (Y/N)")
    c_breakfast = input()
    breakfast = c_breakfast.lower()
    room_price = p_room*days_booked
    if(breakfast==f'y'):
      room_price+= (p_breakfast*days_booked)
    print("Cost of stay: ", room_price, "\n")
    return room_price

class LongTermRenter(Renter):
  def rental_choices(self, days_booked):
    p_room = (119.00*1.15)*0.70
    p_choices = [[0.00, "No Package"], [25.00, "Basic Package"], [75.00, "Premium Package"]]  #Package choices
    
    print("Would they like to purchase an insurance package?")
    for i, package in enumerate(p_choices):
      print(f"\t{i}: {package[1]}")
    c_insurance = int(input())
    insurance = p_choices[c_insurance]

    room_price = (p_room*days_booked)+insurance[0]
    print("Cost of stay: ", room_price, "\n")
'''
@param renters, set of people currently booked in the motel
@param current_room, the next vacant room to be assigned
@return the new array of renters at the motel
'''
def new_rental(current_room):
  print("Input name:")
  r_name = input()
  print("Number of days staying:")
  r_days = input()
  r_days = int(r_days)
  if(r_days<15):
    Added = ShortTermRenter(r_name, current_room, r_days)
  else:
    Added = LongTermRenter(r_name, current_room, r_days) #for now
  
  Added.rental_choices(r_days)

  return Added


def main():
  #driver function
  init = ''
  renters = []
  current_room = 1
  while(init!=f'X'):
    print("Make a Selection:\nRent a Room (R), Check Out (C), Print Motel Details (P), Exit Program (X)")
    init = input()
    choice = init.lower()
    if(choice == f'x'):
      break
    if(choice == f'r'):
      updated_room = new_rental(current_room)
      renters.insert(current_room, updated_room)
    current_room+=1
    for room in renters:
      print(room.get_name())


#This ensures that given this is ran as a script, it will start with the main() function.
if __name__ == "__main__":
  main()