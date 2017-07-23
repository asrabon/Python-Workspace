import pandas
from geopy.geocoders import Nominatim

df = pandas.read_csv("supermarkets.csv")
df["Addres"] = df["Address"] + "," + df["City"] + "," + df["State"]
df
nom = Nominatim()

df["coordinates"] = df["Address"].apply(nom.geocode)
df["Longitude"] = df["coordinates"].apply(lambda x: x.longitude if x != None else None)
df["Latitude"] = df["coordinates"].apply(lambda x: x.latitude if x != None else None)
df = df.drop(df.columns[7:9],1)

df
