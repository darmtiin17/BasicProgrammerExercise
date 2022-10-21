#input product to variable
product_name = input("input the product name : ")
#input amount of items
amount_items = int (input("how many items do you buy : "))
#input product pice to variable
price_product = int(input("input the price of product : ")) 
#set 10% variable
persen = int (input("input prrofit persentage : "))
#calcilate the persentage from the product price
sale_price = price_product *persen/100
#input total selling
total_selling = int (input("imput total selling your product : "))
# Print the final product price
print("sale price of your product (purchase price + profit) : " + str (sale_price+price_product))

#print spend
spend  = price_product * amount_items
print ("spend" , spend)
#print
print ("total_penjualan ", total_selling)
print ("total_pendapatan = ", total_selling*(sale_price+price_product))
print ("total_profit ", (total_selling*(sale_price+price_product)) - spend)
