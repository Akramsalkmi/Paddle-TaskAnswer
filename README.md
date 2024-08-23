# Paddle-TaskAnswer

# Transaction Processor

## Description

This Python script processes a set of transactions and provides answers to the following questions:

1. How many transactions do we have?
2. What is the total amount of money that is past due per year?
3. What is the breakdown of transaction statuses by amount?

The solution is designed to handle basic transaction data and provide summarized information based on the input.

## Running the Application

1. Place your `transactions.json` file in the root directory.

2. Run the application:

   ```bash
   python main.py
   ```

The script will output the following:
- The total number of transactions.
- The total past due amounts, grouped by year.
- The breakdown of transaction statuses by amount, expressed as a percentage of the total transaction amount.

## Example

If your `transactions.json` file contains the following data:

```json
{
  "transactions": [
    {"id": 1, "date": "2022-01-10", "amount": 100.0, "status": "paid"},
    {"id": 2, "date": "2022-02-15", "amount": 200.0, "status": "past_due"},
    {"id": 3, "date": "2023-03-12", "amount": 150.0, "status": "paid"},
    {"id": 4, "date": "2023-04-08", "amount": 250.0, "status": "past_due"}
  ]
}
```

The script will produce the following output:

```
Total Transactions: 4
Total Past Due Amounts per Year: {2022: 200.0, 2023: 250.0}
Transaction Status Breakdown by Amount: {'paid': 50.0, 'past_due': 50.0}
```
