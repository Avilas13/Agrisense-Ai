length_m = 120
width_m = 80
rain_mm = 12

area_m2= length_m*width_m
area_ha = area_m2/10000

water_litres = rain_mm * area_m2
water_m3 = water_litres/1000

print("Field area (m2):",area_m2)
print("Field area (ha):",area_ha)
print("Water from rain (litres):",water_litres)
print("Water from rain (m3):",water_m3)