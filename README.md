# Port-ScannerThis code uses a for loop to iterate through a range of ports specified by the start_port and end_port variables. For each port, it creates a new socket object and sets a 5 second timeout using the sock.settimeout() method. Then it uses the sock.connect_ex() method to check if the port is open.

If the result of sock.connect_ex() is 0, the code prints that the port is open. If the result is anything other than 0, the code prints that the port is closed. The sock.close() method is used to close the socket after each test.
