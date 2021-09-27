#John has 300 at the start, he saves 100 per month, and 500 every
#6 months. Write a function returning his savings after N months.
#(N is an input from the user)

def saving_s(months):#створюємо функцію
  n = 300
  for x in range(months):#створюємо цикл
    if months // 6:#якщо число місяців кратне 6
        n += 500 #+500                
        months -= 6 #кожного разу віднімаємо 6,щоб порахувати
        #вкладення за некратні шести місяці повертаючись до else              
    else:
        n += 100 # +100 за кожні не кратні шести місяці 
  return n
c=int(input('Enter the number of months: '))
print(saving_s(c),"saved for {0} months".format(c))
