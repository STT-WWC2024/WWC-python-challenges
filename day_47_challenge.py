# Create a program that imports the math module and uses its functions.

import math

x = 5.6
ans_ceil = math.ceil(x)
ans_floor = math.floor(x)
print(f"The ceil of {x} is: {ans_ceil}")
print(f"The floor of {x} is: {ans_floor}")

x = 8
ans_factorial = math.factorial(x)
print(f"The factorial of {x} is {ans_factorial}")

x = 9
y = 30
ans_gcd = math.gcd(x, y)
print(f"The gcd of {x} and {y} is: {ans_gcd}")

x = -24
ans_fabs = math.fabs(x)
print(f"The absolute value of {x} is: {ans_fabs}")

x = 8
print (f"Euler's number, e, raised to the power of x is: {math.exp(x)}")

x = 2
y = 3
ans_pow = math.pow(x, y)
print(f"{x} to the power of {y} is: {ans_pow}")

x = 2
b = 3
ans_log = math.log(x, b)
print(f"Value of log {x} with base {b} is: {ans_log}")

x = 8
ans_log = math.log2(x)
print(f"Value of log2 of {x} is: {ans_log}")

x = 10000
ans_log = math.log10(10000)
print(f"The value of log10 of {x} is: {ans_log}")

x = 25
ans_log = math.sqrt(x)
print(f"The square root of {x} is: {ans_log}")

# et cetera
# --- additional functions ---
# math.copysign(x,y)
# math.fmod(x,y)
# math.frexp(x)
# math.fsum(iterable)
# math.isfinite(x)
# math.isinf(x)
# math.isnan(x)
# math.ldexp(x, i)
# math.modf(x)
# math.trunc(x)
# math.expm1(x)
# math.log1p(x)
# math.acos(x)
# math.asin(x)
# math.atan(x)
# math.cos(x)
# math.hypot(x,y)
# math.sin(x)
# math.tan(x)
# math.degrees(x)
# math.radians(x)
# math.acosh(x)
# math.asinh(x)
# math.atanh(x)
# math.cosh(x)
# math.sinh(x)
# math.tanh(x)
# math.erf(x)
# math.erfc(x)
# math.gamma(x)
# math.lgamma(x)