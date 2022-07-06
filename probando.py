def fractional_part(numerator, denominator):
	if numerator == 0 or denominator = 0:
	# Operate with numerator and denominator to 
# keep just the fractional part of the quotient
		return 0
	else:
		num = numerator / denominator
		return num

print(fractional_part(5, 5)) # Should be 0
print(fractional_part(5, 4)) # Should be 0.25
print(fractional_part(5, 3)) # Should be 0.66...
print(fractional_part(5, 2)) # Should be 0.5
print(fractional_part(5, 0)) # Should be 0
print(fractional_part(0, 5)) # Should be 0