
import requests
import requests.utils as utils

def currency_rates(Char_Code):

    from requests import get, utils

    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)

    my_list = content.split('Valute ID')

    my_value = None
    for i in my_list:
        if Char_Code in i:
            my_valute = i

            my_сode = my_valute[my_valute.find("<CharCode>") + 10:my_valute.find("</CharCode>")]
            my_value = my_valute[my_valute.find("<Value>") + 7:my_valute.find("</Value>")]
            my_value = my_value.replace(',', '.')
            my_value = float(my_value)

            #print(my_сode, my_value)
    return (my_value)


#a = currency_rates('RON')
print('EUR =', currency_rates('EUR'))
print('USD =', currency_rates('USD'))
print('RUR =', currency_rates('RUR'))
