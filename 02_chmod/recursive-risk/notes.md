Lab: Recursive chmod Risks

Objective:
Understand the risks and behavior of recursive chmod (-R) on files and directories.

Steps Performed:
1. Created a nested directory structure with files.
2. Applied chmod -R 400 to everything.
3. Tested access:
    - cd into directories → failed
    - touch new files → failed
    - ls top-level → partially worked
4. Applied safer approach:
    - Directories → 700
    - Files → 600
5. Tested access again, all worked for owner.

Observations:
- Recursive chmod applies the same permissions to all files and directories.
- Directories need execute permission to enter/traverse.
- Files need read/write for owner to access/modify.
- Incorrect recursive chmod can lock out access entirely.

Security Takeaway:
- Recursive chmod is dangerous if not carefully planned.
- Always separate directory vs file permissions when changing recursively.
- Attackers or misconfigurations can exploit or break systems using -R.

Conclusion:
Understanding recursive chmod and its risks is essential for Linux administration
and secure system management.
