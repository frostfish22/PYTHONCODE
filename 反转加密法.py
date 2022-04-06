from fnmatch import translate


message = "Hello World!"
translate=""
i = len(message)-1
while i>=0:
    translate=translate+message[i]
    i-=1
print(translate)