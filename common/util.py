import os
import random
import time
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Protocol.KDF import scrypt
from common.read_data import data
import base64

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_file_path = os.path.join(BASE_PATH, "config", "setting.ini")
file_data = data.load_ini(data_file_path)
appkey = file_data["headerConf"]["appkey"]
password = file_data["headerConf"]["password"]

def encryption_password(key, password):
    
    key_bytes = key.encode('latin-1')
    iv = key_bytes  
    
    cipher = AES.new(key_bytes, AES.MODE_CBC, iv)
    
    encrypted = cipher.encrypt(password.encode('utf-8'))
    
    # 返回base64编码的加密字符串
    return base64.b64encode(encrypted).decode('utf-8')


#获取请求头aee
def get_dynamic_headers():
    timeStamp = str(int(time.time() * 1000))
    key = appkey[0:8] + timeStamp[0:3] + timeStamp[-5:]
    aee = encryption_password(key,password)
    return {"timeStamp":timeStamp,"abc12":password,"aee":aee}


# 随机生成手机号
def generate_phone_number():
    # 定义手机号码第一部分（即前缀）
    prefixes = ['13', '14', '15', '16', '17', '18', '19']
    # 随机选择一个前缀
    prefix = random.choice(prefixes)
    # 生成剩余的9位数字
    suffix = ''.join(random.choice('0123456789') for _ in range(9))
    # 拼接成完整的手机号码
    return prefix + suffix
    
if __name__ == "__main__":
    print(get_dynamic_headers())