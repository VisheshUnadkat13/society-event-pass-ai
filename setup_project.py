from pathlib import Path
import pandas as pd

# ==========================
# Create Folders
# ==========================

folders = [
    "data",
    "generated",
    "generated/qr_codes",
    "generated/passes",
    "uploads",
    "uploads/payment_screenshots",
    "logs",
    "assets",
    "agents",
    "pages",
    "services",
    "utils",
]

for folder in folders:
    Path(folder).mkdir(parents=True, exist_ok=True)

print("✅ Folder structure created.")

# ==========================
# members.xlsx
# ==========================

members_columns = [
    "Member ID",
    "Wing",
    "Flat No",
    "Name",
    "Phone Number",
    "Is Primary Contact"
]

members_data = [
    ["M001", "A", "A-101", "Rajesh Patel", "9876543210", "Yes"],
    ["M002", "A", "A-101", "Meena Patel", "9876543211", "No"],
    ["M003", "A", "A-101", "Aarav Patel", "9876543212", "No"],
    ["M004", "A", "A-102", "Amit Shah", "9876543220", "Yes"],
    ["M005", "A", "A-102", "Neha Shah", "9876543221", "No"],
    ["M006", "B", "B-201", "Rahul Joshi", "9876543230", "Yes"],
    ["M007", "B", "B-201", "Pooja Joshi", "9876543231", "No"],
    ["M008", "B", "B-202", "Vikram Desai", "9876543240", "Yes"],
    ["M009", "B", "B-202", "Riya Desai", "9876543241", "No"],
    ["M010", "C", "C-301", "Karan Mehta", "9876543250", "Yes"],
    ["M011", "C", "C-301", "Priya Mehta", "9876543251", "No"],
]

members_df = pd.DataFrame(members_data, columns=members_columns)
members_df.to_excel("data/members.xlsx", index=False)

print("✅ members.xlsx created.")

# ==========================
# events.xlsx
# ==========================

events_columns = [
    "Event ID",
    "Event Name",
    "Event Date",
    "Price Per Person",
    "Booking Open",
    "Booking Close",
    "Status"
]

events_data = [
    [
        "EVT001",
        "Navratri Dinner",
        "2026-10-15",
        150,
        "2026-10-10",
        "2026-10-14",
        "Open"
    ]
]

events_df = pd.DataFrame(events_data, columns=events_columns)
events_df.to_excel("data/events.xlsx", index=False)

print("✅ events.xlsx created.")

# ==========================
# bookings.xlsx
# ==========================

bookings_columns = [
    "Booking ID",
    "Event ID",
    "Flat No",
    "Member IDs",
    "Total Members",
    "Total Amount",
    "Payment Status",
    "Pass ID",
    "Booking Date"
]

bookings_df = pd.DataFrame(columns=bookings_columns)
bookings_df.to_excel("data/bookings.xlsx", index=False)

print("✅ bookings.xlsx created.")

# ==========================
# payments.xlsx
# ==========================

payments_columns = [
    "Payment ID",
    "Booking ID",
    "Transaction ID",
    "Amount",
    "Receiver UPI",
    "Verification Status",
    "Screenshot File"
]

payments_df = pd.DataFrame(columns=payments_columns)
payments_df.to_excel("data/payments.xlsx", index=False)

print("✅ payments.xlsx created.")

print("\n🎉 Project setup completed successfully!")