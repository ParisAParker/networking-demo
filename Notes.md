I ran into an error after running my server.py then running network.py. When I ran network.py, it was returning none. I had to configure my firewall to allow TCP connections to a port I specified

- Steps to configuring port (On Windows)
1. Click start button and type "run". Click on application
2. Type in wf.msc and press "OK"
3. In the left hand corner click on "Inbound Rules"
4. In the right side, click "New Rule"
5. Select "Port" click Next
6. Select "TCP" and "Specific local ports". Type in the port you want to allow the connection
7. Select "Allow the connection"