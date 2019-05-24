from pyfiglet import figlet_format
import socket
import os
import platform
from Network import *


def back_to_menu():
    print()
    back = input('\033[92mDo you want to continue? [y/n]: ')
    if back[0].lower() == 'y':
        print()
        run_information_gathering_tool()
    elif back[0].lower() == 'n':
        exit()
    else:
        exit()


def information_gathering_menu():
    print("""\033[96m
    
    1) DNS Lookup                   8) MTR Trace Route
    2) Whois Lookup                 9) Reverse IP Lookup
    3) GeoIP Lookup                 10) Subnet Lookup
    4) Port Scanner                 11) Page Links
    5) Zone Transfer                12) HTTP Header
    6) Subdomains Finder            13) Get Robots.txt     
    7) Find Shared DNS servers      14) Exit
       """)
    print()


def gathering_information(menu_index, target):
    if menu_index == 1:
        dns_look_up_url = 'https://api.hackertarget.com/dnslookup/?q=' + target
        dns_info = http_request(dns_look_up_url)
        if dns_info.status_code == 200:
            print('\n\033[36m' + 'DNS Records for domain: ', target + '\n')
            print('\033[30m' + dns_info.text)
            back_to_menu()
    elif menu_index == 2:
        whois_url = 'https://api.hackertarget.com/whois/?q=' + target
        whois_info = http_request(whois_url)
        if whois_info.status_code == 200:
            print('\n\033[36m' + 'Whois Lookup for domain: ', target + '\n')
            print('\033[30m' + whois_info.text)
            back_to_menu()
    elif menu_index == 3:
        geo_ip_lookup_url = 'https://api.hackertarget.com/geoip/?q=' + target
        geo_ip_lookup_info = http_request(geo_ip_lookup_url)
        if geo_ip_lookup_info.status_code == 200:
            print('\n\033[36m' + 'GeoIP Lookup for domain: ', target + '\n')
            print('\033[30m' + geo_ip_lookup_info.text)
            back_to_menu()
    elif menu_index == 4:
        tcp_port_scanner_url = 'https://api.hackertarget.com/nmap/?q=' + target
        tcp_port_scanner_info = http_request(tcp_port_scanner_url)
        if tcp_port_scanner_info.status_code == 200:
            print('\n\033[36m' + 'TCP Port Scanner for domain: ', target + '\n')
            print('\033[30m' + tcp_port_scanner_info.text)
            back_to_menu()
    elif menu_index == 5:
        zone_transfer_url = 'https://api.hackertarget.com/zonetransfer/?q=' + target
        zone_transfer_info = http_request(zone_transfer_url)
        if zone_transfer_info.status_code == 200:
            print('\n\033[36m' + 'Zone Transfer for domain: ', target + '\n')
            print('\033[30m' + zone_transfer_info.text)
            back_to_menu()
    elif menu_index == 6:
        sub_domain_url = 'https://api.hackertarget.com/hostsearch/?q=' + target
        sub_domain_info = http_request(sub_domain_url)
        if sub_domain_info.status_code == 200:
            print('\n\033[36m' + 'Subdomains for domain: ', target + '\n')
            print('\033[30m' + sub_domain_info.text)
            back_to_menu()
    elif menu_index == 7:
        share_dns_server_url = 'https://api.hackertarget.com/findshareddns/?q=' + target
        share_dns_server_info = http_request(share_dns_server_url)
        if share_dns_server_info.status_code == 200:
            print('\n\033[36m' + 'Domains sharing DNS server with domain: ', target + '\n')
            print('\033[30m' + share_dns_server_info.text)
            back_to_menu()
    elif menu_index == 8:
        traceroute_mtr_url = 'https://api.hackertarget.com/mtr/?q=' + target
        traceroute_mtr_info = http_request(traceroute_mtr_url)
        if traceroute_mtr_info.status_code == 200:
            print('\n\033[36m' + 'DOnline traceroute using MTR for domain: ', target + '\n')
            print('\033[30m' + traceroute_mtr_info.text)
            back_to_menu()
    elif menu_index == 9:
        reverse_ip_lookup_url = 'https://api.hackertarget.com/reverseiplookup/?q=' + target
        reverse_ip_lookup_info = http_request(reverse_ip_lookup_url)
        if reverse_ip_lookup_info.status_code == 200:
            print('\n\033[36m' + 'Reverse IP Lookup for domain: ', target + '\n')
            print('\033[30m' + reverse_ip_lookup_info.text)
            back_to_menu()
    elif menu_index == 10:
        subnet_lookup_url = 'https://api.hackertarget.com/subnetcalc/?q=' + target
        subnet_lookup_info = http_request(subnet_lookup_url)
        if subnet_lookup_info.status_code == 200:
            print('\n\033[36m' + 'Subnet Lookup for domain: ', target + '\n')
            print('\033[30m' + subnet_lookup_info.text)
            back_to_menu()
    elif menu_index == 11:
        page_links_url = 'https://api.hackertarget.com/pagelinks/?q=' + target
        page_links_info = http_request(page_links_url)
        if page_links_info.status_code == 200:
            print('\n\033[36m' + 'Page Links for domain: ', target + '\n')
            print('\033[30m' + page_links_info.text)
            back_to_menu()
    elif menu_index == 12:
        http_headers_url = 'https://api.hackertarget.com/httpheaders/?q=' + target
        http_headers_info = http_request(http_headers_url)
        if http_headers_info.status_code == 200:
            print('\n\033[36m' + 'HTTP Header for domain: ', target + '\n')
            print('\033[30m' + http_headers_info.text)
            back_to_menu()
    elif menu_index == 13:
        robots_txt_url = 'http://' + target + '/robots.txt'
        robots_txt_info = http_request(robots_txt_url)
        if robots_txt_info.status_code == 200:
            print('\n\033[36m' + 'Robots.txt for domain: ', target + '\n')
            print('\033[30m' + robots_txt_info.text)
            back_to_menu()
    elif menu_index == 14:
        exit()


def run_information_gathering_tool():
    information_gathering_menu()
    target = ''
    try:
        what = input('\033[92mDo you want to collect information of a website or IP address? [website/IP]: ')
        if what[0].upper() == 'W':
            target = input('Enter the website address: ')
        elif what[0].upper() == 'I':
            target = input('Enter the IP address (or domain to get IP address of that domain): ')
            target = socket.gethostbyname(target)
            print('The IP address of the target is:', target)
        else:
            print('\033[31m' + 'Incorrect input. Please re run the script and enter valid input to proceed further!!')
            exit()

        choose = int(input('what information would you like to collect? (1-15): '))
        gathering_information(choose, target)

    except socket.gaierror:
        print('Name or service unknown! \033[93m')


def main():
    print("""\033[093m""" + figlet_format('Information Gathering'))
    run_information_gathering_tool()


if __name__ == '__main__':
    main()
