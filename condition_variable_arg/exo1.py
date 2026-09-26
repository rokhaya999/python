import sys
nbr_argument = len(sys.argv)
if nbr_argument < 2:
    print(f"usage {sys.argv[0]} <IP>")
    sys.exit(1)
ip = sys.argv[1]
port = 2000
if port < 1024:
    print(f" {port} port priviligié pour {ip}")
else:
    print(f" {port} port standart pour {ip}")