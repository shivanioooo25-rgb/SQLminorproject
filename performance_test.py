from detector import detect_sql_injection
from risk_classifier import classify_risk

test_cases = [
    "admin",
    "hello123",
    "admin' OR 1=1 --",
    "' UNION SELECT username,password FROM users --",
    "DROP TABLE users;",
    "SELECT * FROM users"
]

print("=" * 70)
print("      SQL Injection Detection System - Performance Testing")
print("=" * 70)

for test in test_cases:

    print(f"\nInput : {test}")

    if detect_sql_injection(test):

        risk = classify_risk(test)

        print("Status : SQL Injection Detected")
        print(f"Risk   : {risk}")

    else:

        print("Status : Safe Input")

print("\n" + "=" * 70)
print("Performance Testing Completed Successfully")
print("=" * 70)