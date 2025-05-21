readme_md = """
# Bootcamp Setup — DAY 0

This project serves as the initial setup verification for the bootcamp. It demonstrates:

* Running a basic web server on a Linux VM (Azure)
* Displaying a simple HTML page with name and photo
* Setting up Docker and testing a Python container
* Recording CLI demos using Asciinema


---

## 🌐 Live Web Page

The web page displays my name and a photo using a simple HTML file hosted on an Azure VM.

🔗 [http://4.247.27.166/bootcamp/](http://4.247.27.166/bootcamp/)

---

## 🛠 Tools & Prerequisites

* **GitHub**: Version control for all bootcamp exercises
* **Azure VM**: Ubuntu Linux server for app hosting
* **Python 3.11 & 3.13**: Installed using uv and pyenv
* **Docker**: Installed and tested with a Python image
* **Asciinema**: CLI screen recording
* **VSCode / PyCharm**: IDE for development
* **SSH Keys**: Configured for both GitHub and VM access
* **rsync / scp**: Used for syncing files between local and VM

---

## 📁 Folder Structure

\`\`\`
bootcamp/
└── DAY 0/
    ├── index.html          # Web page with name and photo
    ├── photo11.jpg         # My photo
    ├── webserver.cast      # Asciinema recording: Web server setup
    ├── docker.cast         # Asciinema recording: Docker demo
    ├── README.md           # This file
    └── .gitignore
\`\`\`

---

## ⚙️ Setup Instructions

### 1. Created index.html

\`\`\`html
<html>
  <body>
    <h1>Your Name: Pranavi</h1>
    <img src="photo11.jpg" alt="photo11">
  </body>
</html>
\`\`\`

### 2. Transferred Files to VM

Transferred index.html and photo11.jpg to the Azure VM using:

* VS Code Explorer drag-and-drop
* Or scp command (if applicable)

### 3. Started Web Server

Ran a simple Python HTTP server inside the Azure VM:

\`\`\`bash
python3 -m http.server 80
\`\`\`

### 4. Accessed Web Page via Public IP

Navigated to the public IP in a browser:

🔗 [http://4.247.27.166/bootcamp/](http://4.247.27.166/bootcamp/)

### 5. Installed Docker & Ran Python Container

\`\`\`bash
sudo apt update
sudo apt install docker.io
sudo docker pull python
sudo docker run python python -c "print('Hello, World!')"
\`\`\`

---

## 🎥 CLI Demo Recordings (Asciinema)

* **Web Server Setup**: [Web Server Recording](https://asciinema.org/a/K86gAnbSbuzspRdvkT1GBe2jP)
* **Docker Hello World**: [Docker Recording](https://asciinema.org/a/pdvVf1HCSKUdZvECk74NTL8WM)

> Replace the <webserver-cast-id> and <docker-cast-id> with your actual Asciinema recording IDs.

---

## 📌 Notes

* SSH key-based access configured for GitHub and VM
* rsync and scp used for file transfers
* Python virtual environments managed using uv
* IDE used: PyCharm (with proper interpreter setup)

---

## 🔗 Useful Resources

* [GitHub Education Pack](https://education.github.com/pack)
* [Free DNS](https://freedns.afraid.org/)
* [Asciinema](https://asciinema.org/)
* [uv (Python packaging)](https://github.com/astral-sh/uv)

---

## ✅ Status

- GitHub Repo Setup  
- Azure VM Provisioned  
- SSH Key Setup  
- Web Server Running  
- Docker Installed & Tested  
- CLI Demos Recorded

---

## ✅ GitHub Repo Setup

### What We’ve Done:
- Created a GitHub repository named \`bootcamp\` containing all the necessary files for the bootcamp tasks.


- Created a GitHub repository named `bootcamp` containing all the necessary files for the bootcamp tasks.

### Installation Steps:
1. **Create a GitHub Account** (if you don’t have one already): [GitHub Sign Up](https://github.com/)
2. **Create a Repository**:
   - Go to your GitHub profile.
   - Click on \`+\` in the upper-right corner and select **New Repository**.
   - Name the repository \`bootcamp\`, select **Public** or **Private**, and click **Create repository**.
3. **Clone the Repository to Your Local Machine**:
   \`\`\`bash
   git clone https://github.com/<your-github-username>/bootcamp.git
   \`\`\`
4. **Push Files**:
   - Add your files (like \`index.html\`, \`photo11.jpg\`, \`webserver.cast\`, \`docker.cast\`) to the repository.
   - Commit the changes and push to GitHub:
     \`\`\`bash
     git add .
     git commit -m "Initial commit"
     git push origin main
     \`\`\`

---

## ✅ Azure VM Provisioned

### What We’ve Done:
- Set up an Azure VM running Ubuntu Linux and hosted the web server on it.

### Installation Steps:
1. **Create an Azure Account** (if you don’t have one already): [Azure Sign Up](https://azure.microsoft.com/)
2. **Create a Virtual Machine**:
   - Sign in to the Azure portal.
   - Go to **Virtual Machines** and click on **Create**.
   - Select **Ubuntu** as the OS and configure the VM according to your preferences (size, region, etc.).
3. **SSH Access**:
   - Generate an SSH key pair if you don’t have one:
     \`\`\`bash
     ssh-keygen -t rsa -b 2048 -f ~/.ssh/azure_key
     \`\`\`
   - Add the public key to the Azure VM creation process.
   - Once the VM is created, you can SSH into it:
     \`\`\`bash
     ssh -i ~/.ssh/azure_key <your-vm-public-ip>
     \`\`\`

---

## ✅ SSH Key Setup

### What We’ve Done:
- Configured SSH key-based authentication for GitHub and Azure VM access.

### Installation Steps:
1. **Generate SSH Keys** (if not already done):
   \`\`\`bash
   ssh-keygen -t rsa -b 2048 -f ~/.ssh/id_rsa
   \`\`\`
2. **Add SSH Key to GitHub**:
   - Go to [GitHub SSH settings](https://github.com/settings/keys).
   - Click **New SSH Key**, paste your public key (\`~/.ssh/id_rsa.pub\`), and save it.
3. **Add SSH Key to Azure VM**:
   - When creating the VM, paste the public key into the **SSH public key** field, or manually copy it to \`~/.ssh/authorized_keys\` on the VM after SSH-ing in.

---

## ✅ Web Server 

### What We’ve Done:
- Started a basic Python HTTP server to serve the \`index.html\` file on the Azure VM.

### Installation Steps:
1. **Install Python (if not already installed)**:
   \`\`\`bash
   sudo apt update
   sudo apt install python3
   \`\`\`
2. **Upload Files to the VM**:
   - You can use **VS Code**'s Explorer to drag and drop files, or use **scp**:
     \`\`\`bash
     scp index.html photo11.jpg <your-vm-user>@<your-vm-ip>:/home/<your-vm-user>/bootcamp/
     \`\`\`
3. **Start the Web Server**:
   - SSH into your Azure VM.
   - Run the Python HTTP server:
     \`\`\`bash
     cd /home/<your-vm-user>/bootcamp/
     python3 -m http.server 80
     \`\`\`
4. **Access the Web Page**:
   - Open a browser and go to \`http://<your-vm-public-ip>/bootcamp/\` to see the web page.

---

## ✅ Docker Installed & Tested

### What We’ve Done:
- Installed Docker on the Azure VM and ran a Python container.

### Installation Steps:
1. **Install Docker**:
   \`\`\`bash
   sudo apt update
   sudo apt install docker.io
   sudo systemctl enable --now docker
   \`\`\`
2. **Verify Docker Installation**:
   \`\`\`bash
   docker --version
   \`\`\`
3. **Pull the Python Docker Image**:
   \`\`\`bash
   sudo docker pull python
   \`\`\`
4. **Run Python in Docker Container**:
   \`\`\`bash
   sudo docker run python python -c "print('Hello, World!')"
   \`\`\`

---

## ✅ CLI Demos Recorded

### What We’ve Done:
- Recorded terminal sessions using Asciinema for both setting up the web server and testing Docker.

### Installation Steps:
1. **Install Asciinema**:
   \`\`\`bash
   sudo apt install asciinema
   \`\`\`
2. **Record the Web Server Setup**:
   \`\`\`bash
   asciinema rec webserver.cast
   \`\`\`
   - Perform the setup and press \`Ctrl+D\` to stop recording.
3. **Record the Docker Demo**:
   \`\`\`bash
   asciinema rec docker.cast
   \`\`\`
   - Run the Docker commands and press \`Ctrl+D\` to stop recording.
4. **Upload the Recordings**:
   - After finishing, follow the on-screen URL or run:
     \`\`\`bash
     asciinema upload webserver.cast
     asciinema upload docker.cast
     \`\`\`
