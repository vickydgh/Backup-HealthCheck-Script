import os
import boto3
from botocore.exceptions import NoCredentialsError
from datetime import datetime
import zipfile
import os

LOCAL_DIR = r"Path-To-Your-Directory"
BUCKET_NAME = "your-bucket-name"
AWS_ACCESS_KEY = os.getenv("your-access-key")
AWS_SECRET_KEY = os.getenv("your-secret-key")
LOG_FILE = "backup_log.txt"

# Logs messages to console and file
def log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(message)
    with open(LOG_FILE, "a") as f:
        f.write(f"{timestamp} - {message}\n")

# Compress folder to a zip file
def zip_folder(folder_path):
    zip_name = f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.zip"
    zip_path = os.path.join(os.getcwd(), zip_name)
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, folder_path)
                zipf.write(file_path, arcname)
    return zip_path

# Uploads file to S3 bucket
def upload_to_s3(file_path):
    try:
        s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY,
                          aws_secret_access_key=AWS_SECRET_KEY)
        s3.upload_file(file_path, BUCKET_NAME, os.path.basename(file_path))
        log(f"Backup successful: {os.path.basename(file_path)} uploaded to {BUCKET_NAME}")
    except FileNotFoundError:
        log("Error: File not found.")
    except NoCredentialsError:
        log("Error: AWS credentials not available.")
    except Exception as e:
        log(f"Error: {e}")

if __name__ == "__main__":
    log("Backup process started.")
    zip_file = zip_folder(LOCAL_DIR)
    upload_to_s3(zip_file)
    log("Backup process finished.")
