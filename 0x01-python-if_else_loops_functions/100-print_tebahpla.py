<<<<<<< HEAD
#!/usr/bin/python3

i = 0
for c in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(c - i)), end="")
=======
#!/usr/bin/python3

i = 0
for c in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(c - i)), end="")
>>>>>>> 83fbf461d908931f0d3bb5ca190063f6201376ff
    i = 32 if i == 0 else 0