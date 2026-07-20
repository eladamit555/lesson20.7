# for loop is like while loop for specific range
from _pyrepl.commands import end

i = 1
print('while loop: ' , end='')
while i <= 10:
    print(i, end = ' ')
    i += 1
print()
# for loop include all 3 steps
# i = 1
# while i < 11
# i += 1
print('for loop:    ' , end = '')
for i in range(1, 10 + 1, +1):
    print(i, end = ' ')
print()
for i in range(3, 30 + 1, +3):
    print(i, end = ' ')
print()
for i in range(10, 1 - 1, -1):
    print(i, end = ' ')


#stop


