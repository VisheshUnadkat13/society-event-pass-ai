import pandas as pd
from pathlib import Path

class ExcelManager:
    """
    Handles all Excel operations for the society Event Pass System.
    """

    DATA_DIR=Path("data")

    MEMBERS_FILE = DATA_DIR / "members.xlsx"
    EVENTS_FILE = DATA_DIR / "events.xlsx"
    BOOKINGS_FILE = DATA_DIR / "bookings.xlsx"
    PAYMENTS_FILE = DATA_DIR / "payments.xlsx"


    ## MEMBERS

    @classmethod
    def load_membbers(cls):
        return pd.read_excel(cls.MEMBERS_FILE)

    @classmethod
    def get_all_wings(cls):
        df=cls.load_membbers()
        return sorted(df["Wing"].dropna().unique().tolist())

    @classmethod
    def get_flat_by_wings(cls,wing):
        df=cls.load_membbers()

        flats=(
            df[df["Wing"]==wing]["flat No"]
            .dropna()
            .unique()
            .tolist()
        )    
        return sorted(flats)

    @classmethod
    def get_members_by_flats(cls,flat_no):
        df=pd.load_members()

        return df[df["Flat No"] == flat_no]    

    @classmethod
    def get_primary_contact(cls, flat_no):
        df = cls.load_members()

        result = df[
            (df["Flat No"] == flat_no)
            & (df["Is Primary Contact"] == "Yes")
        ]

        if result.empty:
            return None

        return result.iloc[0]

    ## EVENTS
    @classmethod
    def load_event(cls):
        return pd.read_excel(cls.EVENTS_FILE)

    @classmethod
    def get_open_events(cls):
        df = cls.load_events()

        return df[df["Status"] == "Open"]

    @classmethod
    def get_event_by_id(cls, event_id):
        df = cls.load_events()

        result = df[df["Event ID"] == event_id]

        if result.empty:
            return None

        return result.iloc[0]

    ## BOOKINGS 

    @classmethod
    def load_boking(cls):
        return pd.read_excel(cls.BOOKINGS_FILE)

    @classmethod
    def booking_exists(cls,event_id,flat_no):
        df=cls.load_booking()

        result = df[
            (df["Event ID"] == event_id)
            & (df["Flat No"] == flat_no)
        ]

        return not result.empty

    @classmethod
    def save_booking(cls,booking_data):
        df=cls.load_booking()

        df = pd.concat(
            [df, pd.DataFrame([booking_data])],
            ignore_index=True
        )

        df.to_excel(cls.BOOKINGS_FILE, index=False)

    ## PAYMENTS

    @classmethod
    def load_payments(cls):
        return pd.read_excel(cls.PAYMENTS_FILE)

    @classmethod
    def save_payment(cls, payment_data):
        df = cls.load_payments()

        df = pd.concat(
            [df, pd.DataFrame([payment_data])],
            ignore_index=True
        )

        df.to_excel(cls.PAYMENTS_FILE, index=False)

    ## DASHBOARD

    @classmethod
    def total_members(cls):
        return len(cls.load_members())

    @classmethod
    def total_flats(cls):
        df = cls.load_members()

        return df["Flat No"].nunique()

    @classmethod
    def total_bookings(cls):
        return len(cls.load_bookings())

    @classmethod
    def total_revenue(cls):
        df = cls.load_bookings()

        if df.empty:
            return 0

        return df["Total Amount"].sum()                     


