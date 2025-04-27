import art1


def find_highest_bidder(bid):
    highest_bid = 0
    winner = ""
    for i in bid:
        bid_amount = bid[i]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = i
    print(f"The winner is {winner} with a bid of ${highest_bid}")


bid_info = {}
print(art1.logo)
while True:
    name= input("What is your name ? ")
    bid = input("What is your bid($) ? ")
    bid_info[name] = bid
    choice = input("Would you like to add another bid? (Y/N) ")
    if choice.upper() == 'N':
        find_highest_bidder(bid_info)
        break
    elif choice.upper() == "yes":
        print("\n" * 20)