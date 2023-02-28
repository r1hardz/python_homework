def compute_salary(hours,rate):
    if (hours > 40):
        extraHours = hours - 40
        increasedRate = rate * 1.75
        basePayment = 40 * rate
        extraPayment = extraHours * increasedRate
        total = basePayment + extraPayment
    else:
        total = hours * rate
    print("Pay: " + str(total))

if __name__ == "__main__":
    while True:
        try:
            hours = float(input("Enter hours: "))
            rate = float(input("Enter rate: "))
            compute_salary(hours,rate)
            break
        except ValueError:
            print("Error, please enter numeric input")
            continue
