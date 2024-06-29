#!/usr/bin/env python3
amount_to_pay=input("Enter the amount to pay: ")
print("")

tip1=0.15
tip2=0.20
tip3=0.22

tip_1=float(amount_to_pay)*tip1
tip_2=float(amount_to_pay)*tip2
tip_3=float(amount_to_pay)*tip3

total1=float(amount_to_pay)+tip_1
total2=float(amount_to_pay)+tip_2
total3=float(amount_to_pay)+tip_3


print(f"15% tip: {tip_1}")
print(f"20% tip: {tip_2}")
print(f"22% tip: {tip_3}")
print("")
print(f"Total amount with 15% tip: {total1}")
print(f"Total amount with 20% tip: {total2}")
print(f"Total amount with 22% tip: {total3}")

