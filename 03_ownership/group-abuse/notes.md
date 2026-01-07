Lab: Group Permission Abuse

Objective:
Understand how misconfigured group permissions can allow unauthorized access
and lead to privilege escalation.

Steps Performed:
1. Created a root-owned directory and file.
2. Created a shared group and added a non-root user to it.
3. Changed group ownership of the directory and file.
4. Enabled group read/write permissions.
5. Accessed and modified root-owned files as a non-root user.
6. Simulated code injection into a root-executed script.
7. Fixed the issue by tightening permissions and removing group access.

Observations:
- Group write permissions allow non-root users to modify root-owned files.
- Group membership can bypass ownership restrictions.
- Misconfigured groups are a serious security risk.

Security Takeaway:
Group permissions must be carefully managed. Writable group access to sensitive
directories or scripts can lead to full system compromise.

Conclusion:
This lab demonstrates how group abuse can be used for privilege escalation and
why least-privilege group assignment is critical in Linux security.
