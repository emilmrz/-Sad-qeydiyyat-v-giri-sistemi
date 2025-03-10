# Sadə qeydiyyat və giriş sistemi

# Qeydiyyat üçün istifadəçi məlumatları
username = input("Qeydiyyat üçün istifadəçi adı daxil edin: ")
passcode = input("Qeydiyyat üçün şifrə daxil edin: ")

# İstifadəçidən giriş üçün məlumat istəyirik
username_login = input("Daxil ol: İstifadəçi adınızı daxil edin: ")
passcode_login = input("Daxil ol: Şifrənizi daxil edin: ")

# Girişin düzgün olub-olmadığını yoxlayırıq
if username_login == username and passcode_login == passcode:
    print("Xoş gəldiniz!")
else:
    print("İstifadəçi adı və ya şifrə səhvdir!")
