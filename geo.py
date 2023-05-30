import requests

from prettytable import PrettyTable

import colorama

from colorama import Fore

# Initialize colorama

colorama.init()

# Logo

logo = f'''{Fore.LIGHTGREEN_EX}

============================================================{Fore.YELLOW}

                         Geo Locator

                          by Crank{Fore.LIGHTGREEN_EX}

============================================================{Fore.RESET}

'''

# Colors

inputColor = Fore.GREEN

tableColor = Fore.LIGHTBLUE_EX

heartColor = Fore.WHITE + Fore.LIGHTMAGENTA_EX

def get_ip_info(ip_address):

    # Using ip-api.com for IP information

    url = f"http://ip-api.com/json/{ip_address}"

    response = requests.get(url)

    data = response.json()

    return data

def main():

    print(logo)

    ip_address = input(f"{inputColor}Enter the IP address:{Fore.LIGHTGREEN_EX} ")

    table = PrettyTable()

    table.field_names = ["Info Type", "Info"]

    ip_info = get_ip_info(ip_address)

    table.add_row(["IP", ip_info.get("query")])

    table.add_row(["City", ip_info.get("city")])

    table.add_row(["Region", ip_info.get("regionName")])

    table.add_row(["Country", ip_info.get("country")])

    table.add_row(["ISP", ip_info.get("isp")])

    table.add_row(["Latitude", ip_info.get("lat")])

    table.add_row(["Longitude", ip_info.get("lon")])

    table.add_row(["ZIP Code", ip_info.get("zip")])

    table.add_row(["Timezone", ip_info.get("timezone")])

    table.add_row(["Organization", ip_info.get("org")])

    table.add_row(["AS", ip_info.get("as")])

    horizontal_line = f"{heartColor}♡{Fore.LIGHTGREEN_EX}" * (len(table.field_names[0]) + len(table.field_names[1]) + 47)

    table_string = horizontal_line + "\n" + str(table) + "\n" + horizontal_line

    print(table_string)

if __name__ == '__main__':

    main()

