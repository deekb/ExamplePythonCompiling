#!/bin/python3
from argparse import ArgumentParser
from os import path, name, geteuid

parser = ArgumentParser(description='My Example Description (Change this in init.py)')

INSTALLED = (path.dirname(path.abspath(__file__)) == path.join(path.sep, "usr", "bin"))
ON_WINDOWS = (name == "nt")
IS_ROOT = (not geteuid())
# DEBUG = ("DEBUG" in environ)

# if DEBUG:
#     print("Debug mode is activated")
#     print(f"GEOLOCATION_API_URL: {GEOLOCATION_API_URL}")
#     print(f"INTERNET_CHECK_URL: {INTERNET_CHECK_URL}")
#     print(f"INTERNET_CHECK_TIMEOUT_SECONDS: {INTERNET_CHECK_TIMEOUT_SECONDS}")
#     print("if you do not wish to see this message then run \"unset DEBUG\" in bash")

if __name__ == "__main__":
    parser = ArgumentParser(description='Get data about IP addresses.')

    parser.add_argument('--city', action='store_true', help='Print the city of the address')
    parser.add_argument('--zip', action='store_true', help='Print the ZIP code of the address')
    parser.add_argument('--isp', action='store_true', help='Print the Internet Service Provider(ISP) of the address')
    parser.add_argument('--country', action='store_true', help='Print the country of the address')
    parser.add_argument('--region', action='store_true', help='Print the region of the address')
    parser.add_argument('--timezone', action='store_true', help='Print the time zone of the address')
    parser.add_argument('--all', action='store_true', help='Print all data about the address')
    parser.add_argument('--install', action='store_true', help='install this script to your /usr/bin directory ('
                                                               'Unix/MacOS only)')
    parser.add_argument('IP', type=str, nargs='?', help='An IP address (V4/V6)')
    args = parser.parse_args()

    if args.IP:
        IP = args.IP
    else:
        IP = ""
    shownFields = []
    if args.all or True not in [args.city, args.zip, args.isp, args.country, args.region, args.timezone]:
        shownFields = ["city", "zip", "isp", "country", "region", "timezone"]
    else:
        if args.city:
            shownFields.append("city")
        if args.zip:
            shownFields.append("zip")
        if args.isp:
            shownFields.append("isp")
        if args.country:
            shownFields.append("country")
        if args.region:
            shownFields.append("region")
        if args.timezone:
            shownFields.append("timezone")

    if args.install:
        if ON_WINDOWS:
            print("Running on Windows, installation is unavailable")
        else:
            if not IS_ROOT:
                print("Not running as root, can't install!")
            else:
                print("Installing")
                print(f"copy {path.abspath(__file__)} to /usr/bin/ip-geolocator")
                # copyfile(path.abspath(__file__), path.join(path.sep, "usr", "bin", "ip-geolocator"))
    try:
        import main
    except KeyboardInterrupt:
        print()
        print("KeyboardInterrupt")
