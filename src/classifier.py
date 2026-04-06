import json

def load_rules():
    with open("data/rules.json") as f:
        return json.load(f)

def classify(use_case):

    rules = load_rules()

    for rule in rules["prohibited"]:
        if all(use_case.get(k) == v for k, v in rule["conditions"].items()):
            return {
                "risk_level": "PROHIBITED",
                "legal_basis": rule["legal_basis"]
            }

    for rule in rules["high_risk"]:
        if all(use_case.get(k) == v for k, v in rule["conditions"].items()):
            return {
                "risk_level": "HIGH-RISK",
                "legal_basis": rule["legal_basis"]
            }

    return {
        "risk_level": "LOW RISK",
        "legal_basis": "No classification"
    }