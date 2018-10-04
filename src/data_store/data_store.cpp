#include "data_store.hpp"

DataStore::DataStore() : _shared_data(new SharedMemory)
{
}

SharedMemory* DataStore::get_shared_data() {
    return _shared_data;
}

void DataStore::set_windspeed(float windspeed) {
    _shared_data->mWindSpeed = windspeed;
}
