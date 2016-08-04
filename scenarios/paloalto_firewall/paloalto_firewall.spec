{
    "fields" : [
        { "ipv4" : {"type": "random", "generate_type":"IPv4" } },
        { "src_ipv4" : {"type": "random", "generate_type":"LocalIPv4" } },
        { "dst_ipv4" : {"type": "random", "generate_type":"IPv4" } },
        { "local_dst_ipv4" : {"type": "random", "generate_type":"LocalIPv4" } },
        { "srcnat_ipv4" : {"type": "random", "generate_type":"LocalIPv4" } },
        { "dstnat_ipv4" : {"type": "random", "generate_type":"IPv4" } },
        { "date": {"type": "random", "generate_type":"datetime", "format": "%d/%b/%Y:%H:%M:%S" } },
        { "es_date": {"type": "random", "generate_type":"datetime", "format": "%Y-%m-%d %H:%M:%S" } },
        { "url_path" : {"type": "from_list_file", "file" : "url_path.list", "method":"random" } },
        { "url_domain" : {"type": "from_list_file", "file" : "url_domain.list", "method":"random" } },
        { "url_category" : {"type": "from_list_file", "file" : "url_category.list", "method":"random" } },
        { "application_name" : {"type": "from_list_file", "file" : "application_name.list", "method":"sequential" } },
        { "method" : {"type": "from_list_file", "file" : "method.list", "method":"random" } },
        { "port" : {"type": "from_list_file", "file" : "port.list", "method":"random" } },
        { "src_port" : {"type": "from_list_file", "file" : "src_port.list", "method":"random" } },
        { "dst_port" : {"type": "from_list_file", "file" : "dst_port.list", "method":"random" } },
        { "srcnat_port" : {"type": "from_list_file", "file" : "srcnat_port.list", "method":"random" } },
        { "dstnat_port" : {"type": "from_list_file", "file" : "dstnat_port.list", "method":"random" } },
        { "session_id" : {"type": "from_list_file", "file" : "session_id.list", "method":"random" } },
        { "result_code" : {"type": "from_list_file", "file": "result_code.list", "method":"ratio", "ratio":"50,50" } },
        { "total" : {"type": "random", "generate_type":"integer", "min":1100, "max":100000 } },
        { "tot" : {"type": "random", "generate_type":"integer", "min":1, "max":100 } },
        { "src_country" : {"type": "from_list_file", "file" : "src_country.list", "method":"random" } },
        { "dst_country" : {"type": "from_list_file", "file" : "dst_country.list", "method":"random" } },
        { "username" : {"type": "from_list_file", "file" : "username.list", "method":"random" } },
        { "severity_name" : {"type": "from_list_file", "file" : "severity_name.list", "method":"sequential" } },
        { "error_date": {"type": "random", "generate_type":"datetime", "format": "%a %b %d %H:%M:%S %Y" } }
    ],
    "template" : [],
    "json_template": [
        {
            "_es_type": "nastedlog",
            "DataType": "log",
            "Bytes": {
                "Total": "total"
            },
            "EventMap": {
                "Type": "Session",
                "SubType": "Allow",
                "Context": "Network"
            },
            "EventSource": {
                "Vendor": "PaloAlto",
                "IP": "192.168.1.151",
                "PrefixID": 3029,
                "Category": "Firewall",
                "Type": "Security System",
                "Description": "palo_alto_fw",
                "Tag": "palo_alto",
                "Serial": "0011C100469",
                "Collector": "syslog-udp"
            },
            "Event": {
                "VendorID": 2,
                "SystemID": 30292,
                "Info": "end incomplete traffic allow",
                "SubCategory": "end",
                "Category": "TRAFFIC",
                "Action": "allow"
            },
            "Source": {
                "IP": "src_ipv4",
                "UserName": "username",
                "City": "Unknown",
                "Country": "src_country",
                "Interface": "ethernet1/4.1",
                "Location": "location",
                "Port": "src_port",
                "Position": "in",
                "Zone": "trust"
            },
            "Destination": {
                "IP": "local_dst_ipv4",
                "City": "Unknown",
                "Country": "dst_country",
                "Interface": "ethernet1/4.1",
                "Location": "unknown",
                "Port": "dst_port",
                "Position": "out",
                "Zone": "untrust"
            },
            "URL": {
                "Category": "any"

            },
            "Application": {
                "Name": "incomplete"
            },
            "Severity": {
                "ID": 5,
                "Name": "notice"
            },
            "Packets": {
                "Total": "tot"
            },
            "Protocol": {
                "Name": "tcp"
            },
            "Session": {
                "ID": "session_id"
            },
            "Rule": {
                "Name": "rule1"
            },
            "Time": {
                "Generated": "es_date",
                "Received": "es_date"
            }
        },
        {
            "_es_type": "nastedlog",
            "DataType": "log",
            "Bytes": {
                "Total": "total"
            },
            "EventMap": {
                "Type": "Session",
                "SubType": "Allow",
                "Context": "Network"
            },
            "EventSource": {
                "Vendor": "PaloAlto",
                "IP": "192.168.1.151",
                "PrefixID": 3029,
                "Category": "Firewall",
                "Type": "Security System",
                "Description": "palo_alto_fw",
                "Tag": "palo_alto",
                "Serial": "0011C100469",
                "Collector": "syslog-udp"
            },
            "Event": {
                "VendorID": 2,
                "SystemID": 30292,
                "Info": "end dns traffic allow",
                "SubCategory": "end",
                "Category": "TRAFFIC",
                "Action": "allow"
            },
            "Source": {
                "IP": "ipv4",
                "UserName": "username",
                "City": "Unknown",
                "Country": "src_country",
                "Interface": "ethernet1/4.1",
                "Location": "location",
                "Port": "src_port",
                "Position": "out",
                "Zone": "untrust"
            },
            "Destination": {
                "IP": "local_dst_ipv4",
                "City": "Unknown",
                "Country": "dst_country",
                "Interface": "ethernet1/4.1",
                "Location": "unknown",
                "Port": "dst_port",
                "Position": "in",
                "Zone": "trust"
            },
            "URL": {
                "Category": "any"

            },
            "Application": {
                "Name": "dns"
            },
            "Severity": {
                "ID": 5,
                "Name": "notice"
            },
            "Packets": {
                "Total": "tot"
            },
            "Protocol": {
                "Name": "udp"
            },
            "Session": {
                "ID": "session_id"
            },
            "Rule": {
                "Name": "DNS Request"
            },
            "Time": {
                "Generated": "es_date",
                "Received": "es_date"
            }
        },
        {
            "_es_type": "nastedlog",
            "DataType": "log",
            "Bytes": {
                "Total": "total"
            },
            "EventMap": {
                "Type": "Session",
                "SubType": "Deny",
                "Context": "Network"
            },
            "EventSource": {
                "Vendor": "PaloAlto",
                "IP": "192.168.1.151",
                "PrefixID": 3029,
                "Category": "Firewall",
                "Type": "Security System",
                "Description": "palo_alto_fw",
                "Tag": "palo_alto",
                "Serial": "0011C100469",
                "Collector": "syslog-udp"
            },
            "Event": {
                "VendorID": 8,
                "SystemID": 30298,
                "Info": "deny dns traffic deny",
                "SubCategory": "deny",
                "Category": "TRAFFIC",
                "Action": "deny"
            },
            "Source": {
                "IP": "ipv4",
                "UserName": "username",
                "City": "Unknown",
                "Country": "src_country",
                "Interface": "ethernet1/4.1",
                "Location": "location",
                "Port": "src_port",
                "Position": "out",
                "Zone": "untrust"
            },
            "Destination": {
                "IP": "local_dst_ipv4",
                "City": "Unknown",
                "Country": "dst_country",
                "Interface": "ethernet1/4.1",
                "Location": "location",
                "Port": "dst_port",
                "Position": "out",
                "Zone": "trust"
            },
            "URL": {
                "Category": "any"
            },
            "Application": {
                "Name": "dns"
            },
            "Severity": {
                "ID": 4,
                "Name": "warning"
            },
            "Packets": {
                "Total": "tot"
            },
            "Session": {
                "ID": "session_id"
            },
            "Protocol": {
                "Name": "udp"
            },
            "Rule": {
                "Name": "rule2"
            },
            "Time": {
                "Generated": "es_date",
                "Received": "es_date"
            }
        },
        {
            "_es_type": "nastedlog",
            "DataType": "log",
            "Bytes": {
                "Total": "total"
            },
            "EventMap": {
                "Type": "Session",
                "SubType": "Deny",
                "Context": "Network"
            },
            "EventSource": {
                "Vendor": "PaloAlto",
                "IP": "192.168.1.151",
                "PrefixID": 3029,
                "Category": "Firewall",
                "Type": "Security System",
                "Description": "palo_alto_fw",
                "Tag": "palo_alto",
                "Serial": "0011C100469",
                "Collector": "syslog-udp"
            },
            "Event": {
                "VendorID": 7,
                "SystemID": 30298,
                "Info": "drop not-applicable traffic deny",
                "SubCategory": "deny",
                "Category": "TRAFFIC",
                "Action": "deny"
            },
            "Source": {
                "IP": "src_ipv4",
                "UserName": "username",
                "City": "Unknown",
                "Country": "src_country",
                "Interface": "ethernet1/4.1",
                "Location": "location",
                "Port": "src_port",
                "Position": "in",
                "Zone": "trust"
            },
            "Destination": {
                "IP": "dst_ipv4",
                "City": "Unknown",
                "Country": "dst_country",
                "Interface": "ethernet1/4.1",
                "Location": "location",
                "Port": "dst_port",
                "Position": "out",
                "Zone": "untrust"
            },
            "URL": {
                "Category": "any"
            },
            "Application": {
                "Name": "not-applicable"
            },
            "Severity": {
                "ID": 4,
                "Name": "warning"
            },
            "Protocol": {
                "Name": "tcp"
            },
            "Packets": {
                "Total": "tot"
            },
            "Session": {
                "ID": "session_id"
            },
            "Rule": {
                "Name": "rule2"
            },
            "Time": {
                "Generated": "es_date",
                "Received": "es_date"
            }
        },
        {
            "_es_type": "nastedlog",
            "DataType": "log",
            "EventMap": {
                "Type": "URL",
                "SubType": "Allow",
                "Context": "Security"
            },
            "EventSource": {
                "Vendor": "PaloAlto",
                "IP": "192.168.1.151",
                "PrefixID": 3029,
                "Category": "Firewall",
                "Type": "Security System",
                "Description": "palo_alto_fw",
                "Tag": "palo_alto",
                "Serial": "0011C100469",
                "Collector": "syslog-udp"
            },
            "Event": {
                "VendorID": 9,
                "SystemID": 30299,
                "Info": "url web-browsing alert",
                "SubCategory": "url",
                "Category": "THREAT",
                "Action": "alert"
            },
            "Source": {
                "IP": "src_ipv4",
                "UserName": "username",
                "City": "Unknown",
                "Country": "src_country",
                "Interface": "ethernet1/21",
                "NatIP": "srcnat_ipv4",
                "NatPort": "srcnat_port",
                "Location": "unknown",
                "Port": "src_port",
                "Position": "in",
                "Zone": "trust"
            },
            "Destination": {
                "IP": "dst_ipv4",
                "City": "Unknown",
                "Country": "dst_country",
                "Interface": "ethernet1/23",
                "Location": "unknown",
                "NatIP": "dst_ipv4",
                "NatPort": "dst_port",
                "Port": "dst_port",
                "Position": "out",
                "Zone": "untrust"
            },
            "URL": {
                "Category": "url_category",
                "Domain": "url_domain",
                "Path": "url_path",
                "Scheme": "http"
            },
            "Application": {
                "Name": "web-browsing"
            },
            "Severity": {
                "ID": 6,
                "Name": "information"
            },
            "Protocol": {
                "Name": "tcp"
            },
            "Session": {
                "Direction": "client-to-server",
                "ID": "session_id"
            },
            "Rule": {
                "Name": "rule3"
            },
            "Time": {
                "Generated": "es_date",
                "Received": "es_date"
            }
        },
        {
            "_es_type": "nastedlog",
            "DataType": "log",
            "EventMap": {
                "Type": "URL",
                "SubType": "Allow",
                "Context": "Security"
            },
            "EventSource": {
                "Vendor": "PaloAlto",
                "IP": "192.168.1.151",
                "PrefixID": 3029,
                "Category": "Firewall",
                "Type": "Security System",
                "Description": "palo_alto_fw",
                "Tag": "palo_alto",
                "Serial": "0011C100469",
                "Collector": "syslog-udp"
            },
            "Event": {
                "VendorID": 9,
                "SystemID": 30299,
                "Info": "url ssl alert",
                "SubCategory": "url",
                "Category": "THREAT",
                "Action": "alert"
            },
            "Source": {
                "IP": "src_ipv4",
                "UserName": "username",
                "City": "Unknown",
                "Country": "src_country",
                "Interface": "ethernet1/23",
                "NatIP": "srcnat_ipv4",
                "NatPort": "srcnat_port",
                "Location": "unknown",
                "Port": "src_port",
                "Position": "in",
                "Zone": "trust"
            },
            "Destination": {
                "IP": "dst_ipv4",
                "City": "Unknown",
                "Country": "dst_country",
                "Interface": "ethernet1/21",
                "Location": "unknown",
                "NatIP": "dst_ipv4",
                "NatPort": "dst_port",
                "Port": "dst_port",
                "Position": "out",
                "Zone": "untrust"
            },
            "URL": {
                "Category": "url_category",
                "Domain": "url_domain",
                "Path": "url_path",
                "Scheme": "https"
            },
            "Application": {
                "Name": "ssl"
            },
            "Severity": {
                "ID": 6,
                "Name": "information"
            },
            "Protocol": {
                "Name": "tcp"
            },
            "Session": {
                "Direction": "client-to-server",
                "ID": "session_id"
            },
            "Rule": {
                "Name": "rule3"
            },
            "Time": {
                "Generated": "es_date",
                "Received": "es_date"
            }
        },
        {
            "_es_type": "nastedlog",
            "DataType": "log",
            "EventMap": {
                "Type": "URL",
                "SubType": "Block",
                "Context": "Security"
            },
            "EventSource": {
                "Vendor": "PaloAlto",
                "IP": "192.168.1.151",
                "PrefixID": 3029,
                "Category": "Firewall",
                "Type": "Security System",
                "Description": "palo_alto_fw",
                "Tag": "palo_alto",
                "Serial": "0011C100469",
                "Collector": "syslog-udp"
            },
            "Event": {
                "VendorID": 17,
                "SystemID": 302917,
                "Info": "url web-browsing block-url",
                "SubCategory": "url",
                "Category": "THREAT",
                "Action": "block-url"
            },
            "Source": {
                "IP": "src_ipv4",
                "UserName": "username",
                "City": "Unknown",
                "Country": "src_country",
                "Interface": "ethernet1/4",
                "Location": "unknown",
                "Port": "src_port",
                "Position": "in",
                "Zone": "trust"
            },
            "Destination": {
                "IP": "dst_ipv4",
                "City": "Unknown",
                "Country": "dst_country",
                "Interface": "ethernet1/4.1",
                "Location": "unknown",
                "Port": "80",
                "Position": "out",
                "Zone": "untrust"
            },
            "URL": {
                "Category": "url_category",
                "Domain": "url_domain",
                "Path": "url_path",
                "Scheme": "https"
            },
            "Application": {
                "Name": "web-browsing"
            },
            "Severity": {
                "ID": 4,
                "Name": "warning"
            },
            "Protocol": {
                "Name": "tcp"
            },
            "Session": {
                "Direction": "client-to-server",
                "ID": "session_id"
            },
            "Rule": {
                "Name": "rule4"
            },
            "Time": {
                "Generated": "es_date",
                "Received": "es_date"
            }
        },
        {
            "_es_type": "nastedlog",
            "DataType": "log",
            "EventMap": {
                "Type": "URL",
                "SubType": "Block",
                "Context": "Security"
            },
            "EventSource": {
                "Vendor": "PaloAlto",
                "IP": "192.168.1.151",
                "PrefixID": 3029,
                "Category": "Firewall",
                "Type": "Security System",
                "Description": "palo_alto_fw",
                "Tag": "palo_alto",
                "Serial": "0011C100469",
                "Collector": "syslog-udp"
            },
            "Event": {
                "VendorID": 17,
                "SystemID": 302917,
                "Info": "url ssl block-url",
                "SubCategory": "url",
                "Category": "THREAT",
                "Action": "block-url"
            },
            "Source": {
                "IP": "src_ipv4",
                "UserName": "username",
                "City": "Unknown",
                "Country": "src_country",
                "Interface": "ethernet1/4.1",
                "Location": "unknown",
                "Port": "src_port",
                "Position": "in",
                "Zone": "trust"
            },
            "Destination": {
                "IP": "dst_ipv4",
                "City": "Unknown",
                "Country": "dst_country",
                "Interface": "ethernet1/4",
                "Location": "unknown",
                "Port": "443",
                "Position": "out",
                "Zone": "untrust"
            },
            "URL": {
                "Category": "url_category",
                "Domain": "url_domain",
                "Path": "url_path",
                "Scheme": "https"
            },
            "Application": {
                "Name": "ssl"
            },
            "Severity": {
                "ID": 4,
                "Name": "warning"
            },
            "Protocol": {
                "Name": "tcp"
            },
            "Session": {
                "Direction": "client-to-server",
                "ID": "session_id"
            },
            "Rule": {
                "Name": "rule4"
            },
            "Time": {
                "Generated": "es_date",
                "Received": "es_date"
            }
        },
        {
            "_es_type": "nastedlog",
            "DataType": "log",
            "EventMap": {
                "Type": "Attack",
                "SubType": "Detect",
                "Context": "Security"
            },
            "EventSource": {
                "Vendor": "PaloAlto",
                "IP": "192.168.1.151",
                "PrefixID": 3029,
                "Category": "Firewall",
                "Type": "Security System",
                "Description": "palo_alto_fw",
                "Tag": "palo_alto",
                "Serial": "0011C100469",
                "Collector": "syslog-udp"
            },
            "Event": {
                "VendorID": 45,
                "SystemID": 302945,
                "Info": "file steam alert",
                "SubCategory": "file",
                "Category": "THREAT",
                "Action": "alert"
            },
            "Source": {
                "IP": "ipv4",
                "City": "Unknown",
                "Country": "src_country",
                "Interface": "ethernet1/21",
                "Location": "location",
                "Port": "src_port",
                "Position": "out",
                "Zone": "untrust"
            },
            "Destination": {
                "IP": "local_dst_ipv4",
                "City": "Unknown",
                "Country": "dst_country",
                "Interface": "ethernet1/21",
                "Location": "unknown",
                "Port": "dst_port",
                "Position": "in",
                "Zone": "trust"
            },
            "URL": {
                "Category": "url_category",
                "Domain": "url_domain",
                "Scheme": "http"
            },
            "Application": {
                "Name": "application_name"
            },
            "Severity": {
                "ID": 1,
                "Name": "alert"
            },
            "Protocol": {
                "Name": "tcp"
            },
            "Session": {
                "Direction": "client-to-server",
                "ID": "session_id"
            },
            "Rule": {
                "Name": "rule5"
            },
            "Time": {
                "Generated": "es_date",
                "Received": "es_date"
            }
        },
        {
            "_es_type": "nastedlog",
            "DataType": "log",
            "EventMap": {
                "Type": "Attack",
                "SubType": "Detect",
                "Context": "Security"
            },
            "EventSource": {
                "Vendor": "PaloAlto",
                "IP": "192.168.1.151",
                "PrefixID": 3029,
                "Category": "Firewall",
                "Type": "Security System",
                "Description": "palo_alto_fw",
                "Tag": "palo_alto",
                "Serial": "0011C100469",
                "Collector": "syslog-udp"
            },
            "Event": {
                "VendorID": 36,
                "SystemID": 302936,
                "Info": "vulnerability web-browsing alert",
                "SubCategory": "vulnerability",
                "Category": "THREAT",
                "Action": "alert"
            },
            "Source": {
                "IP": "src_ipv4",
                "City": "Unknown",
                "Country": "src_country",
                "Interface": "ethernet1/20",
                "Location": "location",
                "Port": "src_port",
                "Position": "in",
                "Zone": "trust"
            },
            "Destination": {
                "IP": "dst_ipv4",
                "City": "Unknown",
                "Country": "dst_country",
                "Interface": "ethernet1/21",
                "Location": "unknown",
                "Port": "dst_port",
                "Position": "out",
                "Zone": "untrust"
            },
            "URL": {
                "Category": "any",
                "Domain": "wp-login.php",
                "Scheme": "http"
            },
            "Details": {
                "RepeatCount": 2,
                "ThreatID": "WordPress Login BruteForce Attempt(40044)"
            },
            "Application": {
                "Name": "web-browsing"
            },
            "Severity": {
                "ID": 1,
                "Name": "alert"
            },
            "Protocol": {
                "Name": "tcp"
            },
            "Session": {
                "Direction": "client-to-server",
                "ID": "session_id"
            },
            "Rule": {
                "Name": "rule5"
            },
            "Time": {
                "Generated": "es_date",
                "Received": "es_date"
            }
        },
        {
            "_es_type": "nastedlog",
            "DataType": "log",
            "EventMap": {
                "Type": "Virus",
                "SubType": "Block",
                "Context": "Security"
            },
            "EventSource": {
                "Vendor": "PaloAlto",
                "IP": "192.168.1.151",
                "PrefixID": 3029,
                "Category": "Firewall",
                "Type": "Security System",
                "Description": "palo_alto_fw",
                "Tag": "palo_alto",
                "Serial": "0011C100469",
                "Collector": "syslog-udp"
            },
            "Event": {
                "VendorID": 91,
                "SystemID": 302991,
                "Info": "wildfire-virus smtp drop",
                "SubCategory": "vulnerability",
                "Category": "THREAT",
                "Action": "drop"
            },
            "Source": {
                "IP": "ipv4",
                "City": "Unknown",
                "Country": "src_country",
                "Interface": "ethernet1/20",
                "Location": "location",
                "Port": "src_port",
                "Position": "out",
                "Zone": "untrust"
            },
            "Destination": {
                "IP": "local_dst_ipv4",
                "City": "Unknown",
                "Country": "dst_country",
                "Interface": "ethernet1/21",
                "Location": "unknown",
                "Port": "dst_port",
                "Position": "in",
                "Zone": "trust"
            },
            "URL": {
                "Category": "any",
                "Domain": "po.sen260216kk.exe",
                "Scheme": "http"
            },
            "Application": {
                "Name": "smtp"
            },
            "Severity": {
                "ID": 6,
                "Name": "information"
            },
            "Details": {
                "Flags": "0x400000",
                "LogProfile": "Threat Alert",
                "ThreatID": "Virus/Win32.WGeneric.hjykm(3081002)"
            },
            "Protocol": {
                "Name": "tcp"
            },
            "Session": {
                "Direction": "client-to-server",
                "ID": "session_id"
            },
            "Rule": {
                "Name": "rule5"
            },
            "Time": {
                "Generated": "es_date",
                "Received": "es_date"
            }
        }
    ]
}
