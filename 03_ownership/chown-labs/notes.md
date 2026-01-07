Lab: Ownership and Group Permissions

Objective:
Understand file and directory ownership and group permissions in Linux.

Steps Performed:
1. Created a file "file1.txt" and a directory "dir1".
2. Changed owner of file1.txt to another user (otheruser).
3. Changed group of dir1 to another group (otheruser).
4. Switched to otheruser and tested read/write access based on group permissions.
5. Restored original ownership and permissions.

Observations:
- Only the owner can write to a file if permissions allow.
- Group ownership controls access for users in the group.
- Misconfigured group permissions can allow or block access.
- Switching ownership requires root privileges.

Security Takeaway:
- Ownership is a critical part of Linux access control.
- Misconfigured ownership or group settings can be exploited.
- Defenders must ensure least-privilege and correct group assignment.

Conclusion:
Mastering chown and chgrp is essential for Linux administration and secure file access.
