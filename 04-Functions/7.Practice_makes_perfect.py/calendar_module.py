def month_number(n):
    if n==1:
        result = "Styczeń"
    elif n==2:
        result = "Luty"
    elif n==3:
        result = "Marzec"
    elif n==4:
        result = "Kwiecień"
    elif n==5:
        result = "Maj"
    elif n==6:
        result = "Czerwiec"
    elif n==7:
        result = "Lipiec"
    elif n==8:
        result = "Sierpień"
    elif n==9:
        result = "Wrzesień"
    elif n==10:
        result = "Październik"
    elif n==11:
        result = "Listopad"
    elif n==12:
        result = "Grudzień"
    else:
        return "Podaj porawną liczbę od (1-12)"
    return result
