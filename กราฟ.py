import pandas as pd
import matplotlib.pyplot as plt

import matplotlib

# ตั้งค่าฟอนต์สำหรับภาษาไทย
plt.rcParams['font.family']='tahoma'

# การเชื่อมต่อ MySQL
username = 'myuser'
password = 'mypassword'
host = 'localhost'
database = 'mysql-docker'
db = f"mysql+mysqlconnector://{username}:{password}@{host}/{database}"


# SQL Query
query = '''SELECT
    MONTH(Service_Date) AS month, 
    COUNT(CASE WHEN TitleName IN ('นาย ','หญิง','นายแพทย์','แพทย์หญิง','นางสาว','ว่าที่ร้อยตรีหญิง')THEN 1  END) AS layperson,  
    COUNT(CASE WHEN TitleName IN ('พระภิกษุ ','พระมหา','พระปลัด','พระครูสมุห์','พระอธิการ','พระครูใบฎีกา','พระครูสังฆรักษ์','พระครูวนัยธร','สามเณร')THEN 1  END) AS Monk 
FROM clinicvisit
WHERE Service_Date BETWEEN '2020-01-01' AND '2024-12-31'
GROUP BY month
ORDER BY month
'''

# ดึงข้อมูลจาก MySQL
df = pd.read_sql(query, db)

