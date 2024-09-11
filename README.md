# 📄 Automated Warranty Generator

**Version:** 1.0  
**Author:** Gonzalo Patino  

The **Automated Warranty Generator** is a web-based application designed to streamline and automate the process of generating warranty documents across an organization. This solution eliminates the need for manual data entry and back-and-forth email communication, reducing human error and improving overall productivity by 60%.

Employees, especially in the shipping department, can easily generate warranty reports directly through this tool, without requiring technical knowledge or assistance.

---

## 🚀 Problem Statement

Before this tool, generating warranty documents involved manual data entry, leading to frequent human errors and inefficiencies. Team members often had to request warranty details via email, resulting in delays and unnecessary back-and-forth communication.

The **Automated Warranty Generator** solves this by allowing **any team member** to independently generate warranty reports, dramatically **improving efficiency** and **reducing human error**.

---

## 🌟 Solution Overview

This tool provides a fully automated way for employees to generate warranty reports for products. Users simply input the required details (e.g., sales order number, product information), and the tool automatically generates and provides a downloadable `.docx` report.

By implementing this tool:
- **Manual errors are minimized**.
- **Efficiency is increased by 60%**, significantly reducing the time spent on generating documents.
- **No email requests** are necessary, as employees can directly generate reports from the web interface.

---

## ✨ Key Features

- **Dynamic Report Generation**: Automatically generates `.docx` warranty reports with inputted data.
- **Warranty Period Calculation**: Automatically computes the warranty duration based on user input (Standard or Extended).
- **User-Friendly Interface**: Intuitive and accessible to anyone within the organization, especially useful for the shipping department.
- **File Download**: The system provides generated reports as downloadable `.docx` files.
- **Error-Free Automation**: Reduces human error by automating the entire process.
- **Efficient Session Management**: Saves session data to maintain user inputs throughout the process.

---

## 🛠 Technologies Used

- **Backend**: Python (Flask)
- **Frontend**: HTML, CSS, JavaScript (Datepicker, SweetAlert2)
- **Document Generation**: `python-docx` for dynamic Word document creation
- **PDF Generation** (Optional): `reportlab` for potential PDF support
- **Session Management**: Flask's built-in session handling

---

## 📦 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/automated-warranty-generator.git
   cd automated-warranty-generator
