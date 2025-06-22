from geopy.geocoders import Nominatim

# activate nominatim geocoder
# NOTE: replace "myGeoCoder" with your email ID if you get a HTTP Error 403.
locator = Nominatim(user_agent="myGeocoder")

# type any address text
location = locator.geocode("Harare, Zimbabwe")

print(location.raw.get("osm_id"))


print(location.raw)