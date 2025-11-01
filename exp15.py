

def decision_tree(outlook, humidity, wind):
    if outlook == "sunny":
        if humidity == "high":
            return "No"
        else:
            return "Yes"
    elif outlook == "overcast":
        return "Yes"
    elif outlook == "rain":
        if wind == "strong":
            return "No"
        else:
            return "Yes"

outlook = input("Enter outlook (sunny/overcast/rain): ")
humidity = input("Enter humidity (high/normal): ")
wind = input("Enter wind (strong/weak): ")
print("Play Tennis Decision:", decision_tree(outlook, humidity, wind))
