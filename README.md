The client.py and the server.py has a simple cli. Please provide a valid host IP address and a port number through this cli.

Example:

"python server.py -host 127.0.0.1 -port 11111"

"python client.py -host 127.0.0.1 -port 11111"

The provided IP address and port number should be the same. It's servers IP and port, which is used in the TCP communication.

The client.py generates a graph.png image as a data visualization, the client refreshes this image every time it recieve a batch of data.
If you open the graph.html in your browser, it shows the image file and refresshes itself when a new image has been saved. 
