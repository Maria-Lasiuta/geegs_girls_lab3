#John has 300 at the start, he saves 100 per month, and 500 every
#6 months. Write a function returning his savings after N months.
#(N is an input from the user)

def saving_s(months):
  n=0
  for x in range(months):#створюємо цикл
    if months//6:#якщо число місяців кратне 6
        n+=500 #додаємо до n 500                
        months-=6 #кожного разу віднімаємо,6
        #щоб порахувати вкладення за некратні шести місяців               
    else:
        n+=100 # +100 за кожні не кратні шести місяці 
  return n
c=int(input())
print(saving_s(c),"saved for {0} months".format(c))
