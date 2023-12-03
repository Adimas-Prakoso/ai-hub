import random
import string

def nama():
    nama_file = ''.join(random.choices(string.ascii_letters + string.digits, k=20))
    return nama_file