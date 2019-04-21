from auth import *


def get_all_records_by_key(gss_client, key):
    wks = gss_client.open_by_key(key)
    sheet = wks.sheet1
    for r in sheet.get_all_records():
        print(r)


def get_all_values(gss_client, key):
    wks = gss_client.open_by_key(key)
    sheet = wks.sheet1
    for r in sheet.get_all_values():
        print(r)


def get_cell(gss_client, key, row, column):
    wks = gss_client.open_by_key(key)
    sheet = wks.sheet1
    B1 = sheet.cell(row, column)
    print(B1.value)


spreadsheet_key_path = 'spreadsheet_key.txt'

with open(spreadsheet_key_path) as f:
    spreadsheet_key = f.read().strip()

get_all_records_by_key(gss_client, spreadsheet_key)
get_all_values(gss_client, spreadsheet_key)
get_cell(gss_client, spreadsheet_key, 1, 2)
