# Flat Asterisk Pyramid

n = int(input())
rows = int(n/2)+1
for i in range(rows):
    stars = ""
    stars += "*"*(2*(i+1)-1)
    print(stars)