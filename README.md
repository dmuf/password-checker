
### **📌 Updated README.md**  

```md
# Password Strength Checker 🔐  

A Python tool that checks password strength and security. It analyzes passwords for complexity, length, and whether they have been exposed in **data breaches** using the Have I Been Pwned API.  

## 🚀 Features  
✔️ Analyzes password length and complexity  
✔️ Detects common words and patterns  
✔️ Provides real-time feedback on password strength  
✔️ **Checks if your password has been leaked in a data breach** 🔥  
✔️ GUI version with a "Show Password" button  

## 🛠️ Installation  
1. **Clone the repository**  
```sh
git clone https://github.com/dmuf/password-checker.git
```
2. **Navigate to the project folder**  
```sh
cd password-checker
```
3. **Install dependencies**  
```sh
pip install -r requirements.txt
```
4. **Run the script**  
```sh
python password_checker.py
```

## 🔒 How the Breach Check Works  
- This tool **does NOT send your actual password** to the Have I Been Pwned API.  
- Instead, it uses **k-Anonymity** to send only a **partial hash** of your password.  
- This ensures **privacy** while checking if your password has appeared in data breaches.  

## 📸 Screenshots  
![image](https://github.com/user-attachments/assets/fc8e2f84-8701-4b51-bddf-72280ba97d30)

![image](https://github.com/user-attachments/assets/01e0397f-6106-49f8-85ed-fec6e68d62bf)

## 📝 License  
This project is licensed under the MIT License.  
