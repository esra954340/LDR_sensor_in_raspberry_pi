import RPi.GPIO as IO
 
IO.setmode(IO.BCM)
IO.setup(4,IO.IN)#LDR sensor pin
IO.setup(2,IO.OUT) #GPIO 2 -> Red LED as output
IO.setup(3,IO.OUT) #GPIO 3 -> Green LED as output
IO.setup(22,IO.OUT) #GPIO 14 -> Buzzer as output

while True:
    #for i in range(0,5):
     stat=IO.input(4)
     if(1==stat):
         print("light on")
         IO.output(3,True) #Green led ON
         IO.output(22,True) #Buzzer ON
         IO.output(2,False) # Red led OFF
     else:
         print("light off")
         IO.output(2,True) #Red led ON
         IO.output(3,False) # Green led OFF
         IO.output(22,False) # Buzzer OFF
