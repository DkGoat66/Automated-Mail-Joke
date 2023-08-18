import smtplib
import requests

MY_Email = "sabinarai2273@gmail.com"
My_Password="rvxmguiivvjiopug"

response = requests.get(url="https://api.chucknorris.io/jokes/random")
response.raise_for_status()
data = response.json()
joke = data["value"]
with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(MY_Email,My_Password)
    connection.sendmail(from_addr=MY_Email,
                        to_addrs="amazingsabina01@gmail.com",
                        msg=f"subject: Joke of the day!\n\n{joke}")
