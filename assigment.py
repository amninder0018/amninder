def collect_user_details():
    user_details = {}

    # Collecting user input
    user_details['Name'] = input("Enter your name: ").strip()

    while True:
        phone = input("Enter your phone number: ").strip()
        if phone.isdigit() and (7 <= len(phone) <= 15):
            user_details['Phone'] = phone
            break
        else:
            print("Invalid phone number. Please enter digits only (7-15 characters).")

    while True:
        email = input("Enter your email: ").strip()
        if '@' in email and '.' in email:
            user_details['Email'] = email
            break
        else:
            print("Invalid email format. Please try again.")

    user_details['State'] = input("Enter your state: ").strip()
    user_details['Country'] = input("Enter your country: ").strip()

    while True:
        pincode = input("Enter your pincode: ").strip()
        if pincode.isdigit() and len(pincode) in [5, 6]:
            user_details['Pincode'] = pincode
            break
        else:
            print("Invalid pincode. It should be 5 or 6 digits.")

    # Display collected data
    print("\nCollected User Details:")
    for key, value in user_details.items():
        print(f"{key}: {value}")

    return user_details


# Call the function to collect details
if __name__ == "__main__":
    collect_user_details()
