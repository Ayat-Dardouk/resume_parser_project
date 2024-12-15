def isskill(line):
    skills = [
        # Technical Skills
        "python", "customer support", "sales", "c++", "programming", "android", 
        "css", "adobe", "google", "processing", "sql", "django", "cloud", 
        "drawing", "painting", "html", "algorithms", "excel", "analytics", 
        "data structures", "dbms", "php", "R", "science", "machine", "tally", 
        "accountancy", "chemistry", "physics", "javascript", "java", "react", 
        "angular", "vue", "node.js", "flask", "data analysis", "power bi", 
        "tableau", "ai", "deep learning", "nlp", "machine learning", 
        "big data", "hadoop", "spark", "git", "github", "docker", "kubernetes", 
        "linux", "bash scripting", "sap", "statistical analysis", "sas", 
        "matlab", "simulink", "latex", "blockchain", "cryptography", "vr", 
        "ar", "iot", "robotics", "networking", "cybersecurity", "ethical hacking", 
        "penetration testing", "qa", "testing", "agile", "scrum", "jira", 
        "trello", "powerpoint", "microsoft office", "crm", "3d modeling", 
        "autocad", "solidworks", "video editing", "motion graphics", 
        "animation", "graphic design", "ui/ux design", "photoshop", 
        "illustrator", "content creation", "social media management", "ecommerce", 
        "supply chain management", "logistics",

        # Communication Skills
        "public speaking", "negotiation", "active listening", 
        "presentation skills", "verbal communication", "non-verbal communication", 
        "storytelling", "email writing", "rapport building", 
        "conflict resolution", "influencing", "interpersonal skills", 
        "persuasion",

        # Personal Skills
        "teamwork", "time management", "problem solving", "critical thinking", 
        "leadership", "creativity", "adaptability", "self-motivation", 
        "organization", "emotional intelligence", "stress management", 
        "decision making", "goal setting", "empathy", "collaboration", 
        "integrity", "attention to detail", "work ethic",

        # Technical Skills (Soft Skill Overlaps)
        "project management", "technical writing", "analytical thinking", 
        "research", "troubleshooting", "innovation"
    ]

    # Normalize input line to lowercase for case-insensitive matching
    line = line.lower()

    # Check if any skill is found in the line
    for s in skills:
        if s in line:
            return True  # Skill found
    return False  # No skill found
