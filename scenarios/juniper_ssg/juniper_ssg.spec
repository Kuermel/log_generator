{
    "fields" : [
        { "templateCount" : {"count":14 } },
        { "datetime": {"type": "random", "generate_type":"datetime", "format": "%Y-%m-%d %H:%M:%S" } },
        { "url" : {"type": "from_list_file", "file" : "url.list", "method":"sequential" } },
        { "category" : {"type": "from_list_file", "file" : "category.list", "method":"sequential" } },
        { "ip" : {"type": "from_list_file", "file" : "ip.list", "method":"random" } },
        { "ip2" : {"type": "random", "generate_type":"IPv4" } },
        { "port" : {"type": "random", "generate_type":"integer", "min":1, "max":10000 } },
        { "port2" : {"type": "random", "generate_type":"integer", "min":1, "max":5000 } },
        { "pri" : {"type": "from_list_file", "file" : "pri.list", "method":"random" } },
        { "number" : {"type": "random", "generate_type":"integer", "min":1, "max":10000 } },
        { "sent" : {"type": "random", "generate_type":"integer", "min":1, "max":10000 } },
        { "rcvd" : {"type": "random", "generate_type":"integer", "min":1, "max":10000 } }
    ],
    "template" : [
        "XYZ: NetScreen device_id=XYZ  [Root]system-information-00536: IKE ${ip} Phase 2 msg ID 580d34ad: Completed negotiations with SPI 6f7c9327, tunnel ID 67, and lifetime ${number} seconds/${sent} KB. (${datetime})",
        "XYZ: NetScreen device_id=SDH12XYZ  [Root]system-critical-00033: Src IP session limit! From ${ip}:${port} to ${ip2}:${port2}, proto UDP (zone Trust int ethernet0/0). Occurred 2 times. (${datetime})",
        "XYZ-SSG320M: NetScreen device_id=XYZ-SSG320M  [Root]system-information-00769: UF-MGR: URL PERMITTED: ${ip}(${port})->${ip2}(${port2}) updates.cudasvc.com/cgi-bin/update.cgi CATEGORY: default REASON: BY_FAIL_MODE PROFILE: Martur (${datetime})",
        "NetScreen device_id=XYZ-SSG320M  [Root]system-warning-00601: CS:FLV has been detected from ${ip}/${port} to ${ip}/${port} through policy 1 1 times. (${datetime})",
        "XYZ-SSG5: NetScreen device_id=XYZ-SSG5  [Root]system-information-00524: SNMP request has been received from an unknown host in SNMP community public at ${ip}:${port}. (${datetime})",
        "XYZ-SSG320M: NetScreen device_id=XYZ-SSG320M  [Root]system-information-00536: IKE ${ip}:${port} Added Phase 2 session tasks to the task list. (${datetime})",
        "XYZ-ssg5: NetScreen device_id=XYZ-ssg5  [Root]system-information-00527: IP address ${ip} is assigned to 001e6598bc8a. (${datetime})",
        "XYZ-SSG5: NetScreen device_id=XYZ-SSG5  [Root]system-information-00536: Phase 2 SA for tunnel ID 8005 has been idle too long. Deactivated P2 SA and sent a Delete msg to peer. (${datetime})",
        "XYZ: NetScreen device_id=XYZ  [Root]system-notification-00257(traffic): start_time=\"${datetime}\" duration=${number} policy_id=2 service=icmp proto=1 src zone=Untrust dst zone=Trust action=Permit sent=${sent} rcvd=${rcvd} src=${ip} dst=${ip2} icmp type=8 src-xlated ip=${ip} dst-xlated ip=${ip2} session_id=46949 reason=Close - RESP",
        "XYZ-SSG5: NetScreen device_id=XYZ-SSG5 [Root]system-notification-00257(traffic): start_time=\"${datetime}\" duration=${number} policy_id=1 service=tcp/port:${port} proto=6 src zone=Trust dst zone=Untrust action=Permit sent=${sent} rcvd=${rcvd} src=${ip} dst=${ip2} src_port=${port} dst_port=${port2} src-xlated ip=${ip} port=${port} dst-xlated ip=${ip2} port=${port2} session_id=7367 reason=Close - AGE OUT",
        "XYZ: NetScreen device_id=XYZ  [Root]system-notification-00257(traffic): start_time=\"${datetime}\" duration=${number} policy_id=320001 service=udp/port:${port} proto=17 src zone=Null dst zone=self action=Deny sent=${sent} rcvd=${rcvd} src=${ip} dst=${ip2} src_port=${port} dst_port=${port2} session_id=0",
        "XYZ: NetScreen device_id=XYZ [Root]system-notification-00257(traffic): start_time=\"${datetime}\" duration=${number} policy_id=107 service=icmp proto=1 src zone=Trust dst zone=Untrust action=Deny sent=${sent} rcvd=${rcvd} src=${ip} dst=${ip2} icmp type=8 session_id=0",
        "XYZ: NetScreen device_id=XYZ  [Root]system-notification-00257(traffic): start_time=\"${datetime}\" duration=${number} policy_id=48 service=icmp proto=1 src zone=DMZ dst zone=Untrust action=Deny sent=${sent} rcvd=${rcvd} src=${ip} dst=${ip2} icmp type=8 icmp code=0 session_id=0",
        "XYZ_SSG520: NetScreen device_id=XYZ_SSG520  [Root]system-notification-00257(traffic): start_time=\"${datetime}\" duration=${number} policy_id=74 service=Network Time proto=17 src zone=Trust dst zone=Untrust action=Permit sent=${sent} rcvd=${rcvd} src=${ip} dst=${ip2} src_port=${port} dst_port=${port2} src-xlated ip=${ip} port=${port} dst-xlated ip=${ip2} port=${port2} session_id=125472 reason=Creation"
     ]
}
