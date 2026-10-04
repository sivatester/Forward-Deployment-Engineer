import csv

CSV_FILE = "homework_invoices.csv"
HIGH_VALUE_LIMIT = 100000

total_invoices = 0
high_value_count = 0
invalid_amount_count = 0

# Step 1: Read CSV
with open(CSV_FILE, newline="") as file:
    reader = csv.DictReader(file)

    # Step 2: Read each invoice
    for row in reader:
        total_invoices += 1

        invoice_id = row["invoice_id"]
        vendor = row["vendor"].strip() or "MISSING VENDOR"
        amount_text = row["amount"].strip()
        status = row["status"].strip()

        # Step 3 + 4: Check the amount, and handle invalid data with try/except
        try:
            amount = float(amount_text)  # "" or "TBD" raises ValueError
        except ValueError:
            invalid_amount_count += 1
            print(f"{invoice_id} | {vendor} | amount='{amount_text}' | {status} -> INVALID/MISSING AMOUNT")
            continue  # skip to the next invoice instead of stopping

        if amount > HIGH_VALUE_LIMIT:
            high_value_count += 1
            print(f"{invoice_id} | {vendor} | {amount:,.2f} | {status} -> HIGH VALUE (> 100,000)")
        else:
            print(f"{invoice_id} | {vendor} | {amount:,.2f} | {status} -> OK")

# Step 5: Print summary
print("\n----- SUMMARY -----")
print(f"Total invoices read            : {total_invoices}")
print(f"Invoices greater than 100,000  : {high_value_count}")
print(f"Invoices with missing/invalid amount : {invalid_amount_count}")