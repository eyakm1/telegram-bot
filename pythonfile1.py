n = int(input())
print(int((n - n % 100)/100 + (n % 100 - n % 10)/10 + n % 10))