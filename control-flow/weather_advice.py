current_weather = str(input("What's the weather like today? (sunny/rainy/cold): "))
choice = current_weather.lower()
if choice  == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif choice  == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif choice  == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")
