Lab: chmod Numeric vs Symbolic Permissions

Objective:
Learn how to set permissions using numeric (octal) and symbolic notation on files and directories.

Steps Performed:
1. Created a file "file1.txt" and a directory "dir1".
2. Applied numeric permissions:
    - file1.txt → 600 (rw-------)
    - dir1 → 700 (rwx------)
3. Tested access for owner and observed restricted access for others.
4. Applied symbolic permissions:
    - Added execute to file1.txt for owner (u+x)
    - Removed read from others on dir1 (o-r)
    - Added write to group on dir1 (g+w)
5. Tested behaviors and access permissions after each change.

Observations:
- Numeric permissions are faster for setting all permissions at once.
- Symbolic permissions are better for incremental changes.
- Directory execute is required for entering and creating files.
- File execute is required to run scripts or binaries.
- Owner, group, and others permissions affect access differently.

Security Takeaway:
Understanding both numeric and symbolic chmod allows precise control over access.
Misconfigured permissions can lead to unauthorized access or privilege escalation.

Conclusion:
Mastering chmod numeric and symbolic modes is critical for Linux administration and security.
