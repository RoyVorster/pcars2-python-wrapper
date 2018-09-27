#include "Store.h"

Store::Store() : local(new SharedMemory), shared_memory_version(SHARED_MEMORY_VERSION) {
    map_file();
}

void Store::map_file() {
    file_handle = OpenFileMapping(PAGE_READONLY, FALSE, MAPPED_OBJECT);
    data = (SharedMemory*) MapViewOfFile(file_handle, PAGE_READONLY, 0, 0, sizeof(SharedMemory));
}

void Store::update() {
    if (data->mSequenceNumber%2) {
        step_size = data->mSequenceNumber - steps;
        steps = data->mSequenceNumber;

        memcpy(local, data, sizeof(SharedMemory));
    }
}

Store::~Store() {
    UnmapViewOfFile(data);
    CloseHandle(file_handle);

    delete local;
}