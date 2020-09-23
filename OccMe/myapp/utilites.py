from django.core.exceptions import ValidationError

def validatePhone(phone : str) -> str :
    """ Validate if the phone number has egyptian pattern"""
    if len(phone) == 11 :
        if phone[:2] == "01" :
            if phone[3] in ["0" , "2" , "5" , "1"] :
                return phone
    else :
        raise ValidationError("You Enter Wrong Phone Number")
