# This files defines the vulnerability rules that will be searched on the files

class VulnerabilityRule:
    def __init__(self, name, severity, description, pattern):
        self.name = name
        self.severity = severity  # HIGH, MEDIUM, LOW
        self.description = description
        self.pattern = pattern  # What to look for

    def __str__(self):
        return f"{self.name} ({self.severity}): {self.description} - Pattern: {self.pattern}"

class VulnerabilityRules:
    def __init__(self):
        self.rules = []

    def add_rule(self, rule):
        self.rules.append(rule)

    def __str__(self):
        return "\n".join(str(rule) for rule in self.rules)

    def get_rules(self):
        return self.rules
