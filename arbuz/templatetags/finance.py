from arbuz.templatetags.base import *


class Finance_Manager(Base_Tag_Manager):

    def Get_Brutto_Value(self):
        price = self.values['price']
        rate = self.values['rate']
        return format(price * (100 + rate) / 100, '.2f')

    def Get_VAT_Value(self):
        price = self.values['price']
        rate = self.values['rate']
        variant = self.values['variant']

        vats = {
            'netto': format(price * rate / 100, '.2f'),
            'brutto': format(price * rate / 100, '.2f')
        }

        return vats[variant]



@register.simple_tag
def brutto(price, rate):

    task = 'Get_Brutto_Value'
    values = {
        'price': price,
        'rate': rate
    }

    return Finance_Manager(task, values).OUT

@register.simple_tag
def vat(price, rate, variant='netto'):

    task = 'Get_VAT_Value'
    values = {
        'price': price,
        'rate': rate,
        'variant': variant
    }

    return Finance_Manager(task, values).OUT
