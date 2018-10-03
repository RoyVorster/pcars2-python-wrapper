import boost_lib

store = boost_lib.DataStore()
data = store.get_shared_data()

print(data.mWindSpeed)

store.set_windspeed(100)
print(data.mWindSpeed)
