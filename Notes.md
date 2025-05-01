# Resolving Network.py Returning None Issue

I encountered an issue where running `network.py` returned `None` after starting `server.py`. The problem was resolved by configuring my firewall to allow TCP connections to the specified port.

## Steps to Configure a Port (Windows)

1. Click the **Start** button and type `run`. Open the **Run** application.
2. Type `wf.msc` and press **OK**.
3. In the left-hand panel, click on **Inbound Rules**.
4. In the right-hand panel, click **New Rule**.
5. Select **Port** and click **Next**.
6. Choose **TCP** and **Specific local ports**. Enter the port number you want to allow.
7. Select **Allow the connection** and complete the setup.