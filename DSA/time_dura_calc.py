# hour = int(input("Starting time (hours): "))
# mins = int(input("Starting time (minutes): "))
# dura = int(input("Event duration (minutes): "))

# Write your code here.
hour, mins, dura = 12,17,59
# hour, mins, dura = 0,1,2939

hour = (hour+dura//60 + (mins+dura%60)//60)%24
mins = (mins+dura%60)%60
print(hour,mins,sep=":")
