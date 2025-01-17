from .proton_import import send_ics_to_proton
import os

def main():
    ics_file = "calender.ics" # Replace with path to .ics file.
    proton_email = os.getenv("PROTON_EMAIL")
    proton_import_email = os.getenv("PROTON_IMPORT_EMAIL")
    send_ics_to_proton(ics_file, proton_email, proton_import_email)

if __name__ == "__main__":
    main()
    