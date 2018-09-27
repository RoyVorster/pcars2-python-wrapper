# Project Cars 2 python wrapper
A simple C++ class handling the memory mapping (please note that this, as a consequence of pcars2's design, only works on windows) is later wrapped by a simple python script. Libclang is used to autogenerate ctype bindings.

### Use
This wrapper is just for the data transfer, it provides little more than an interface. There are well-known python frameworks for making real-time dashboard or simple plotting/analyzing data afterwards.