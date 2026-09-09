# content.py  -  Static content data (replaces database queries)
# All article and video data is stored here as plain Python dictionaries.
# Views import ARTICLES and VIDEOS directly from this file.

# ============================================================
# OWASP Top 10 Articles  (was: articles.owasptop10 in DB)
# ============================================================
ARTICLES = [
    {
        "page_no": 1,
        "title": "A01 2025 Broken Access Control",
        "description": (
            "Broken access control is a vulnerability where an application fails to properly "
            "enforce restrictions on what authenticated or unauthenticated users are allowed to do. "
            "This allows attackers to access, modify, or act on resources outside their intended "
            "permissions, often leading to data exposure or privilege escalation."
        ),
        "prevention": [
            "Enforce least privilege principles",
            "Deny access by default",
            "Implement proper authorization checks on server-side",
            "Use access control mechanisms like RBAC/ABAC",
            "Log and monitor access control failures",
        ],
        "attack_scenarios": [
            "User modifies URL to access another user's data",
            "Privilege escalation to admin functions",
            "Accessing APIs without proper authorization",
            "Bypassing access control via misconfigured CORS",
        ],
    },
    {
        "page_no": 2,
        "title": "A02 2025 Security Misconfiguration",
        "description": (
            "Security misconfiguration is a vulnerability caused by improper or incomplete "
            "configuration of systems, frameworks, or services. This can leave applications exposed "
            "through default settings, unnecessary features, or inconsistent security controls, "
            "making it easier for attackers to exploit weaknesses."
        ),
        "prevention": [
            "Harden configurations for all environments",
            "Remove unused features and services",
            "Implement secure headers",
            "Automate configuration management",
            "Regularly patch and update systems",
        ],
        "attack_scenarios": [
            "Default credentials used to gain access",
            "Verbose error messages exposing system info",
            "Unpatched systems exploited",
            "Open cloud storage exposing sensitive data",
        ],
    },
    {
        "page_no": 3,
        "title": "A03 2025 Software Supply Chain Failures",
        "description": (
            "Software supply chain failures occur when vulnerabilities are introduced through "
            "third-party components, dependencies, or build processes. Attackers exploit these "
            "external elements to inject malicious code or take advantage of known weaknesses in "
            "software dependencies."
        ),
        "prevention": [
            "Verify integrity of dependencies",
            "Use trusted repositories",
            "Implement Software Bill of Materials (SBOM)",
            "Secure CI/CD pipelines",
            "Continuously monitor dependencies",
        ],
        "attack_scenarios": [
            "Compromised third-party library injects malware",
            "Malicious update from vendor infects system",
            "Use of vulnerable open-source package",
            "Build pipeline tampering",
        ],
    },
    {
        "page_no": 4,
        "title": "A04 2025 Cryptographic Failures",
        "description": (
            "Cryptographic failures occur when encryption and data protection mechanisms are "
            "improperly implemented or outdated. This exposes sensitive data during storage or "
            "transmission, allowing attackers to intercept, read, or manipulate confidential "
            "information."
        ),
        "prevention": [
            "Use strong encryption algorithms",
            "Enforce HTTPS everywhere",
            "Secure key management",
            "Avoid storing sensitive data unnecessarily",
            "Use modern cryptographic libraries",
        ],
        "attack_scenarios": [
            "Sensitive data transmitted without encryption",
            "Weak hashing allows password cracking",
            "Improper key storage leads to data exposure",
            "Man-in-the-middle attacks",
        ],
    },
    {
        "page_no": 5,
        "title": "A05 2025 Injection",
        "description": (
            "Injection is a vulnerability where untrusted input is sent to an interpreter and "
            "executed as code or commands. This allows attackers to manipulate queries, execute "
            "malicious commands, or access unauthorized data within the system."
        ),
        "prevention": [
            "Use parameterized queries",
            "Validate and sanitize inputs",
            "Use ORM frameworks",
            "Escape special characters",
            "Implement input validation",
        ],
        "attack_scenarios": [
            "SQL injection bypasses login",
            "Command injection executes system commands",
            "XSS injects malicious scripts",
            "LDAP injection alters queries",
        ],
    },
    {
        "page_no": 6,
        "title": "A06 2025 Insecure Design",
        "description": (
            "Insecure design refers to flaws that originate from poor system architecture or lack "
            "of proper security considerations during the design phase. These weaknesses are not "
            "due to bugs but arise from missing or ineffective security controls."
        ),
        "prevention": [
            "Perform threat modeling",
            "Use secure design patterns",
            "Implement defense in depth",
            "Define security requirements early",
            "Conduct architecture reviews",
        ],
        "attack_scenarios": [
            "Business logic abuse (e.g., bypass payment)",
            "Missing rate limiting enables abuse",
            "No fraud detection mechanisms",
            "Insecure workflow design",
        ],
    },
    {
        "page_no": 7,
        "title": "A07 2025 Authentication Failures",
        "description": (
            "Authentication failures occur when systems improperly verify the identity of users or "
            "fail to secure authentication processes. This allows attackers to compromise accounts, "
            "impersonate users, or gain unauthorized access."
        ),
        "prevention": [
            "Use multi-factor authentication",
            "Implement secure password policies",
            "Protect against brute force attacks",
            "Use secure session management",
            "Avoid default credentials",
        ],
        "attack_scenarios": [
            "Credential stuffing attacks",
            "Session hijacking",
            "Brute force login attempts",
            "Weak password policies exploited",
        ],
    },
    {
        "page_no": 8,
        "title": "A08 2025 Software and Data Integrity Failures",
        "description": (
            "Software and data integrity failures happen when systems do not properly ensure that "
            "code and data have not been tampered with. This can allow attackers to introduce "
            "malicious updates, alter data, or execute unauthorized code."
        ),
        "prevention": [
            "Use digital signatures",
            "Verify updates and packages",
            "Secure CI/CD pipelines",
            "Implement integrity checks",
            "Restrict unsafe deserialization",
        ],
        "attack_scenarios": [
            "Malicious update installed",
            "Tampered data processed by application",
            "Insecure deserialization leads to RCE",
            "Pipeline injection attacks",
        ],
    },
    {
        "page_no": 9,
        "title": "A09 2025 Logging and Alerting Failures",
        "description": (
            "Logging and alerting failures occur when systems lack proper monitoring, logging, or "
            "alert mechanisms to detect and respond to security incidents. This allows attacks to "
            "go unnoticed and delays incident response."
        ),
        "prevention": [
            "Enable comprehensive logging",
            "Monitor logs continuously",
            "Set up alerts for suspicious activity",
            "Integrate SIEM systems",
            "Ensure logs are protected from tampering",
        ],
        "attack_scenarios": [
            "Attack goes undetected due to no logs",
            "Delayed response to breach",
            "No alert on repeated login failures",
            "Logs deleted to hide attack traces",
        ],
    },
    {
        "page_no": 10,
        "title": "A10 2025 Mishandling of Exceptional Conditions",
        "description": (
            "Mishandling of exceptional conditions occurs when applications fail to properly handle "
            "errors, unexpected inputs, or edge cases. This can lead to crashes, denial of service, "
            "or unintended system behavior that attackers can exploit."
        ),
        "prevention": [
            "Implement proper error handling",
            "Gracefully handle resource exhaustion",
            "Validate inputs under all conditions",
            "Use fail-safe defaults",
            "Test edge cases thoroughly",
        ],
        "attack_scenarios": [
            "Resource exhaustion causing DoS",
            "Unhandled exceptions crash system",
            "Infinite loops triggered by input",
            "Improper fallback exposes vulnerabilities",
        ],
    },
]

