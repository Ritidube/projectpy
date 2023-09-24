def displayWelcome():
    print("this program will determine the time to pay off a credit")
    print("card and the interest paid based on the current balance")
    print("the interst rate and the monthly payment made")

def displayPayments(balance,int_rate,monthly_payement):
    num_months=0
    total_int_paid=0
    payment_num=1
    empty_year_field=format('','8')
    print('\n', format ('PAYOFF SCHEDULE','>20')) 
    print(format ('Year','>10')+format('Balance','>10')+format('Payment Num', '>14') +format('Interest Paid','>16'))

# display year-by-year account status while balance > 0:
    while balance > 0:
      monthly_int=balance*int_rate 
      total_int_paid=total_int_paid + monthly_int
      balance = balance + monthly_int - monthly_payment

      if balance < 0:
       balance = 0

      if num_months % 12 == 0:
       year_field= format(num_months // 12 + 1, '>8')

      else:
        year_field= empty_year_field

      print (year_field + format(balance, '>12,.2f')+format (payment_num,'>9') + format (total_int_paid, '>17,.2f'))

      payment_num= payment_num + 1

      num_months =num_months + 1
    

displayWelcome()
balance=int(input("\nEnter the balance on your credit card: ")) 
apr=int(input("Enter the interest rate (APR) on the card:"))

monthly_int_rate=apr/1200

yes_response=('y', 'Y') 
no_response=('n', 'N')

calc=True 
while calc:
  if balance < 1000:
    min_monthly_payment=20
  else:
    min_monthly_payment=balance *.02

  print ("\nAssuming a minimum payment of 2% of the balance ($20 min)")
  print("Your minimum payment would be", format(min_monthly_payment,'.2f'),'\n')
  response=input('Use the minimum monthly payment? (y/n): ')
  while response not in yes_response + no_response: 
     response = input('Use the minimum monthly payment? (y/n): ')

  if response in yes_response: 
    monthly_payment=min_monthly_payment 
  else: 
    acceptable_payment=False

    while not acceptable_payment:
       monthly_payment=int(input("\nEnter monthly payment: "))
       if monthly_payment < balance*.02: 
         print('Minimum payment of 2% of balance required ($' + str(balance*.02) + ')') 
       elif monthly_payment < 20: 
         print ("Minimum payment of $20 required")

       else:
        acceptable_payment = True
  if monthly_payment>=balance:
    print('*this payment amount would pay off your balance*')
  else:
    displayPayments(balance,monthly_int_rate,monthly_payment)
    again=input('\nRecalculate with another payment?(y/n)')
    while again not in yes_response + no_response:
      again=input('Recalculate with another payments?(y/n):')
    if again in yes_response:
      calc=True
      print('\n\nFor your currrent balance of$'+ str(balance))
    else:
      calc=False             