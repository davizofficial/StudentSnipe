# 🎯 StudentSnipe

![GitHub Repo stars](https://img.shields.io/github/stars/davizofficial/studentsnipe?style=flat-square)
![GitHub forks](https://img.shields.io/github/forks/davizofficial/studentsnipe?style=flat-square)
![GitHub last commit](https://img.shields.io/github/last-commit/davizofficial/studentsnipe?style=flat-square)
![License](https://img.shields.io/github/license/davizofficial/studentsnipe?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg?style=flat-square)



**StudentSnipe** is a lightweight and efficient CLI-based intelligence tool designed to retrieve public academic data of Indonesian university students based on full names. It supports academic research, OSINT exploration, and educational demonstration of public data systems.

Whether you're a researcher, student, journalist, or open-source investigator, StudentIntel helps you understand how structured public data can be accessed responsibly using simple and offline tools — without relying on heavy third-party libraries.


## 🔍 Why StudentSnipe?

In today's digital landscape, understanding how public academic records are exposed and structured is essential. **StudentSnipe** allows users to:

- Explore the public PDDIKTI dataset programmatically  
- Raise awareness on public information exposure  
- Build tools for educational or institutional research  
- Analyze student distributions and university records  

 **This is not a scraping or illegal harvesting tool** — StudentIntel mimics a user-facing search of publicly available records.


## 🚀 Features

- 🔎 Search student data by **Full Name**
- 🎓 Displays information including:
  - Full Name
  - Student ID (NIM)
  - Program of Study
  - University
  - Enrollment Status
- 📟 Interactive and clean CLI interface
- 💡 Open-source and modifiable
- 🧠 Ideal for academic analysis and ethical OSINT tasks


## 📥 Installation

### 🔧 Requirements

- Python 3.8 or higher  
- Git (optional)  
- Internet access (only to query the official public API)


### 🪟 Windows Setup

1. **Install Python**  
   Download from [python.org](https://www.python.org/downloads/windows/)  
   Ensure that **"Add Python to PATH"** is checked ✅ during installation.

2. **Clone the Repository**
   ```bash
   git clone https://github.com/davizofficial/studentsnipe.git
   cd studentsnipe
````

Or download ZIP and extract manually.

3. **Create Virtual Environment (Optional but Recommended)**

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

4. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Program**

   ```bash
   python main.py
   ```

### 🐧 Linux Setup (Debian/Ubuntu)

1. **Install Python**

   ```bash
   sudo apt update
   sudo apt install python3 python3-pip
   ```

2. **Clone the Repository**

   ```bash
   git clone https://github.com/davizofficial/studentsnipe.git
   cd studentsnipe
   ```

3. **Install Dependencies**

   ```bash
   pip3 install -r requirements.txt
   ```

4. **Run the Program**

   ```bash
   python3 main.py
   ```



## 🛡️ Legal & Ethical Disclaimer

This tool is developed solely for **educational and research purposes**.
All data processed and displayed is **publicly available** from the official PDDIKTI platform ([https://pddikti.kemdikbud.go.id](https://pddikti.kemdikbud.go.id)), and **no private or unauthorized information** is accessed.

> I do not encourage or support the use of this tool for cybercrime, illegal activities, or privacy violations. I believe this tool can be used responsibly and ethically for learning, academic exploration, and public data analysis.



## 🤝 Contributing

Feel free to submit issues, suggest features, fork the repository, or open pull requests. Contributions are welcome and appreciated.


## 👨‍💻 About the Developer

Built with a focus on education, responsible disclosure, and cybersecurity awareness.
This tool is a reminder of how public data should be handled thoughtfully in the digital age.