# ============================================================
# Videos  (was: videos.video in DB)
# ============================================================
VIDEOS = [
    {"page_no": 1,  "title": "A01 2025 Broken Access Control",                 "src": "https://www.youtube.com/embed/vUFVxoV5y_I?si=RkxrrmpAxub2r3iq"},
    {"page_no": 2,  "title": "A02 2025 Security Misconfigurations",            "src": "https://www.youtube.com/embed/67cuz8aOvjk?si=vvBktgTGx5dISXvM"},
    {"page_no": 3,  "title": "A03 2025 Software Supply Chain Failures",       "src": "https://www.youtube.com/embed/LIkxOiNOkec?si=R7vgNJf7kiU0ZrrT"},
    {"page_no": 4,  "title": "A04 2025 Cryptographic Failures",               "src": "https://www.youtube.com/embed/2CMNNAJ6Ixc?si=bODCX-CJ4CN3DhER"},
    {"page_no": 5,  "title": "A05 2025 Injection",                            "src": "https://www.youtube.com/embed/wu6FAsiFhv0?si=tPqcj8oCROQwuqix"},
    {"page_no": 6,  "title": "A06 2025 Insecure Design",                      "src": "https://www.youtube.com/embed/wu6FAsiFhv0?si=tPqcj8oCROQwuqix"},
    {"page_no": 7,  "title": "A07 2025 Authentication Failures",              "src": "https://www.youtube.com/embed/IDKhNPlHMOY?si=clCP8D5zwL5zaYra"},
    {"page_no": 8,  "title": "A08 2025 Software and Data Integrity Failures", "src": "https://www.youtube.com/embed/TwfLvG0D6dc?si=Ps0g4QMxS1UdI3ak"},
    {"page_no": 9,  "title": "A09 2025 Logging and Alerting Failures",        "src": "https://www.youtube.com/embed/IDKhNPlHMOY?si=qhNmOGtDvl_aO69e"},
    {"page_no": 10, "title": "A10 2025 Mishandling of Exceptional Conditions","src": "https://www.youtube.com/embed/SzyQYOCbNDY?si=vFnWNtIGqfqyvAtk"},
]
