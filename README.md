# **README – Automation Projects**

## 📌 Project Overview

This repository contains two automation projects developed using **Python** and **Bash (WSL)** integrated with **AWS services**.
The projects demonstrate system automation, cloud integration, and monitoring capabilities.

---

## **1. Automated Backup Solution (Python + AWS S3)**

### 🔹 Objective

To automate the backup of a specified local directory by compressing it and uploading it to **AWS S3**. The script also logs success and failure of each backup operation.

### 🔹 Features

* Compresses a specified folder into a **timestamped ZIP**.
* Uploads the ZIP file to an **AWS S3 bucket**.
* Generates a **log file (`backup_log.txt`)** containing timestamps and results.
* Can be automated with **Windows Task Scheduler** for periodic backups.

### 🔹 Technologies Used

* **Python** (`boto3`, `zipfile`, `datetime`)
* **AWS S3** for cloud storage
* **Windows Task Scheduler** for automation

### 🔹 Setup & Execution

1. Install dependencies:

   ```bash
   pip install boto3
   ```
2. Configure AWS credentials in the script.
3. Run the script:

   ```bash
   python backup_to_s3.py
   ```
4. Check your **S3 bucket** for uploaded backup ZIPs.
5. Logs are stored in `backup_log.txt`.

## S3 Bucket
Uploaded backup ZIP files stored securely in AWS S3.

![s3 Bucket](Images_Proof/1.png)

## Python Script
Terminal output showing successful backup and upload process.

![Python Script](Images_Proof/4.png)

---

## **2. Application Health Checker (Bash + AWS SNS)**

### 🔹 Objective

To check the uptime of an application (website) and determine if it is **functioning (UP)** or **not responding (DOWN)**. The script logs results and sends email alerts via **AWS SNS**.

### 🔹 Features

* Uses **cURL** to check HTTP response codes.
* Logs results with timestamps into `app_health_log.txt`.
* Sends **SNS email alerts** if the application is DOWN.
* Runs in **WSL (Windows Subsystem for Linux)**.
* Can be scheduled using **cron jobs** for periodic checks.

### 🔹 Technologies Used

* **Bash Script (WSL)**
* **AWS SNS** for email notifications
* **cURL** for HTTP status checking

### 🔹 Setup & Execution

1. Create an **SNS topic** in AWS and subscribe your email.
2. Install AWS CLI and configure credentials:

   ```bash
   aws configure
   ```
3. Make script executable:

   ```bash
   chmod +x app_health_checker.sh
   ```
4. Run the script:

   ```bash
   ./app_health_checker.sh
   ```
5. If the site is **DOWN**, you’ll receive an **email alert** from SNS.

## Health Checker Script
Bash script code for monitoring application uptime.

![Bash Script](Images/3.png)

## Terminal & Alert
Script execution results with uptime status and email alert trigger.

![Terminal](Images/4.png)

---

## ✅ Conclusion

* **Project 1 (Backup Solution):** Ensures reliable backups of important data to **AWS S3**.
* **Project 2 (Health Checker):** Provides automated monitoring and alerting for web applications.

These projects demonstrate the integration of **Python, Bash, and AWS services** to achieve **automation, reliability, and monitoring** in real-world scenarios.

---

