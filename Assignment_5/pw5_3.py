import requests

# Input the latitude and longitude data
lat = input("Enter latitude: ")
lon = input("Enter longitude: ")

# Make a request to Nominatim API for reverse geocoding
url = f"https://nominatim.openstreetmap.org/reverse?lat={lat}&lon={lon}&format=json"
response = requests.get(url).json()

# Extract the required information from the response
place = response["display_name"]
type = response.get("type", "N/A")
address = response["address"]
house_number = address.get("house_number", "N/A")
street = address.get("road", "N/A")
city = address.get("city", "N/A")
postcode = address.get("postcode", "N/A")
country = address.get("country", "N/A")
country_code = address.get("country_code", "N/A")

# Print the extracted information
print("Place: ", place)
print("Type: ", type)
print("House Number: ", house_number)
print("Street Name: ", street)
print("City: ", city)
print("Postcode: ", postcode)
print("Country: ", country)
print("Country Code: ", country_code)
