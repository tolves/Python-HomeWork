def narcissistic(value):
 total = []
 number = len(str(value)) #Find the length of the value
 power = int(number) #convert the length back to integer datatype
 digits = [int(x) for x in str(value)] #convert value to string and loop through, convert back to int and store in digits
 for i in digits:
   product = i**power #loop through digits and multiply by the power
   total.append(product) #append the result of the operation to list total
   sumtotal = sum(total); 
 if(sumtotal == value):
    print ( str(value) + " is a narcisstic number")
 else:
    print( str(value) + " is not a narcisstic number")