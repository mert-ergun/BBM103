n = int(input('Enter the number N value:'))

stars = {x: x*['*'] for x in range(1,n+1)}

print(stars)