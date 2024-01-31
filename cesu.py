def speeding_ticket(speed, is_birthday):
    if is_birthday == False:
        if speed <= 60:
            print ("no ticket")
        elif speed>= 61 and speed<= 80:
            print("small ticket")
        else:
            print("big ticker")
    else:
        if speed <= 65:
            print ("no ticket")
        elif speed>= 66 and speed<= 85:
            print("small ticket")
        else:
            print("big ticker")

speeding_ticket(60, False)
speeding_ticket(75, False)  # Expected output: "Small Ticket"
speeding_ticket(85, False)  # Expected output: "Big Ticket"
speeding_ticket(65, True)  # Expected output: "No Ticket"
speeding_ticket(85, True)  # Expected output: "Small Ticket"
