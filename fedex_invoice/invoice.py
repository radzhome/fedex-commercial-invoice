import os


def format_phone_number(value):
    if not value:
        return ''
    if len(value) == 10:
        phone = '({0}){1}-{2}'.format(value[0:3], value[3:6], value[6:10])
    elif len(value) == 11:
        phone = '+{0}({1}){2}-{3}'.format(value[0], value[1:4], value[4:7], value[7:11])
    else:
        phone = value

    return phone


# TODO: file path shoudl be None default, to return as buffer
def generate_commercial_invoice(export_data, exporter_data, cosignee_data, products, flags, importer_data=None,
                                file_path="output_commercial_invoice.pdf"):  # self, request, *args, **kwargs):

    current_directory = os.path.dirname(os.path.realpath(__file__))

    from reportlab.lib.enums import TA_CENTER, TA_RIGHT, TA_LEFT
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

    from reportlab.lib import colors
    from reportlab.lib.pagesizes import cm
    from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image, PageBreak

    # TODO: return as buffer vs file
    # if file_path = None then return buffer instead
    doc = SimpleDocTemplate(file_path, rightMargin=.5 * cm, leftMargin=.5 * cm,
                            topMargin=1.5 * cm, bottomMargin=1.5 * cm)

    story = []

    # Styles
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Center', alignment=TA_CENTER))
    styles.add(ParagraphStyle(name='Right', alignment=TA_RIGHT))
    styles.add(ParagraphStyle(name='Left', alignment=TA_LEFT))
    styles.add(ParagraphStyle(name='Line_Data', alignment=TA_LEFT, fontSize=8, leading=7))
    styles.add(ParagraphStyle(name='Line_Data_Small', alignment=TA_LEFT, fontSize=7, leading=8))
    styles.add(ParagraphStyle(name='Line_Data_Large', alignment=TA_LEFT, fontSize=12, leading=12))
    styles.add(ParagraphStyle(name='Line_Data_Largest', alignment=TA_LEFT, fontSize=14, leading=15))
    styles.add(ParagraphStyle(name='Line_Label', font='Helvetica-Bold', fontSize=7, leading=6, alignment=TA_LEFT))
    styles.add(ParagraphStyle(name='Line_Label_Center', font='Helvetica-Bold', fontSize=7, alignment=TA_CENTER))

    # Get company information
    company_address = '{0}<br />{1}, {2}<br />{3} {4}'.format(export_data['address'],
                                                              export_data['city'],
                                                              export_data['state_code'],
                                                              export_data['postal_code'],
                                                              export_data['country_code'])
    data1 = [[Paragraph(export_data['company'], styles["Line_Data_Large"])],
             [Paragraph('COMPANY NAME', styles["Line_Label"])],
             [Paragraph(company_address, styles["Line_Data_Large"])],
             [Paragraph('COMPANY ADDRESS', styles["Line_Label"])]
    ]

    t1 = Table(data1, colWidths=(9 * cm))  # , rowHeights = [.3*cm, .5*cm, .3*cm, .5*cm])
    t1.setStyle(TableStyle([
        ('INNERGRID', (0, 0), (0, 1), 0.25, colors.black),
        ('INNERGRID', (0, 2), (0, 3), 0.25, colors.black),
    ]))
    t1.hAlign = 'RIGHT'

    story.append(t1)

    story.append(Spacer(0.1 * cm, .5 * cm))

    story.append(Paragraph("COMMERCIAL INVOICE", styles["Line_Label_Center"]))

    data1 = [[Paragraph('INTERNATIONAL<br /> AIR WAYBILL NO.', styles["Line_Label"]),
              Paragraph(export_data['waybill_no'], styles["Line_Data_Largest"]),
              Paragraph('<b>NOTE: ALl shipments must be <br /> '
                        'accompanied by a Fedex Express <br /> '
                        'international Air Waybill.</b>', styles["Line_Data_Small"]),
             ]]

    t1 = Table(data1, colWidths=(3 * cm, None, 4.5 * cm,))
    t1.setStyle(TableStyle([
        ('INNERGRID', (1, 0), (-1, -1), 0.25, colors.black),
        ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))

    story.append(t1)

    data1 = [[Paragraph('DATE OF EXPORTATION', styles["Line_Label"]),
              Paragraph('EXPORT REFERENCES (i.e. order no., invoice no.)', styles["Line_Label"])],
             [Paragraph(export_data['export_date'], styles["Line_Data_Largest"]),
              Paragraph(export_data['export_refs'], styles["Line_Data_Largest"]),
             ]]
    t1 = Table(data1)
    t1.setStyle(TableStyle([
        ('INNERGRID', (0, 0), (1, 0), 0.25, colors.black),
        ('INNERGRID', (0, 1), (1, 1), 0.25, colors.black),
        ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    story.append(t1)

    # Shipper/Exporter, Cosignee

    address_paragraph = \
        "{first_name}, {last_name}<br />" \
        "{address}<br />" \
        "{city}, {state_code} <br />" \
        "{postal_code}, <br />" \
        "{country_code}"

    cosignee_paragraph = address_paragraph.format(**cosignee_data)
    exporter_paragraph = address_paragraph.format(**exporter_data)

    data1 = [[Paragraph('SHIPPER/EXPORTER (complete name and address)', styles["Line_Label"]),
              Paragraph('CONSIGNEE (complete name and address)', styles["Line_Label"])],

             [Paragraph(cosignee_paragraph, styles["Line_Data_Large"]),
              Paragraph(exporter_paragraph, styles["Line_Data_Large"])]
             ]

    t1 = Table(data1)
    t1.setStyle(TableStyle([
        ('INNERGRID', (0, 0), (1, 0), 0.25, colors.black),
        ('INNERGRID', (0, 1), (1, 1), 0.25, colors.black),
        ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    story.append(t1)

    if not importer_data:
        # importer_data = {'first_name': '', 'last_name': '',
        #                  'postal_code': '', 'country_code': '', 'state_code': '',
        #                  'city': '', 'address': ''}
        importer_paragraph = ''
    else:
        importer_paragraph = address_paragraph.format(**importer_data)

    data1 = [[Paragraph('COUNTRY OF EXPORT', styles["Line_Label"]),
              Paragraph('IMPORTER -- IF OTHER THAN CONSIGNEE <br />(complete name and address)', styles["Line_Label"])],
             [Paragraph(export_data['export_country'], styles["Line_Data_Largest"]),
              Paragraph(importer_paragraph, styles["Line_Data_Large"])],
             [Paragraph('COUNTRY OF MANUFACTURE', styles["Line_Label"]), ''],
             [Paragraph(export_data['manufacture_country'], styles["Line_Data_Largest"]), ''],
             [Paragraph('COUNTRY OF ULTIMATE DESTINATION', styles["Line_Label"]), ''],
             [Paragraph(export_data['destination_country'], styles["Line_Data_Largest"]), ''],
    ]
    t1 = Table(data1)
    t1.setStyle(TableStyle([
        ('INNERGRID', (0, 1), (0, 2), 0.25, colors.black),
        ('INNERGRID', (0, 3), (0, 4), 0.25, colors.black),
        ('INNERGRID', (0, 0), (1, 0), 0.25, colors.black),
        ('INNERGRID', (0, 1), (1, 1), 0.25, colors.black),
        ('INNERGRID', (0, 2), (1, 2), 0.25, colors.black),
        ('INNERGRID', (0, 3), (1, 3), 0.25, colors.black),
        ('INNERGRID', (0, 4), (1, 4), 0.25, colors.black),
        ('INNERGRID', (0, 5), (1, 5), 0.25, colors.black),
        ('SPAN', (1, 1), (1, 5)),
        ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    story.append(t1)

    data1 = [[Paragraph('MARKS/NOS.', styles["Line_Label"]),
              Paragraph('NO. OF<br />PKGS.', styles["Line_Label"]),
              Paragraph('TYPE OF<br />PACKAGING', styles["Line_Label"]),
              Paragraph('FULL DESCRIPTION OF GOODS', styles["Line_Label"]),
              Paragraph('QTY.', styles["Line_Label"]),
              Paragraph('UNIT OF MEA-<br />SURE', styles["Line_Label"]),
              Paragraph('WEIGHT', styles["Line_Label"]),
              Paragraph('UNIT VALUE', styles["Line_Label"]),
              Paragraph('TOTAL<br />VALUE.', styles["Line_Label"])],
    ]

    t1 = Table(data1, colWidths=(1.7 * cm, 1.3 * cm, 2 * cm, 7 * cm, 1 * cm, 1.5 * cm, 1.5 * cm, 1.8 * cm, 1.8 * cm))
    t1.setStyle(TableStyle([
        ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
        ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    story.append(t1)

    data1 = [[Paragraph(str(product['marks_nos']), styles["Line_Data"]),
              Paragraph(str(product['no_packages']), styles["Line_Data"]),
              Paragraph(str(product['package_type']), styles["Line_Data"]),
              Paragraph(str(product['description']), styles["Line_Data"]),
              Paragraph(str(product['quantity']), styles["Line_Data"]),
              Paragraph(str(product['measure_unit']), styles["Line_Data"]),
              Paragraph(str(product['weight']), styles["Line_Data"]),
              Paragraph(str(product['unit_value']), styles["Line_Data"]),
              Paragraph(str(product['total_value']), styles["Line_Data"])] for product in products]

    t1 = Table(data1, colWidths=(1.7 * cm, 1.3 * cm, 2 * cm, 7 * cm, 1 * cm, 1.5 * cm, 1.5 * cm, 1.8 * cm, 1.8 * cm))
    t1.setStyle(TableStyle([
        ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
        ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    story.append(t1)

    total_packages = 0
    total_weight = 0.0
    total_value = 0.0

    for product in products:
        total_packages += product['no_packages']
        total_weight += product['weight']
        total_value += product['total_value']

    data1 = [['',
              Paragraph('TOTAL NO OF PKGS.', styles["Line_Label"]),
              '',
              Paragraph('TOTAL WEIGHT', styles["Line_Label"]),
              '',
              Paragraph('TOTAL INVOICE VALUE', styles["Line_Label"]),
              ],
             ['',
              Paragraph(str(total_packages), styles["Line_Data"]),
              Paragraph('SEE http://www.fedex.com FOR MORE INFORMATION ON THE CORPORATE INVOICE.',
                        styles["Line_Label_Center"]),
              Paragraph(str(total_weight), styles["Line_Data"]),
              '',
              Paragraph('${0}'.format(total_value), styles["Line_Data"]),
              ]]

    t1 = Table(data1, colWidths=(1.7 * cm, 1.3 * cm, 11.5 * cm, 1.5 * cm, 1.8 * cm, 1.8 * cm))
    t1.setStyle(TableStyle([
        ('INNERGRID', (1, 0), (1, 1), 0.25, colors.black),
        ('INNERGRID', (3, 0), (3, 1), 0.25, colors.black),
        ('INNERGRID', (5, 0), (5, 1), 0.25, colors.black),
        ('BOX', (1, 0), (1, 1), 0.25, colors.black),
        ('BOX', (3, 0), (3, 1), 0.25, colors.black),
        ('BOX', (5, 0), (5, 1), 0.25, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    story.append(t1)

    checked_image_path = os.path.join(current_directory, 'images/checked.png')
    unchecked_image_path = os.path.join(current_directory, 'images/unchecked.png')

    flag_image_paths = {}
    for key, value in flags.items():
        flag_image_paths[key] = checked_image_path if value else unchecked_image_path

    check_data = [[Paragraph('Check one', styles["Line_Label"]), ''],
                  [Image(flag_image_paths['fob'], .25 * cm, .25 * cm), Paragraph('F.O.B.', styles["Line_Label"])],
                  [Image(flag_image_paths['caf'], .25 * cm, .25 * cm), Paragraph('C & F', styles["Line_Label"])],
                  [Image(flag_image_paths['cif'], .25 * cm, .25 * cm), Paragraph('C.I.F.', styles["Line_Label"])]]
    tc = Table(check_data, colWidths=(.4 * cm, None))
    tc.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('SPAN', (0, 0), (1, 0)),
    ]))

    data1 = [[Paragraph(
        'For U.S. EXPORT ONLY: THESE COMMODITIES, TECHNOLOGY OR SOFTWARE WERE EXPORTED FROM THE UNITED STATES '
        'IN ACCORDANCE WITH THE EXPORT ADMINISTRATION REGULATIONS. DIVERSION CONTRARY TO THE UNITED STATES LAW '
        'IS PROHIBITED.', styles["Line_Label"]), '',
              tc]]
    t1 = Table(data1, colWidths=(None, 3.3 * cm, 1.8 * cm))
    t1.setStyle(TableStyle([
        ('BOX', (2, 0), (2, 0), 0.25, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    story.append(t1)

    story.append(Table([[Paragraph('I DECLARE THE INFORMATION CONTAINED IN THIS '
                                   'INVOICE TO BE TRUE AND CORRECT', styles["Line_Label"])]]))

    story.append(Spacer(0.1 * cm, .5 * cm))

    # TODO: signature could be image ? Date could be sign_date ?
    # TODO: signature, date
    data1 = [
        [Paragraph(export_data['company'], styles["Line_Data_Large"]), '',
         Paragraph(export_data['export_date'], styles["Line_Data_Large"])
        ],
        [Paragraph('SIGNATURE OF SHIPPER/EXPORTER (Type name and title and sign.)', styles["Line_Label"]), '',
         Paragraph('DATE', styles["Line_Label"])]]

    t1 = Table(data1, colWidths=(None, 2*cm, None))
    t1.setStyle(TableStyle([
        ('INNERGRID', (0, 0), (0, 1), 0.25, colors.black),
        ('INNERGRID', (2, 0), (2, 1), 0.25, colors.black),
    ]))

    story.append(t1)

    doc.build(story)

