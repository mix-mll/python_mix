import csv
import glob
import logging
import os

import openpyxl

# file_name, column_index, delimiter, with_header
EMPLOYEES_EMAIL_FILE = [
    "csv_vs_xlms_lists/employees_email.csv",
    2,
    ";",
    True,
]  # fix list
CONFIRMED_EMPLOYEES_FILE = [
    "csv_vs_xlms_lists/Christmas Party _ *.xlsx",
    3,
    ";",
    True,
]  # file name patern that gets updated and get the latest
PENDING_EMAIL_FILE = "csv_vs_xlms_lists/pending_email.csv"  # result list


def get_emails_from_csv(file_name, column_index, delimiter, with_header):
    """
    Returns the sum of two decimal numbers in binary digits.

            Parameters:
                    file_name (string): name of the csv file
                    column_index (int): column where the email data is, from 0

            Returns:
                    emails (set[string]): list of the emails
    """
    logging.info(f"reading {file_name=}")
    with open(file_name, "r", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=delimiter)
        if with_header:
            next(reader)
        emails = set(row[column_index] for row in reader)
        check_vailid_email(emails)
    return emails


def get_confirmed_from_xlsx(file_name, column_index, delimiter, with_header):
    wb = openpyxl.load_workbook(file_name)
    ws = wb.active
    emails = set(row[column_index] for row in ws.iter_rows(values_only=True))
    check_vailid_email(emails)
    return emails


def __get_latest_confirmed_list__():
    """# name templete that gets updated and get the latest for the file name patern"""
    max_time = 0
    for f in glob.glob(CONFIRMED_EMPLOYEES_FILE[0]):
        file_time = os.path.getctime(f)
        if file_time > max_time:
            max_time = file_time
            latest_file = f
    CONFIRMED_EMPLOYEES_FILE[0] = latest_file


def check_vailid_email(emails):
    one_email = next(iter(emails))
    if "@" not in one_email:
        raise ValueError(f"NO VALID EMAIL. example: <<{one_email}>>")


def main() -> int:
    """proces employees list and remove confirmed"""
    all_emails = get_emails_from_csv(*EMPLOYEES_EMAIL_FILE)
    # print(next(iter(all_emails)))

    __get_latest_confirmed_list__()
    confirmed_emails = get_confirmed_from_xlsx(*CONFIRMED_EMPLOYEES_FILE)
    # print(next(iter(confirmed_emails)))

    pending_emails = sorted(all_emails - confirmed_emails)
    print("PENDING:", len(pending_emails))
    with open(PENDING_EMAIL_FILE, "w", encoding="utf-8") as f:
        writer = csv.writer(f)
        # writer.writerow(header)
        writer.writerows(zip(pending_emails))

    pending_emails_txt = "; ".join(pending_emails)
    print(pending_emails_txt)


if __name__ == "__main__":
    logging.getLogger().setLevel(logging.INFO)
    main()
