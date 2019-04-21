from auth import *
import datetime


def update_sheet(gss_client, key, today, item, price):
    wks = gss_client.open_by_key(key)
    sheet = wks.sheet1
    sheet.insert_row([str(today), item, price], 2)
    sheet.insert_row([str(today), item, price], 2)
    sheet.insert_row([str(today), item, price], 2)
    sheet.insert_row([str(today), item, price], 2)
    sheet.insert_row([str(today), item, price], 2)
    sheet.insert_row([str(today), item, price], 2)
    sheet.insert_row([str(today), item, price], 2)
    sheet.insert_row([str(today), item, price], 2)
    sheet.insert_row([str(today), item, price], 2)
    sheet.insert_row([str(today), item, price], 2)
    sheet.insert_row([str(today), item, price], 2)
    sheet.insert_row([str(today), item, price], 2)


spreadsheet_key_path = 'spreadsheet_key.txt'

today = datetime.datetime.now()
with open(spreadsheet_key_path) as f:
    spreadsheet_key = f.read().strip()

update_sheet(gss_client, spreadsheet_key, today, 'cheapest_item', 999)
