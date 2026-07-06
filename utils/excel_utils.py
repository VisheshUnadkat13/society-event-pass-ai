from pathlib import Path
import pandas as pd


class ExcelManager:
    """
    Handles all Excel read/write operations.

    Every service should use this class instead of
    directly accessing Excel files.
    """

    DATA_DIR = Path("data")

    MEMBERS_FILE = DATA_DIR / "members.xlsx"
    EVENTS_FILE = DATA_DIR / "events.xlsx"
    BOOKINGS_FILE = DATA_DIR / "bookings.xlsx"
    PAYMENTS_FILE = DATA_DIR / "payments.xlsx"

    # ==========================================================
    # Generic Helpers
    # ==========================================================

    @staticmethod
    def _read_excel(file_path):
        return pd.read_excel(file_path)

    @staticmethod
    def _write_excel(df, file_path):
        df.to_excel(file_path, index=False)

    @staticmethod
    def _append_row(df, row):
        return pd.concat(
            [df, pd.DataFrame([row])],
            ignore_index=True
        )

    # ==========================================================
    # MEMBERS
    # ==========================================================

    @classmethod
    def load_members(cls):
        return cls._read_excel(cls.MEMBERS_FILE)

    @classmethod
    def get_all_wings(cls):
        df = cls.load_members()

        return sorted(
            df["Wing"].dropna().unique().tolist()
        )

    @classmethod
    def get_flats_by_wing(cls, wing):

        df = cls.load_members()

        return sorted(
            df[df["Wing"] == wing]["Flat No"]
            .dropna()
            .unique()
            .tolist()
        )

    @classmethod
    def get_members_by_flat(cls, flat_no):

        df = cls.load_members()

        return df[df["Flat No"] == flat_no]

    @classmethod
    def get_primary_contact(cls, flat_no):

        df = cls.load_members()

        result = df[
            (df["Flat No"] == flat_no)
            &
            (df["Is Primary Contact"] == "Yes")
        ]

        if result.empty:
            return None

        return result.iloc[0]

    # ==========================================================
    # EVENTS
    # ==========================================================

    @classmethod
    def load_events(cls):
        return cls._read_excel(cls.EVENTS_FILE)

    @classmethod
    def get_open_events(cls):

        df = cls.load_events()

        return df[df["Status"] == "Open"]

    @classmethod
    def get_event_by_id(cls, event_id):

        df = cls.load_events()

        result = df[
            df["Event ID"] == event_id
        ]

        if result.empty:
            return None

        return result.iloc[0]

    @classmethod
    def event_exists(cls, event_id):

        df = cls.load_events()

        return not df[
            df["Event ID"] == event_id
        ].empty

    @classmethod
    def save_event(cls, event):

        df = cls.load_events()

        df = cls._append_row(df, event)

        cls._write_excel(
            df,
            cls.EVENTS_FILE
        )

    @classmethod
    def update_event_status(
        cls,
        event_id,
        status
    ):

        df = cls.load_events()

        df.loc[
            df["Event ID"] == event_id,
            "Status"
        ] = status

        cls._write_excel(
            df,
            cls.EVENTS_FILE
        )

    # ==========================================================
    # BOOKINGS
    # ==========================================================

    @classmethod
    def load_bookings(cls):
        return cls._read_excel(cls.BOOKINGS_FILE)

    @classmethod
    def booking_exists(
        cls,
        event_id,
        flat_no
    ):

        df = cls.load_bookings()

        return not df[
            (df["Event ID"] == event_id)
            &
            (df["Flat No"] == flat_no)
        ].empty

    @classmethod
    def save_booking(
        cls,
        booking
    ):

        df = cls.load_bookings()

        df = cls._append_row(
            df,
            booking
        )

        cls._write_excel(
            df,
            cls.BOOKINGS_FILE
        )

    @classmethod
    def update_payment_status(
        cls,
        booking_id,
        status
    ):

        df = cls.load_bookings()

        df.loc[
            df["Booking ID"] == booking_id,
            "Payment Status"
        ] = status

        cls._write_excel(
            df,
            cls.BOOKINGS_FILE
        )

    @classmethod
    def update_booking_status(
        cls,
        booking_id,
        status
    ):

        df = cls.load_bookings()

        df.loc[
            df["Booking ID"] == booking_id,
            "Booking Status"
        ] = status

        cls._write_excel(
            df,
            cls.BOOKINGS_FILE
        )

    # ==========================================================
    # PAYMENTS
    # ==========================================================

    @classmethod
    def load_payments(cls):
        return cls._read_excel(
            cls.PAYMENTS_FILE
        )

    @classmethod
    def save_payment(
        cls,
        payment
    ):

        df = cls.load_payments()

        df = cls._append_row(
            df,
            payment
        )

        cls._write_excel(
            df,
            cls.PAYMENTS_FILE
        )

    # ==========================================================
    # DASHBOARD
    # ==========================================================

    @classmethod
    def total_members(cls):
        return len(
            cls.load_members()
        )

    @classmethod
    def total_flats(cls):
        return cls.load_members()[
            "Flat No"
        ].nunique()

    @classmethod
    def total_events(cls):
        return len(
            cls.load_events()
        )

    @classmethod
    def total_bookings(cls):
        return len(
            cls.load_bookings()
        )

    @classmethod
    def total_revenue(cls):

        df = cls.load_bookings()

        if df.empty:
            return 0

        return df["Total Amount"].sum()