import json
from collections import defaultdict
from datetime import datetime


# Load transactions from the JSON file
def load_transactions(json_file_path):
    with open(json_file_path, 'r') as f:
        data = json.load(f)
    return data['transactions']

# 1. How many transactions do we have?
def count_transactions(transactions):
    return len(transactions)

# 2. What is the total amount of money that is past due per year?
def total_past_due_amount_per_year(transactions):
    past_due_amounts = defaultdict(float)
    for transaction in transactions:
        if transaction['status'] == 'past_due':
            year = datetime.strptime(transaction['date'], '%Y-%m-%d').year
            past_due_amounts[year] += transaction['amount']
    return dict(past_due_amounts)

# 3. What is the breakdown of transaction statuses by amount?
def transaction_status_breakdown(transactions):
    status_amounts = defaultdict(float)
    total_amount = sum(transaction['amount'] for transaction in transactions)

    for transaction in transactions:
        status_amounts[transaction['status']] += transaction['amount']

    breakdown = {status: (amount / total_amount) * 100 for status, amount in status_amounts.items()}
    return breakdown

# Main script
if __name__ == "__main__":
    # Load transactions from the file
    transactions = load_transactions('transactions.json')

    # 1. Count of transactions
    total_transactions = count_transactions(transactions)
    print(f"Total Transactions: {total_transactions}")

    # 2. Total past due amount per year
    past_due_amounts_per_year = total_past_due_amount_per_year(transactions)
    print(f"Total Past Due Amounts per Year: {past_due_amounts_per_year}")

    # 3. Breakdown of transaction statuses by amount
    breakdown = transaction_status_breakdown(transactions)
    print(f"Transaction Status Breakdown by Amount: {breakdown}")
