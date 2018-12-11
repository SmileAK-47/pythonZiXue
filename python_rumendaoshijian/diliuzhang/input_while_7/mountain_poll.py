responses = {}
polling_active= True
while polling_active:
    name = input("\nwhat is you name:")
    response = input("\n you see mountain")
    responses[name] = response

    repeat = input("how you like another r?(yes/no)")
    if repeat == "no":
        polling_active = False
print("\n----poll Results---")
for name,response in responses.items():
    print(name + "would like to climb "+ response +".")