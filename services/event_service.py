from datetime import datetime
import uuid

from utils.excel_utils import ExcelManager
from utils.constants import (
    EVENT_OPEN_STATUS,
    EVENT_CLOSED_STATUS,
    EVENT_COMPLETED_STATUS,
)

class EventService:
    """
    Handles all business logic related to Events.
    """

    @staticmethod
    def generate_event_id():
        """
        Generate a unique Event ID.
        Example: EVT-A1B2C3D4
        """
        return f"EVT-{uuid.uuid4().hex[:8].upper()}"

    @staticmethod
    def get_all_events():
        """
        Return All Events
        """    
        return ExcelManager.load_events()

    @staticmethod
    def get_open_events():
        """
        Return All Open Events
        """    
        return ExcelManager.get_open_events()

    @staticmethod
    def get_event_by_id(event_id):
        """
        Return All Events By Id
        """    
        return ExcelManager.get_event_by_id(event_id)

    @staticmethod
    def get_current_event():
        """
        Return the first active event.
        """

        events = ExcelManager.get_open_events()

        if events.empty:
            return None

        return events.iloc[0]

    @staticmethod
    def active_event_exists():
        """
        check if there is any active events.
        """        
        return not ExcelManager.get_open_events().empty


    @staticmethod
    def is_booking_open(event):
        """
        Check whether booking is currently open.
        """

        today = datetime.today().date()

        booking_open = datetime.strptime(
            str(event["Booking Open"]),
            "%Y-%m-%d"
        ).date()

        booking_close = datetime.strptime(
            str(event["Booking Close"]),
            "%Y-%m-%d"
        ).date()

        return booking_open <= today <= booking_close

    @staticmethod
    def get_price_per_person(event):
        """
        Return event ticket price.
        """

        return int(event["Price Per Person"])

    @staticmethod
    def create_event(
        event_name,
        event_date,
        booking_open,
        booking_close,
        price_per_person,
    ):
        """
        Create a new event.
        """

        event = {

            "Event ID": EventService.generate_event_id(),

            "Event Name": event_name,

            "Event Date": event_date,

            "Price Per Person": price_per_person,

            "Booking Open": booking_open,

            "Booking Close": booking_close,

            "Status": EVENT_OPEN_STATUS,

        }

        ExcelManager.save_event(event)

        return {
            "success":True,
            "message":"Event Created Successfully",
            "event":event
        }            
    @staticmethod
    def close_event(event_id):
        """
        close an events.
        """    
        event = ExcelManager.get_event_by_id(event_id)

        if event is None:

            return {

                "success": False,

                "message": "Event not found."

            }

        ExcelManager.update_event_status(
            event_id,
            EVENT_CLOSED_STATUS
        )

        return {

            "success": True,

            "message": "Event closed successfully."

        }

    @staticmethod
    def complete_event(event_id):
        """
        Mark an event as complete.
        """    
        event=ExcelManager.get_event_by_id(event_id)
        if event in None:
            return {
                "success":False,
                "message":"Event not found"
            }

        ExcelManager.update_event_status(
            event_id,
            EVENT_COMPLETED_STATUS
        )

        return {

            "success": True,

            "message": "Event completed successfully."

        }
    @staticmethod
    def total_events():
        """
        Return total number of events.
        """

        return ExcelManager.total_events()

    @staticmethod
    def total_open_events():
        """
        Return total number of open events.
        """

        return len(
            ExcelManager.get_open_events()
        )    