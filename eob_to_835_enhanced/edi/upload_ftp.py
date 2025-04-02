
import os
from ftplib import FTP

def upload_edi_to_ftp(file_path, file_name):
    ftp = FTP()
    ftp.connect(os.getenv("FTP_HOST"))
    ftp.login(user=os.getenv("FTP_USER"), passwd=os.getenv("FTP_PASS"))
    ftp.cwd(os.getenv("FTP_DIR", "/"))
    with open(file_path, 'rb') as f:
        ftp.storbinary(f'STOR {file_name}', f)
    ftp.quit()
    return f"ftp://{os.getenv('FTP_HOST')}/{file_name}"
