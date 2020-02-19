import zipfile

obj = zipfile.ZipFile("file_to_crack.zip") # הקובץ זיפ שאנו רוצים לפרוץ

f = open("password.txt", 'r') #קובץ הסיסמאות הנפוצות 

for password in f.readlines(): #עובר על כל הסיסמאות בקובץ זה ומנסה להפעיל אותם על הקובץ זיפ
    password = password.strip("\n").strip("\r")

    try:
        obj.extractall(pwd=password)
        print("[+]Password found : " + password + " ************************")

    except:
        print("[-]Trying........")          


