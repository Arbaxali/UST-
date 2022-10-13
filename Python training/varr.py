#Create a program which will swap the variables without using third variable
temp1 = 12
temp2 = 5

temp1 = temp1 +temp2
temp2 = temp1 - temp2 
temp1 =temp1 - temp2

print(temp1)
print(temp2)




#Suppose you have 100 apples with 7.5 rs each and you have sold 20 apples at 10rs , 30 apples at 50 rs calculate the profit/loss
#for the shopkeeper. Find out how many apples he can purchase with the earned amount.

apples  = 100
net_cost  =7.5 
net_invest = apples * net_cost
apples_cost_1 = 10
apples_sold_1 = 20
amount_1 = apples_cost_1 * apples_sold_1

apples_cost_2 = 50
apples_sold_2 = 30
amount_2 = apples_sold_2 * apples_cost_2

total_profit = (amount_1 + amount_2) - net_invest

print("profit from selling apples",total_profit)
print("amount of apples can be purchased", total_profit/net_cost)