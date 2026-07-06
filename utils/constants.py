"""
============================================================
Society Event Pass AI
Application Constants
============================================================

This file contains all application-wide constants.

Whenever possible, DO NOT hardcode values in your project.
Import them from this file instead.

Example:
    from utils.constants import PAYMENT_VERIFIED
"""

# ============================================================
# APPLICATION
# ============================================================

APP_NAME = "Society Event Pass AI"

APP_VERSION = "1.0.0"

PAGE_TITLE = "Society Event Pass AI"

PAGE_ICON = "🎟️"

LAYOUT = "wide"

# ============================================================
# SOCIETY DETAILS
# ============================================================

SOCIETY_NAME = "Shyamal Satva"

SOCIETY_UPI_ID = "abcsociety@upi"

SOCIETY_EMAIL = "shyamalsatva@gmail.com"

SOCIETY_PHONE = "+91 9106891862"

# ============================================================
# PROJECT DIRECTORIES
# ============================================================

DATA_FOLDER = "data"

UPLOAD_FOLDER = "uploads"

PAYMENT_SCREENSHOT_FOLDER = "uploads/payment_screenshots"

GENERATED_FOLDER = "generated"

QR_FOLDER = "generated/qr_codes"

PASS_FOLDER = "generated/passes"

ASSET_FOLDER = "assets"

LOG_FOLDER = "logs"

# ============================================================
# EXCEL FILES
# ============================================================

MEMBERS_FILE = "data/members.xlsx"

EVENTS_FILE = "data/events.xlsx"

BOOKINGS_FILE = "data/bookings.xlsx"

PAYMENTS_FILE = "data/payments.xlsx"

# ============================================================
# MEMBER COLUMNS
# ============================================================

MEMBER_ID = "Member ID"

WING = "Wing"

FLAT_NO = "Flat No"

NAME = "Name"

PHONE = "Phone Number"

PRIMARY_CONTACT = "Is Primary Contact"

# ============================================================
# EVENT COLUMNS
# ============================================================

EVENT_ID = "Event ID"

EVENT_NAME = "Event Name"

EVENT_DATE = "Event Date"

PRICE_PER_PERSON = "Price Per Person"

BOOKING_OPEN = "Booking Open"

BOOKING_CLOSE = "Booking Close"

EVENT_STATUS = "Status"

# ============================================================
# BOOKING COLUMNS
# ============================================================

BOOKING_ID = "Booking ID"

MEMBER_IDS = "Member IDs"

TOTAL_MEMBERS = "Total Members"

TOTAL_AMOUNT = "Total Amount"

PAYMENT_STATUS = "Payment Status"

PASS_ID = "Pass ID"

BOOKING_DATE = "Booking Date"

# ============================================================
# PAYMENT COLUMNS
# ============================================================

PAYMENT_ID = "Payment ID"

TRANSACTION_ID = "Transaction ID"

AMOUNT = "Amount"

RECEIVER_UPI = "Receiver UPI"

VERIFICATION_STATUS = "Verification Status"

SCREENSHOT_FILE = "Screenshot File"

# ============================================================
# PAYMENT STATUS
# ============================================================

PAYMENT_PENDING = "Pending"

PAYMENT_VERIFIED = "Verified"

PAYMENT_REJECTED = "Rejected"

# ============================================================
# BOOKING STATUS
# ============================================================

BOOKING_PENDING = "Pending"

BOOKING_CONFIRMED = "Confirmed"

BOOKING_CANCELLED = "Cancelled"

# ============================================================
# EVENT STATUS
# ============================================================

EVENT_OPEN_STATUS = "Open"

EVENT_CLOSED_STATUS = "Closed"

EVENT_COMPLETED_STATUS = "Completed"

# ============================================================
# QR CODE SETTINGS
# ============================================================

QR_VERSION = 1

QR_BOX_SIZE = 10

QR_BORDER = 4

# ============================================================
# OCR SETTINGS
# ============================================================

TESSERACT_LANGUAGE = "eng"

# ============================================================
# FILE TYPES
# ============================================================

SUPPORTED_IMAGE_TYPES = [
    "png",
    "jpg",
    "jpeg"
]

SUPPORTED_EXCEL_TYPES = [
    "xlsx"
]

# ============================================================
# PASS SETTINGS
# ============================================================

PASS_PREFIX = "PASS"

BOOKING_PREFIX = "BK"

PAYMENT_PREFIX = "PAY"

EVENT_PREFIX = "EVT"

MEMBER_PREFIX = "M"

# ============================================================
# CURRENCY
# ============================================================

CURRENCY_SYMBOL = "₹"

# ============================================================
# DATE FORMAT
# ============================================================

DATE_FORMAT = "%d-%m-%Y"

DATETIME_FORMAT = "%d-%m-%Y %H:%M:%S"

# ============================================================
# STREAMLIT MESSAGES
# ============================================================

SUCCESS_BOOKING = "✅ Booking completed successfully."

SUCCESS_PAYMENT = "✅ Payment verified successfully."

SUCCESS_PASS = "✅ Pass generated successfully."

ERROR_DUPLICATE_BOOKING = "❌ This flat has already booked for this event."

ERROR_PAYMENT = "❌ Payment verification failed."

ERROR_EVENT = "❌ No active event found."

ERROR_MEMBER = "❌ No members found."

# ============================================================
# AGENT NAMES
# ============================================================

BOOKING_AGENT = "Booking Agent"

OCR_AGENT = "OCR Agent"

PAYMENT_AGENT = "Payment Verification Agent"

PASS_AGENT = "Pass Generation Agent"

NOTIFICATION_AGENT = "Notification Agent"

# ============================================================
# DEFAULT VALUES
# ============================================================

DEFAULT_PRICE = 100

DEFAULT_STATUS = PAYMENT_PENDING

DEFAULT_BOOKING_STATUS = BOOKING_PENDING