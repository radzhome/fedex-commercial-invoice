# generate_invoice test
from fedex_invoice.invoice import generate_commercial_invoice


# TODO: refactor the structures here

# Includes company info.
export_data = {'company': 'Radtek Inc.', 'address': '123 Main St.',
               'city': 'Toronto', 'state_code': 'ON', 'postal_code': 'L8J 1V4', 'country_code': 'CA',
               'waybill_no': '9999 9999 9999', 'export_date': '12/20/2015', 'export_refs': '999432423, 14314321423',
               'export_country': 'USA', 'manufacture_country': 'CHINA',
               'destination_country': 'CANADA'}

# email, phone ? address1, address2 lines ? suite? etc?

importer_data = {'first_name': 'Real First Name',
                 'last_name': 'Real Last Name',
                 'postal_code': 'M5A 3C6', 'country_code': 'CA', 'state_code': 'ON',
                 'city': 'North York', 'address': '123 Import St.'}

exporter_data = {'first_name': 'Real First Name',
                 'last_name': 'Real Last Name',
                 'postal_code': 'M5A 3C6', 'country_code': 'CA', 'state_code': 'ON',
                 'city': 'North York', 'address': '123 Export St.'}

cosignee_data = {'first_name': 'Real First Name',
                 'last_name': 'Real Last Name',
                 'postal_code': 'M5A 3C6', 'country_code': 'CA', 'state_code': 'ON',
                 'city': 'North York', 'address': '123 Cosignee St.'}

product1 = {'marks_nos': '1234', 'no_packages': 1, 'package_type': 'BOX',
            'description': 'a description of the goods in a full and up to date way', 'quantity': 1,
            'measure_unit': 'lbs', 'weight': 25, 'unit_value': 23.24, 'total_value': 23.24}

product2 = {'marks_nos': '12', 'no_packages': 1, 'package_type': 'OWN_PACKAGING',
            'description': 'a description of the goods, another product to describe', 'quantity': 2,
            'measure_unit': 'lbs', 'weight': 5, 'unit_value': 43.44, 'total_value': 43.44}

flags = {'fob': True, 'caf': True, 'cif': False}

# Test products
products = [product1, product2, product1, product2, product1, product2]

generate_commercial_invoice(export_data, exporter_data, cosignee_data, products, flags, importer_data)
