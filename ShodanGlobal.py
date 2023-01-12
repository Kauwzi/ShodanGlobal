import folium
import shodan

# Replace YOUR_API_KEY with your Shodan API key
SHODAN_API_KEY = "YOUR_API_KEY"

# Replace YOUR_USER_ID and YOUR_LICENSE_KEY with your GeoIP2 credentials
GEOIP2_USER_ID = "YOUR_USER_ID"
GEOIP2_LICENSE_KEY = "YOUR_LICENSE_KEY"

# Create a Shodan object
api = shodan.Shodan(SHODAN_API_KEY)

# Create a GeoIP2 object
geoip2_client = geoip2.webservice.Client(GEOIP2_USER_ID, GEOIP2_LICENSE_KEY)

# Create a map object
map = folium.Map()

# Perform the search
try:
    query = "Your search query"
    result = api.search(query)

    # Add markers for all IP addresses
    for service in result['matches']:
        ip = service['ip_str']
        try:
            response = geoip2_client.insights(ip)
            lat = response.location.latitude
            lon = response.location.longitude
            folium.Marker([lat, lon], popup=ip).add_to(map)
        except Exception as e:
            print(f"Error getting location for IP {ip}: {e}")

    # Save the map to an HTML file
    map.save("map.html")

except shodan.APIError as e:
    print("Error: {}".format(e))
