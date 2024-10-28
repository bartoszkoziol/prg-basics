def mask_credit_card(card_number):
    if len(card_number) != 16:
        return "Nieprawidłowy numer karty. Numer musi mieć dokładnie 16 cyfr."
    
    masked_number = card_number[:2]+'*'*10+card_number[-4:]
    return masked_number
