a = int(input())
if(a<18):
    print("You are minor")
elif(a>18 or a<65):
    print("You are an adult")
elif(a==65 or a>65):
    print("You are a senior citizen")