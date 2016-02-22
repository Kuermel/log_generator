{
    "fields" : [
        { "ipv4" : {"type": "random", "generate_type":"IPv4" } },
        { "src_ipv4" : {"type": "random", "generate_type":"LocalIPv4" } },
        { "dst_ipv4" : {"type": "random", "generate_type":"IPv4" } },
        { "local_dst_ipv4" : {"type": "random", "generate_type":"LocalIPv4" } },
        { "local_dstnat_ipv4" : {"type": "random", "generate_type":"LocalIPv4" } },
        { "srcnat_ipv4" : {"type": "random", "generate_type":"LocalIPv4" } },
        { "dstnat_ipv4" : {"type": "random", "generate_type":"IPv4" } },
        { "date": {"type": "random", "generate_type":"datetime", "format": "%d/%b/%Y:%H:%M:%S" } },
        { "es_date": {"type": "random", "generate_type":"datetime", "format": "%Y-%m-%d %H:%M:%S" } },
        { "url_path" : {"type": "from_list_file", "file" : "url_path.list", "method":"random" } },
        { "url_domain" : {"type": "from_list_file", "file" : "url_domain.list", "method":"random" } },
        { "url_scheme" : {"type": "from_list_file", "file" : "url_scheme.list", "method":"random" } },
        { "url_category" : {"type": "from_list_file", "file" : "url_category.list", "method":"random" } },
        { "application_name" : {"type": "from_list_file", "file" : "application_name.list", "method":"sequential" } },
        { "method" : {"type": "from_list_file", "file" : "method.list", "method":"random" } },
        { "session_id" : {"type": "from_list_file", "file" : "session_id.list", "method":"random" } },
        { "result_code" : {"type": "from_list_file", "file": "result_code.list", "method":"ratio", "ratio":"50,50" } },
        { "sent" : {"type": "random", "generate_type":"integer", "min":1, "max":10000 } },
        { "port" : {"type": "from_list_file", "file" : "port.list", "method":"random" } },
        { "srcnat_port" : {"type": "from_list_file", "file" : "srcnat_port.list", "method":"random" } },
        { "dstnat_port" : {"type": "from_list_file", "file" : "dstnat_port.list", "method":"random" } },
        { "dst_port" : {"type": "from_list_file", "file" : "dst_port.list", "method":"random" } },
        { "src_port" : {"type": "from_list_file", "file" : "src_port.list", "method":"random" } },
        { "username" : {"type": "from_list_file", "file" : "username.list", "method":"random" } },
        { "recv" : {"type": "random", "generate_type":"integer", "min":1, "max":10000 } },
        { "duration_time" : {"type": "random", "generate_type":"integer", "min":1, "max":1000 } },
        { "src_country" : {"type": "from_list_file", "file" : "src_country.list", "method":"random" } },
        { "dst_country" : {"type": "from_list_file", "file" : "dst_country.list", "method":"random" } },
        { "city" : {"type": "from_list_file", "file" : "city.list", "method":"random" } },
        { "severity_name" : {"type": "from_list_file", "file" : "severity_name.list", "method":"sequential" } },
        { "error_date": {"type": "random", "generate_type":"datetime", "format": "%a %b %d %H:%M:%S %Y" } }
    ],
    "template" : [],
    "json_template": [
             {
                 "_es_type": "nastedlog",
                 "Bytes": {
                     "Received": "recv",
                     "Sent": "sent"
                 },
                 "EventMap": {
                     "Type": "Session",
                     "SubType": "Allow",
                     "Context": "Network"
                 },
                 "EventSource": {
                     "Vendor": "Fortinet",
                     "Product": "FortiGate",
                     "IP": "192.168.1.152",
                     "ID": "FG800C3913802819",
                     "Name": "Master Firewall",
                     "PrefixID": 3024,
                     "Category": "Firewall",
                     "Type": "Security System",
                     "Description": "fortigate_fw",
                     "Collector": "syslog-udp"
                 },
                 "Event": {
                     "VendorID": 15,
                     "SystemID": 302400015,
                     "SubCategory": "forward",
                     "Category": "traffic",
                     "Status": "start"
                 },
                 "Source": {
                     "IP": "src_ipv4",
                     "City": "Unknown",
                     "Country": "src_country",
                     "Interface": "port5",
                     "Location": "Unknown",
                     "Port": "src_port",
                     "Position": "in",
                     "UserName": "username"
                 },
                 "Destination": {
                     "IP": "dst_ipv4",
                     "City": "Unknown",
                     "Country": "dst_country",
                     "Interface": "port6",
                     "NatIP": "dstnat_ipv4",
                     "NatISP": "dnat",
                     "NatPort": "dstnat_port",
                     "Location": "unknown",
                     "Port": "dst_port",
                     "Position": "out"
                 },
                 "Policy": {
                     "ID": 449
                 },
                 "Severity": {
                     "ID": 5,
                     "Name": "notice"
                 },
                 "Protocol": {
                     "ID": 6
                 },
                 "Session": {
                     "ID": "session_id"
                 },
                 "Time": {
                     "Generated": "es_date",
                     "Received": "es_date",
                     "Duration": "duration_time"
                 }
             },
             {
                  "_es_type": "nastedlog",
                  "Bytes": {
                      "Received": "recv",
                      "Sent": "sent"
                  },
                  "EventMap": {
                      "Type": "Session",
                      "SubType": "Allow",
                      "Context": "Network"
                  },
                  "EventSource": {
                      "Vendor": "Fortinet",
                      "Product": "FortiGate",
                      "IP": "192.168.1.152",
                      "ID": "FG800C3913802819",
                      "Name": "Master Firewall",
                      "PrefixID": 3024,
                      "Category": "Firewall",
                      "Type": "Security System",
                      "Description": "fortigate_fw",
                      "Collector": "syslog-udp"
                  },
                  "Event": {
                      "VendorID": 13,
                      "SystemID": 302400015,
                      "SubCategory": "forward",
                      "Category": "traffic",
                      "Action": "allow"
                  },
                  "Source": {
                      "IP": "ipv4",
                      "City": "Unknown",
                      "Country": "src_country",
                      "Interface": "port5",
                      "Location": "Unknown",
                      "Port": "src_port",
                      "Position": "out"
                  },
                  "Destination": {
                      "IP": "local_dst_ipv4",
                      "City": "Unknown",
                      "Country": "dst_country",
                      "Interface": "port6",
                      "NatIP": "dstnat_ipv4",
                      "NatISP": "dnat",
                      "Location": "unknown",
                      "Port": "dst_port",
                      "Position": "in"
                  },
                  "Policy": {
                      "ID": 449
                  },
                  "Severity": {
                      "ID": 5,
                      "Name": "notice"
                  },
                  "Service": {
                      "Name": "DNS_UDP"
                  },
                  "Protocol": {
                      "ID": 6
                  },
                  "Session": {
                      "ID": "session_id"
                  },
                  "Time": {
                      "Generated": "es_date",
                      "Received": "es_date",
                      "Duration": "duration_time"
                  }
             },
             {
                 "_es_type": "nastedlog",
                 "Bytes": {
                     "Received": "0",
                     "Sent": "0"
                 },
                 "EventMap": {
                     "Type": "Session",
                     "SubType": "Deny",
                     "Context": "Network"
                 },
                 "EventSource": {
                     "Vendor": "Fortinet",
                     "Product": "FortiGate",
                     "IP": "192.168.1.152",
                     "ID": "FG800C3913802819",
                     "Name": "Master Firewall",
                     "PrefixID": 3024,
                     "Category": "Firewall",
                     "Type": "Security System",
                     "Description": "fortigate_fw",
                     "Collector": "syslog-udp"
                 },
                 "Event": {
                     "VendorID": 13,
                     "SystemID": 302400013,
                     "SubCategory": "forward",
                     "Category": "traffic",
                     "Action": "deny"
                 },
                 "Source": {
                     "IP": "ipv4",
                     "City": "Unknown",
                     "Country": "src_country",
                     "Interface": "LAN",
                     "Location": "Unknown",
                     "Port": "src_port",
                     "Position": "out"
                 },
                 "Destination": {
                     "IP": "local_dst_ipv4",
                     "City": "Unknown",
                     "Country": "dst_country",
                     "Interface": "port6",
                     "NatIP": "local_dstnat_ipv4",
                     "NatISP": "dnat",
                     "Port": "dst_port",
                     "Position": "out"
                 },
                 "Policy": {
                     "ID": 296
                 },
                 "Packets": {
                     "Sent": 1
                 },
                 "Severity": {
                     "ID": 5,
                     "Name": "notice"
                 },
                 "Protocol": {
                     "ID": 6
                 },
                 "Session": {
                     "ID": "session_id"
                 },
                 "Time": {
                     "Generated": "es_date",
                     "Received": "es_date",
                     "Duration": "duration_time"
                 }
             },
             {
                 "_es_type": "nastedlog",
                 "Bytes": {
                     "Received": "recv",
                     "Sent": "sent"
                 },
                 "EventMap": {
                     "Type": "URL",
                     "SubType": "Allow",
                     "Context": "Security"
                 },
                 "EventSource": {
                     "Vendor": "Fortinet",
                     "Product": "FortiGate",
                     "IP": "192.168.1.152",
                     "ID": "FG800C3913802819",
                     "Name": "Master Firewall",
                     "PrefixID": 3024,
                     "Category": "Firewall",
                     "Type": "Security System",
                     "Description": "fortigate_fw",
                     "Collector": "syslog-udp"
                 },
                 "Event": {
                     "VendorID": 302413312,
                     "SystemID": 13312,
                     "Info": "URL belongs to an allowed category in policy",
                     "Status": "passthrough",
                     "Method": "domain",
                     "SubCategory": "webfilter",
                     "Category": "utm"
                 },
                 "Source": {
                     "IP": "src_ipv4",
                     "City": "Unknown",
                     "Interface": "LAN",
                     "Location": "Unknown",
                     "Port": "src_port",
                     "Position": "in"
                 },
                 "Destination": {
                     "IP": "dst_ipv4",
                     "City": "city",
                     "Interface": "port7",
                     "Location": "Unknown",
                     "NatIP": "dstipv4",
                     "Port": "dst_port",
                     "Position": "out"
                 },
                 "URL": {
                     "Domain": "url_domain",
                     "Path": "url_path",
                     "Scheme": "url_scheme",
                     "RequestType": "direct"
                 },
                 "Severity": {
                     "ID": 5,
                     "Name": "notice"
                 },
                 "Protocol": {
                     "Name": "tcp"
                 },
                 "Profile": {
                     "Name": "Staff_General"
                 },
                 "Session": {
                     "ID": "session_id"
                 },
                 "Policy": {
                     "ID": 2559
                 },
                 "Time": {
                     "Generated": "es_date",
                     "Received": "es_date"
                 }
             },
             {
                  "_es_type": "nastedlog",
                  "Bytes": {
                      "Received": "recv",
                      "Sent": "sent"
                  },
                  "EventMap": {
                      "Type": "URL",
                      "SubType": "Allow",
                      "Context": "Security"
                  },
                  "EventSource": {
                      "Vendor": "Fortinet",
                      "Product": "FortiGate",
                      "IP": "192.168.1.152",
                      "ID": "FG800C3913802819",
                      "Name": "Master Firewall",
                      "PrefixID": 3024,
                      "Category": "Firewall",
                      "Type": "Security System",
                      "Description": "fortigate_fw",
                      "Collector": "syslog-udp"
                  },
                  "Event": {
                      "VendorID": 302413312,
                      "SystemID": 13312,
                      "Info": "URL belongs to an allowed category in policy",
                      "Status": "passthrough",
                      "Method": "domain",
                      "SubCategory": "webfilter",
                      "Category": "utm"
                  },
                  "Source": {
                      "IP": "src_ipv4",
                      "City": "Unknown",
                      "Interface": "LAN",
                      "Location": "Unknown",
                      "Port": "src_port",
                      "Position": "in"
                  },
                  "Destination": {
                      "IP": "dst_ipv4",
                      "City": "city",
                      "Interface": "port7",
                      "Location": "Unknown",
                      "NatIP": "dstipv4",
                      "Port": "dst_port",
                      "Position": "out"
                  },
                  "URL": {
                      "Domain": "url_domain",
                      "Path": "url_path",
                      "Scheme": "url_scheme",
                      "RequestType": "referral"
                  },
                  "Severity": {
                      "ID": 5,
                      "Name": "notice"
                  },
                  "Protocol": {
                      "Name": "tcp"
                  },
                  "Profile": {
                      "Name": "Staff_General"
                  },
                  "Session": {
                      "ID": "session_id"
                  },
                  "Policy": {
                      "ID": 2559
                  },
                  "Time": {
                      "Generated": "es_date",
                      "Received": "es_date"
                  }
             },
             {
                 "_es_type": "nastedlog",
                 "Bytes": {
                     "Received": 0,
                     "Sent": "sent"
                 },
                 "EventMap": {
                     "Type": "URL",
                     "SubType": "Block",
                     "Context": "Security"
                 },
                 "EventSource": {
                     "Vendor": "Fortinet",
                     "Product": "FortiGate",
                     "IP": "192.168.1.152",
                     "ID": "FG800C3913802819",
                     "Name": "Master Firewall",
                     "PrefixID": 3024,
                     "Category": "Firewall",
                     "Type": "Security System",
                     "Description": "fortigate_fw",
                     "Collector": "syslog-udp"
                 },
                 "Event": {
                     "VendorID": 12544,
                     "SystemID": 30212544,
                     "Info": "URL was blocked because it is in the URL filter list",
                     "SubCategory": "webfilter",
                     "Status": "blocked",
                     "Category": "utm"
                 },
                 "Source": {
                     "IP": "src_ipv4",
                     "City": "Unknown",
                     "Interface": "LAN",
                     "Location": "Unknown",
                     "Port": "src_port",
                     "Position": "in"
                 },
                 "Destination": {
                     "IP": "dst_ipv4",
                     "City": "city",
                     "Interface": "port8",
                     "Location": "Unknown",
                     "NatIP": "dst_ipv4",
                     "Port": "dst_port",
                     "Position": "out"
                 },
                 "URL": {
                     "Domain": "url_domain",
                     "Path": "url_path",
                     "Scheme": "url_scheme",
                     "RequestType": "direct"
                 },
                 "Severity": {
                     "ID": 4,
                     "Name": "warning"
                 },
                 "Protocol": {
                     "Name": "tcp"
                 },
                 "Profile": {
                     "Name": "Staff_General"
                 },
                 "Session": {
                     "ID": "session_id"
                 },
                 "Policy": {
                     "ID": 2559
                 },
                 "Time": {
                     "Generated": "es_date",
                     "Received": "es_date"
                 }
             },
             {
                  "_es_type": "nastedlog",
                  "Bytes": {
                      "Received": 0,
                      "Sent": "sent"
                  },
                  "EventMap": {
                      "Type": "URL",
                      "SubType": "Block",
                      "Context": "Security"
                  },
                  "EventSource": {
                      "Vendor": "Fortinet",
                      "Product": "FortiGate",
                      "IP": "192.168.1.152",
                      "ID": "FG800C3913802819",
                      "Name": "Master Firewall",
                      "PrefixID": 3024,
                      "Category": "Firewall",
                      "Type": "Security System",
                      "Description": "fortigate_fw",
                      "Collector": "syslog-udp"
                  },
                  "Event": {
                      "VendorID": 12544,
                      "SystemID": 30212544,
                      "Info": "URL was blocked because it is in the URL filter list",
                      "SubCategory": "webfilter",
                      "Status": "blocked",
                      "Category": "utm"
                  },
                  "Source": {
                      "IP": "src_ipv4",
                      "City": "Unknown",
                      "Interface": "LAN",
                      "Location": "Unknown",
                      "Port": "src_port",
                      "Position": "in"
                  },
                  "Destination": {
                      "IP": "dst_ipv4",
                      "City": "city",
                      "Interface": "port8",
                      "Location": "Unknown",
                      "NatIP": "dst_ipv4",
                      "Port": "dst_port",
                      "Position": "out"
                  },
                  "URL": {
                      "Domain": "url_domain",
                      "Path": "url_path",
                      "Scheme": "url_scheme",
                      "RequestType": "referral"
                  },
                  "Severity": {
                      "ID": 4,
                      "Name": "warning"
                  },
                  "Protocol": {
                      "Name": "tcp"
                  },
                  "Profile": {
                      "Name": "Staff_General"
                  },
                  "Session": {
                      "ID": "session_id"
                  },
                  "Policy": {
                      "ID": 2559
                  },
                  "Time": {
                      "Generated": "es_date",
                      "Received": "es_date"
                  }
             },
             {
                  "_es_type": "nastedlog",
                  "Bytes": {
                      "Received": "recv",
                      "Sent": "sent"
                  },
                  "EventMap": {
                      "Type": "URL",
                      "SubType": "Block",
                      "Context": "Security"
                  },
                  "EventSource": {
                      "Vendor": "Fortinet",
                      "Product": "FortiGate",
                      "IP": "192.168.1.152",
                      "ID": "FG800C3913802819",
                      "Name": "Master Firewall",
                      "PrefixID": 3024,
                      "Category": "Firewall",
                      "Type": "Security System",
                      "Description": "fortigate_fw",
                      "Collector": "syslog-udp"
                  },
                  "Event": {
                      "VendorID": 13056,
                      "SystemID": 302413056,
                      "Info": "URL belongs to a denied category in policy",
                      "Method": "Domain",
                      "SubCategory": "webfilter",
                      "Action": "blocked",
                      "Category": "utm"
                  },
                  "Source": {
                      "IP": "src_ipv4",
                      "City": "Unknown",
                      "Interface": "port11",
                      "Location": "Unknown",
                      "Port": "src_port",
                      "Position": "in"
                  },
                  "Destination": {
                      "IP": "dst_ipv4",
                      "City": "city",
                      "Interface": "port8",
                      "Location": "Unknown",
                      "NatIP": "dst_ipv4",
                      "Port": "dst_port",
                      "Position": "out"
                  },
                  "URL": {
                      "Domain": "url_domain",
                      "Path": "url_path",
                      "Scheme": "url_scheme",
                      "RequestType": "direct"
                  },
                  "Severity": {
                      "ID": 4,
                      "Name": "warning"
                  },
                  "Protocol": {
                      "Name": "tcp"
                  },
                  "Profile": {
                      "Name": "Temporary_Guests"
                  },
                  "Session": {
                      "ID": "session_id"
                  },
                  "Policy": {
                      "ID": 2559
                  },
                  "Time": {
                      "Generated": "es_date",
                      "Received": "es_date"
                  }
             },
             {
                   "_es_type": "nastedlog",
                   "Bytes": {
                       "Received": "recv",
                       "Sent": "sent"
                   },
                   "EventMap": {
                       "Type": "URL",
                       "SubType": "Block",
                       "Context": "Security"
                   },
                   "EventSource": {
                       "Vendor": "Fortinet",
                       "Product": "FortiGate",
                       "IP": "192.168.1.152",
                       "ID": "FG800C3913802819",
                       "Name": "Master Firewall",
                       "PrefixID": 3024,
                       "Category": "Firewall",
                       "Type": "Security System",
                       "Description": "fortigate_fw",
                       "Collector": "syslog-udp"
                   },
                   "Event": {
                       "VendorID": 13056,
                       "SystemID": 302413056,
                       "Info": "URL belongs to a denied category in policy",
                       "Method": "Domain",
                       "SubCategory": "webfilter",
                       "Action": "blocked",
                       "Category": "utm"
                   },
                   "Source": {
                       "IP": "src_ipv4",
                       "City": "Unknown",
                       "Interface": "port11",
                       "Location": "Unknown",
                       "Port": "src_port",
                       "Position": "in"
                   },
                   "Destination": {
                       "IP": "dst_ipv4",
                       "City": "city",
                       "Interface": "port8",
                       "Location": "Unknown",
                       "NatIP": "dst_ipv4",
                       "Port": "dst_port",
                       "Position": "out"
                   },
                   "URL": {
                       "Domain": "url_domain",
                       "Path": "url_path",
                       "Scheme": "url_scheme",
                       "RequestType": "referral"
                   },
                   "Severity": {
                       "ID": 4,
                       "Name": "warning"
                   },
                   "Protocol": {
                       "Name": "tcp"
                   },
                   "Profile": {
                       "Name": "Temporary_Guests"
                   },
                   "Session": {
                       "ID": "session_id"
                   },
                   "Policy": {
                       "ID": 2559
                   },
                   "Time": {
                       "Generated": "es_date",
                       "Received": "es_date"
                   }
             },
             {
                 "_es_type": "nastedlog",
                 "EventMap": {
                     "Type": "Virus",
                     "SubType": "Block",
                     "Context": "Security"
                 },
                 "EventSource": {
                     "Vendor": "Fortinet",
                     "Product": "FortiGate",
                     "IP": "192.168.1.152",
                     "ID": "FG800C3913802819",
                     "Name": "Security Guard",
                     "PrefixID": 3024,
                     "Category": "Firewall",
                     "Type": "Security System",
                     "Description": "fortigate_fw"
                 },
                 "Event": {
                     "VendorID": 8704,
                     "SystemID": 302408704,
                     "Info": "Size limit is exceeded.",
                     "SubCategory": "virus",
                     "Category": "utm",
                     "Action": "blocked"
                 },
                 "Source": {
                     "IP": "src_ipv4",
                     "City": "Unknown",
                     "Interface": "port1",
                     "Location": "Unknown",
                     "Port": "src_port",
                     "Position": "in",
                     "Group": "Internet Access Standart",
                     "UserName": "username"
                 },
                 "Destination": {
                     "IP": "dst_ipv4",
                     "City": "Unknown",
                     "Interface": "port2",
                     "NatIP": "dstnat_ipv4",
                     "Location": "Unknown",
                     "Port": "dst_port",
                     "Position": "out"
                 },
                 "URL": {
                     "Domain": "url_domain",
                     "Path": "url_path",
                     "Scheme": "url_scheme"
                 },
                 "Severity": {
                     "ID": 4,
                     "Name": "warning"
                 },
                 "Protocol": {
                     "ID": 6
                 },
                 "Session": {
                     "Direction": "incoming",
                     "ID": "session_id"
                 },
                 "Policy": {
                     "ID": 89
                 },
                 "Profile": {
                     "Name": "Standard Users Max 20 MB Download"
                 },
                 "Time": {
                     "Generated": "es_date",
                     "Received": "es_date"
                 }
             },
             {
                 "_es_type": "nastedlog",
                 "EventMap": {
                     "Type": "Virus",
                     "SubType": "Info",
                     "Context": "Security"
                 },
                 "EventSource": {
                     "Vendor": "Fortinet",
                     "Product": "FortiGate",
                     "IP": "192.168.1.152",
                     "ID": "FG800C3913802819",
                     "Name": "Security Guard",
                     "PrefixID": 3024,
                     "Category": "Firewall",
                     "Type": "Security System",
                     "Description": "fortigate_fw"
                 },
                 "Event": {
                     "VendorID": 8192,
                     "SystemID": 302408192,
                     "Info": "File is infected.",
                     "SubCategory": "virus",
                     "Category": "utm",
                     "Action": "blocked",
                     "DetectionType": "Virus"
                 },
                 "Source": {
                     "IP": "ipv4",
                     "City": "Unknown",
                     "Interface": "port2",
                     "Location": "Unknown",
                     "Port": "src_port",
                     "Position": "out"
                 },
                 "Destination": {
                     "IP": "local_dst_ipv4",
                     "City": "Unknown",
                     "Interface": "port1",
                     "NatIP": "dstnat_ipv4",
                     "Location": "Unknown",
                     "Port": "dst_port",
                     "Position": "in"
                 },
                 "URL": {
                     "Domain": "url_domain",
                     "Path": "url_path",
                     "Scheme": "url_scheme"
                 },
                 "Virus": {
                     "DType": "Virus",
                     "Name": "WM/Moat.59A54E96!tr",
                     "Reference": "http://www.fortinet.com/ve?vn=WM%2FMoat.59A54E96%21tr"
                 },
                 "Severity": {
                     "ID": 4,
                     "Name": "warning"
                 },
                 "Protocol": {
                     "ID": 6
                 },
                 "Session": {
                     "Direction": "outgoing",
                     "ID": "session_id"
                 },
                 "Service": {
                     "Name": "SMTP"
                 },
                 "Policy": {
                     "ID": 2
                 },
                 "Profile": {
                     "Name": "EmailScan"
                 },
                 "Time": {
                     "Generated": "es_date",
                     "Received": "es_date"
                 }
             },
             {
                 "_es_type": "nastedlog",
                 "EventMap": {
                     "Type": "Attack",
                     "SubType": "Block",
                     "Context": "Security"
                 },
                 "EventSource": {
                     "Vendor": "Fortinet",
                     "Product": "FortiGate",
                     "IP": "192.168.1.152",
                     "ID": "FG800C3913802819",
                     "Name": "Security Guard",
                     "PrefixID": 3024,
                     "Category": "Firewall",
                     "Type": "Security System",
                     "Description": "fortigate_fw"
                 },
                 "Event": {
                     "VendorID": 28705,
                     "SystemID": 302428705,
                     "Info": "Social.Media: Facebook",
                     "SubCategory": "app-ctrl",
                     "Category": "utm",
                     "Action": "block"
                 },
                 "Source": {
                     "IP": "src_ipv4",
                     "City": "Unknown",
                     "Interface": "port1",
                     "Location": "Unknown",
                     "Group": "Basic User",
                     "Port": "src_port",
                     "Position": "out"
                 },
                 "Destination": {
                     "IP": "local_dst_ipv4",
                     "City": "Unknown",
                     "Interface": "port1",
                     "NatIP": "dstnat_ipv4",
                     "Location": "Unknown",
                     "Port": "dst_port",
                     "Position": "out"
                 },
                 "Application": {
                     "Category": "Social.Media",
                     "ID": 15832,
                     "List": "Basic Profile",
                     "Name": "Facebook"
                 },
                 "URL": {
                     "Domain": "url_domain",
                     "Path": "url_path",
                     "Scheme": "url_scheme"
                 },
                 "Severity": {
                     "ID": 4,
                     "Name": "warning"
                 },
                 "Protocol": {
                     "ID": 6
                 },
                 "Session": {
                     "ID": "session_id"
                 },
                 "Policy": {
                     "ID": 72
                 },
                 "Time": {
                     "Generated": "es_date",
                     "Received": "es_date"
                 }
             },
             {
                 "_es_type": "nastedlog",
                 "EventMap": {
                     "Type": "User",
                     "SubType": "Login",
                     "Context": "VPN"
                 },
                 "EventSource": {
                     "Vendor": "Fortinet",
                     "Product": "FortiGate",
                     "IP": "192.168.1.152",
                     "ID": "FG800C3913802819",
                     "Name": "Security Guard",
                     "PrefixID": 3024,
                     "Category": "Firewall",
                     "Type": "Security System",
                     "Description": "fortigate_fw"
                 },
                 "Source": {
                     "Group": "SSLVPN_Authorized",
                     "UserName": "username"
                 },
                 "Destination": {
                     "IP": "dst_ipv4",
                     "City": "Unknown",
                     "Country": "country",
                     "HostName": "N/A",
                     "NatIP": "dstnat_ipv4",
                     "Location": "Unknown",
                     "Position": "out"
                 },
                 "Event": {
                     "VendorID": 39424,
                     "SystemID": 302439424,
                     "Info": "SSL",
                     "Reason": "login successfully",
                     "SubCategory": "vpn",
                     "Category": "event",
                     "Action": "tunnel-up"
                 },
                 "Protocol": {
                     "Name": "tcp"
                 },
                 "Severity": {
                     "ID": 6,
                     "Name": "information"
                 },
                 "Time": {
                     "Generated": "es_date",
                     "Received": "es_date"
                 }
             },
             {
                 "_es_type": "nastedlog",
                 "EventMap": {
                     "Type": "User",
                     "SubType": "Deny",
                     "Context": "VPN"
                 },
                 "EventSource": {
                     "Vendor": "Fortinet",
                     "Product": "FortiGate",
                     "IP": "192.168.1.152",
                     "ID": "FG800C3913802819",
                     "Name": "Security Guard",
                     "PrefixID": 3024,
                     "Category": "Firewall",
                     "Type": "Security System",
                     "Description": "fortigate_fw"
                 },
                 "Source": {
                     "Group": "N/A",
                     "UserName": "username"
                 },
                 "Destination": {
                     "IP": "dst_ipv4",
                     "City": "Unknown",
                     "Country": "country",
                     "HostName": "N/A",
                     "NatIP": "dstnat_ipv4",
                     "Position": "out"
                 },
                 "Event": {
                     "VendorID": 39426,
                     "SystemID": 302439426,
                     "Info": "SSL user failed to logged in",
                     "Reason": "sslvpn_login_unknown_user",
                     "SubCategory": "vpn",
                     "Category": "event",
                     "Action": "ssl-login-fail"
                 },
                 "Protocol": {
                     "Name": "tcp"
                 },
                 "Severity": {
                     "ID": 1,
                     "Name": "alert"
                 },
                 "Time": {
                     "Generated": "es_date",
                     "Received": "es_date"
                 }
             },
             {
                 "_es_type": "nastedlog",
                 "Bytes": {
                     "Received": "recv",
                     "Sent": "sent"
                 },
                 "EventMap": {
                     "Type": "User",
                     "SubType": "Logout",
                     "Context": "VPN"
                 },
                 "EventSource": {
                     "Vendor": "Fortinet",
                     "Product": "FortiGate",
                     "IP": "192.168.1.152",
                     "ID": "FG800C3913802819",
                     "Name": "Security Guard",
                     "PrefixID": 3024,
                     "Category": "Firewall",
                     "Type": "Security System",
                     "Description": "fortigate_fw"
                 },
                 "Source": {
                     "Group": "SSLVPN_Authorized",
                     "UserName": "username"
                 },
                 "Destination": {
                     "IP": "dst_ipv4",
                     "City": "Unknown",
                     "Country": "country",
                     "HostName": "N/A",
                     "NatIP": "dstnat_ipv4",
                     "Position": "out"
                 },
                 "Event": {
                     "VendorID": 39948,
                     "SystemID": 302439948,
                     "Info": "SSL tunnel shutdown",
                     "Reason": "N/A",
                     "SubCategory": "vpn",
                     "Category": "event",
                     "Action": "tunnel-down"
                 },
                 "Protocol": {
                     "Name": "tcp"
                 },
                 "Severity": {
                     "ID": 6,
                     "Name": "information"
                 },
                 "Time": {
                     "Generated": "es_date",
                     "Received": "es_date",
                     "Duration": "duration_time"
                 }
             },
             {
                 "_es_type": "nastedlog",
                 "EventMap": {
                     "Type": "User",
                     "SubType": "Login",
                     "Context": "Identity"
                 },
                 "EventSource": {
                     "Vendor": "Fortinet",
                     "Product": "FortiGate",
                     "IP": "192.168.1.152",
                     "ID": "FG800C3913802819",
                     "Name": "Security Guard",
                     "PrefixID": 3024,
                     "Category": "Firewall",
                     "Type": "Security System",
                     "Description": "fortigate_fw"
                 },
                 "Source": {
                     "City": "Unknown",
                     "IP": "src_ipv4",
                     "Location": "Unknown",
                     "UserName": "username",
                     "Position": "in"
                 },
                 "Event": {
                     "VendorID": 43014,
                     "SystemID": 302443014,
                     "Info": "FSSO-logon",
                     "SubCategory": "user",
                     "Category": "event",
                     "Action": "FSSO-logon"
                 },
                 "Protocol": {
                     "Name": "tcp"
                 },
                 "Severity": {
                     "ID": 5,
                     "Name": "notice"
                 },
                 "Time": {
                     "Generated": "es_date",
                     "Received": "es_date"
                 }
             },
             {
                 "_es_type": "nastedlog",
                 "EventMap": {
                     "Type": "User",
                     "SubType": "Logout",
                     "Context": "Identity"
                 },
                 "EventSource": {
                     "Vendor": "Fortinet",
                     "Product": "FortiGate",
                     "IP": "192.168.1.152",
                     "ID": "FG800C3913802819",
                     "Name": "Security Guard",
                     "PrefixID": 3024,
                     "Category": "Firewall",
                     "Type": "Security System",
                     "Description": "fortigate_fw"
                 },
                 "Source": {
                     "City": "Unknown",
                     "IP": "src_ipv4",
                     "Location": "Unknown",
                     "UserName": "username",
                     "Position": "out"
                 },
                 "Event": {
                     "VendorID": 43015,
                     "SystemID": 302443015,
                     "Info": "FSSO-logoff",
                     "SubCategory": "user",
                     "Category": "event",
                     "Action": "FSSO-logoff"
                 },
                 "Protocol": {
                     "Name": "tcp"
                 },
                 "Severity": {
                     "ID": 5,
                     "Name": "notice"
                 },
                 "Time": {
                     "Generated": "es_date",
                     "Received": "es_date"
                 }
             }
    ]
}
