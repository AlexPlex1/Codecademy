weight = 41.5
# Ground Shipping
if weight <= 2:
  cost = 1.5 * weight + 20
elif weight <= 6:
  cost = 3 * weight + 20
elif weight <= 10:
  cost = 4 * weight + 20
else :
  cost = 4.75 * weight + 20
print("Cost of ground shipping $", round(cost, 2))

premium_ground_shipping = 125
print("Premium Groudn Shipping $", premium_ground_shipping)

# Drone Shipping
if weight <= 2:
  cost = 4.5 * weight
elif weight <= 6:
  cost = 9 * weight
elif weight <= 10:
  cost = 12 * weight
else :
  cost = 14.25 * weight
print("Cost of drone shipping $", round(cost, 2))
