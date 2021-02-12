# HTTP Benchmarck - Client 

This program uses wrk (https://github.com/wg/wrk) as a benchmarking tool.

We will be using wrk like this :

```./wrk -t12 -c400 -d30s URL```

with *URL* being the url of our server.

This repository also contains the *test.py* script that launch the wrk executable from this repository with the correct arguments.

The wrk binary from this repository has been compiled from an intel macbook pro. It might not work on other os. You should then clone the original wrk and build it then move the executable to this folder or simply use it from the src folder.