from datetime import datetime
import uuid

from utils.excel_utils import ExcelManager
from utils.constants import (
    BOOKING_PENDING,
    PAYMENT_PENDING,
)

class BookingService:
    @staticmethod
    def generate_booking_id():
        """
        Generate unique Booking ID
        Example:
        BK-9F2D8A31
        """
        return f"BK-{uuid.uuid4().hex[:8].upper()}"

    @staticmethod
    def generate_pass_id():
        """
        Generate unique Pass ID
        Example:
        PASS-AB12CD34
        """
        return f"PASS-{uuid.uuid4().hex[:8].upper()}"

    @staticmethod
    def get_members(flat_no):
        """
        Return All Members of a flat.
        """        
        return ExcelManager.get_members_by_flats(flat_no)

    @staticmethod
    def is_duplicate_booking(event_id,flat_no):
        """
        Check whether booking already exists.
        """
        return ExcelManager.booking_exists(
            event_id,
            flat_no
        )    

    @staticmethod
    def calculate_amount(
        selected_members,
        price_per_person
    ):
        """
        Calculate total booking amount.
        """

        total_members = len(selected_members)

        total_amount = total_members * price_per_person

        return total_members, total_amount

    @staticmethod
    def create_booking(
        event_id,
        wing,
        flat_no,
        selected_members,
        price_per_person
    ):
        """
        Create booking after validation.
        """
         # Duplicate Booking

        if BookingService.is_duplicate_booking(event_id,flat_no):
            return {
                "success":False,
                "message":"Booking Already Exists."
            }   

        # Calculate Amount
        total_members, total_amount = (
            BookingService.calculate_amount(
                selected_members,
                price_per_person
            )
        )

        #Ids

        booking_id=BookingService.generate_booking_id()

        pass_id=BookingService.generate_pass_id()

        #Member Details

        member_ids = ",".join(
            member["Member ID"]
            for member in selected_members
        )

        member_names = ",".join(
            member["Name"]
            for member in selected_members
        )  

        # Booking Record      

        booking = {

            "Booking ID": booking_id,

            "Event ID": event_id,

            "Wing": wing,

            "Flat No": flat_no,

            "Member IDs": member_ids,

            "Member Names": member_names,

            "Total Members": total_members,

            "Total Amount": total_amount,

            "Payment Status": PAYMENT_PENDING,

            "Booking Status": BOOKING_PENDING,

            "Pass ID": pass_id,

            "Booking Date": datetime.now().strftime(
                "%d-%m-%Y %H:%M:%S"
            )

        }

        ExcelManager.save_booking(booking)

        return 
        {
            "success":True,
            "message":"Booking Created Successfully",
            "booking":booking
        } 