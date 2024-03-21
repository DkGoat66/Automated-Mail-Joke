# Import necessary libraries
import smtplib  # Library for sending emails via SMTP
import requests  # Library for making HTTP requests

# Email credentials (Consider using environment variables for better security)
MY_Email = "sabinarai2273@gmail.com"
My_Password = "rvxmguiivvjiopug"  # This should be an app-specific password or secured differently

# Make an HTTP GET request to the Chuck Norris joke API
response = requests.get(url="https://api.chucknorris.io/jokes/random")
response.raise_for_status()  # Raise an error for bad responses
data = response.json()  # Parse the JSON response into a Python dictionary
joke = data["value"]  # Extract the joke text from the response

# Use smtplib to send an email
with smtplib.SMTP("smtp.gmail.com", port=587) as connection:  # Open a connection to the Gmail SMTP server
    connection.starttls()  # Upgrade the connection to secure TLS/SSL
    connection.login(MY_Email, My_Password)  # Log in to the SMTP server
    # Send an email from MY_Email to a specified receiver with the joke as the message
    connection.sendmail(from_addr=MY_Email,
                        to_addrs="amazingsabina01@gmail.com",  # Recipient's email address
                        msg=f"subject: Joke of the day!\n\n{joke}")  # Email subject and body
