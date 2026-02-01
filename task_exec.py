import os

# Define the contact information
contact_info = {
    "name": "John Doe",
    "email": "johndoe@email.com",
    "phone": "123-456-7890"
}

# Write the contact information to a text file
with open("contact_info.txt", "w") as file:
    file.write("Name: " + contact_info["name"] + "\n")
    file.write("Email: " + contact_info["email"] + "\n")
    file.write("Phone: " + contact_info["phone"] + "\n")

print("Contact information saved to contact_info.txt.")