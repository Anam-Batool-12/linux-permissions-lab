Python cannot elevate via SUID

Only compiled binaries can

Attackers look for:

find / -perm -4000 -type f 2>/dev/null
