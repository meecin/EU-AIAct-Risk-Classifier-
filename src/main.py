from classifier import classify

use_case = {
    "domain": "employment",
    "decision_support": True
}

result = classify(use_case)

print("Risk Level:", result["risk_level"])
print("Legal Basis:", result["legal_basis"])