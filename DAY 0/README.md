# Simple Web Server Setup

This project demonstrates a simple web server running on an Azure Virtual Machine. It displays my name and photo using a basic HTML file, and includes command-line demonstrations recorded via Asciinema.

## Setup Instructions

### 1. Created `index.html`
A basic HTML file was created with the following content:

<html>
<body>
  <h1>Your Name:Pranavi<h1>
  <img src= "photo11.jpg" alt="photo11">
</body>
</html>
2. Transferred Photo
The image file photo11.jpg was transferred to the remote Azure VM using the VS Code Explorer drag-and-drop functionality. This allowed copying files from the local machine to the remote server without using SCP or CLI-based methods.

3. Started Web Server
A simple HTTP server was started using Python with the following command inside the terminal of the Azure VM:
python3 -m http.server 80

4. Accessed via Public IP
The web page was accessed by entering the public IP of the Azure Virtual Machine in a browser.
http://4.247.27.166/bootcamp/

5.Command-Line Application Demonstration
You can see a recording of the command-line actions, including navigating directories and starting the web server, in the following Asciinema recordings:

Web Server Setup Recording:
https://asciinema.org/a/K86gAnbSbuzspRdvkT1GBe2jP

Docker Demo Recording:
https://asciinema.org/a/pdvVf1HCSKUdZvECk74NTL8WM

6.Folder Structure

bootcamp/
 DAY 0/
    index.html
    photo11.jpg
    webserver.cast
    docker.cast
    README.md
    .gitignore

