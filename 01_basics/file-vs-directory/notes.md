Lab: File vs Directory Permissions

Objective:
Understand how permissions behave differently on files versus directories in Linux.

Steps Performed:
1. Created a directory "mydir" and a file "myfile.txt".
2. Set directory to read-only (chmod 400) and tested access.
3. Set file to read-only (chmod 400) and tested reading/writing.
4. Observed differences in behavior between files and directories.

Observations:
- Directory read-only allows listing filenames but prevents entering or creating files.
- File read-only allows reading but prevents writing.
- Execute permission has different meanings:
    - Directory: required to enter (cd)
    - File: required to execute/run

Security Takeaway:
Permissions affect files and directories differently. Understanding these differences is
essential for access control and defending Linux systems.

Conclusion:
Files and directories behave differently under permissions. Directory execute is crucial
for traversal, file execute is crucial for running scripts or binaries.
