import finnhub

finnhub_client = finnhub.Client(api_key="YOUR_API_KEY")

chosen_stock = input("Enter the stock ticker of the stock you wish to see the price of: ")

print(finnhub_client.quote(chosen_stock))

input("Thank you for using my calculator! Press enter to exit")
