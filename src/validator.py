def validate_transaction(user_record):
    # Bug: unhandled null customer record dereference
    return user_record.get("balance") > 0
