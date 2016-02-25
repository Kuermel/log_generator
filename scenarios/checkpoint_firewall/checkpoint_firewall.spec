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
        { "host_name" : {"type": "from_list_file", "file" : "host_name.list", "method":"random" } },
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
                     "EventMap": {
                         "Type": "Session",
                         "SubType": "Allow",
                         "Context": "Network"
                     },
                     "EventSource": {
                         "Vendor": "CheckPoint",
                         "IP": "192.168.1.156",
                         "PrefixID": 3020,
                         "Tag": "Checkpoint",
                         "Category": "Firewall",
                         "Type": "Security System",
                         "Description": "checkpoint_fw",
                         "Collector": "lea_fw.log"
                     },
                     "Event": {
                         "VendorID": 18,
                         "SystemID": 302018,
                         "Info": "The firewall accepted a connection",
                         "Category": " VPN-1 & FireWall-1",
                         "Action": "accept"
                     },
                     "Source": {
                         "IP": "src_ipv4",
                         "HostName": "host_name",
                         "City": "Unknown",
                         "Country": "src_country",
                         "Location": "Unknown",
                         "Port": "src_port",
                         "Position": "in",
                         "UserName": "username"
                     },
                     "Destination": {
                         "IP": "local_dst_ipv4",
                         "City": "Unknown",
                         "Country": "src_country",
                         "Location": "Unknown",
                         "Port": "dst_port",
                         "Position": "in"
                     },
                     "Details": {
                         "I/fName": "eth2",
                         "Inzone": "Internal",
                         "Orig": "10.1.4.2",
                         "OrigName": "MasterFW",
                         "Outzone": "Local"
                     },
                     "Severity": {
                         "ID": 6,
                         "Name": "information"
                     },
                     "Protocol": {
                         "Name": "tcp"
                     },
                     "Session": {
                         "ID": "session_id"
                     },
                     "Time": {
                         "Generated": "es_date",
                         "Received": "es_date"
                     }
             },
             {
                     "_es_type": "nastedlog",
                     "EventMap": {
                         "Type": "Session",
                         "SubType": "Allow",
                         "Context": "Network"
                     },
                     "EventSource": {
                         "Vendor": "CheckPoint",
                         "IP": "192.168.1.156",
                         "PrefixID": 3020,
                         "Tag": "Checkpoint",
                         "Category": "Firewall",
                         "Type": "Security System",
                         "Description": "checkpoint_fw",
                         "Collector": "lea_fw.log"
                     },
                     "Event": {
                         "VendorID": 18,
                         "SystemID": 302018,
                         "Info": "The firewall accepted a connection",
                         "Category": " VPN-1 & FireWall-1",
                         "Action": "accept"
                     },
                     "Source": {
                         "IP": "src_ipv4",
                         "HostName": "host_name",
                         "City": "Unknown",
                         "Country": "src_country",
                         "Location": "Unknown",
                         "Port": "src_port",
                         "Position": "in",
                         "UserName": "username"
                     },
                     "Destination": {
                         "IP": "dst_ipv4",
                         "City": "Unknown",
                         "Country": "dst_country",
                         "Location": "Unknown",
                         "Port": "dst_port",
                         "Position": "out"
                     },
                     "Details": {
                         "I/fName": "eth2",
                         "Inzone": "Internal",
                         "Orig": "10.1.4.2",
                         "OrigName": "MasterFW",
                         "Outzone": "External"
                     },
                     "Severity": {
                         "ID": 6,
                         "Name": "information"
                     },
                     "Protocol": {
                         "Name": "tcp"
                     },
                     "Session": {
                         "ID": "session_id"
                     },
                     "Time": {
                         "Generated": "es_date",
                         "Received": "es_date"
                     }
             },
             {
                     "_es_type": "nastedlog",
                     "EventMap": {
                         "Type": "Session",
                         "SubType": "Info",
                         "Context": "Network"
                     },
                     "EventSource": {
                         "Vendor": "CheckPoint",
                         "IP": "192.168.1.156",
                         "PrefixID": 3020,
                         "Tag": "Checkpoint",
                         "Category": "Firewall",
                         "Type": "Security System",
                         "Description": "checkpoint_fw",
                         "Collector": "lea_fw.log"
                     },
                     "Event": {
                         "VendorID": 22,
                         "SystemID": 302022,
                         "Info": "Web access status",
                         "Note": "Address spoofing",
                         "Category": " VPN-1 & FireWall-1",
                         "Action": "monitor"
                     },
                     "Source": {
                         "IP": "ipv4",
                         "City": "Unknown",
                         "Country": "src_country",
                         "Location": "Unknown",
                         "Port": "src_port",
                         "Position": "out"
                     },
                     "Destination": {
                         "IP": "local_dst_ipv4",
                         "City": "Unknown",
                         "Country": "dst_country",
                         "Location": "Unknown",
                         "Port": "dst_port",
                         "Position": "in"
                     },
                     "Details": {
                         "I/fName": "eth4",
                         "I/fDir": "inbound",
                         "Inzone": "Internal",
                         "Orig": "10.1.4.2",
                         "OrigName": "MasterFW"
                     },
                     "Severity": {
                         "ID": 6,
                         "Name": "information"
                     },
                     "Protocol": {
                         "Name": "icmp"
                     },
                     "Time": {
                         "Generated": "es_date",
                         "Received": "es_date"
                     }
             },
             {
                     "_es_type": "nastedlog",
                     "EventMap": {
                         "Type": "Session",
                         "SubType": "Deny",
                         "Context": "Network"
                     },
                     "EventSource": {
                         "Vendor": "CheckPoint",
                         "IP": "192.168.1.156",
                         "PrefixID": 3020,
                         "Tag": "Checkpoint",
                         "Category": "Firewall",
                         "Type": "Security System",
                         "Description": "checkpoint_fw",
                         "Collector": "lea_fw.log"
                     },
                     "Event": {
                         "VendorID": 21,
                         "SystemID": 302021,
                         "Info": "The firewall dropped a connection",
                         "Category": " VPN-1 & FireWall-1",
                         "Action": "drop"
                     },
                     "Source": {
                         "IP": "src_ipv4",
                         "HostName": "host_name",
                         "City": "Unknown",
                         "Country": "src_country",
                         "Location": "Unknown",
                         "Port": "src_port",
                         "Position": "in",
                         "UserName": "username"
                     },
                     "Destination": {
                         "IP": "dst_ipv4",
                         "City": "Unknown",
                         "Country": "dst_country",
                         "Location": "Unknown",
                         "Port": "dst_port",
                         "Position": "out"
                     },
                     "Details": {
                         "I/fName": "eth2",
                         "Inzone": "Internal",
                         "Orig": "10.1.4.2",
                         "OrigName": "MasterFW",
                         "Outzone": "External",
                         "RuleUid": "{ACF463D4-45FE-4AE7-B6DB-F6314CEEFB0B}"
                     },
                     "Severity": {
                         "ID": 6,
                         "Name": "information"
                     },
                     "Protocol": {
                         "Name": "udp"
                     },
                     "Rule": {
                         "Name": 44
                     },
                     "Session": {
                         "ID": "session_id"
                     },
                     "Time": {
                         "Generated": "es_date",
                         "Received": "es_date"
                     }
             },
             {
                      "_es_type": "nastedlog",
                      "EventMap": {
                          "Type": "Session",
                          "SubType": "Deny",
                          "Context": "Network"
                      },
                      "EventSource": {
                          "Vendor": "CheckPoint",
                          "IP": "192.168.1.156",
                          "PrefixID": 3020,
                          "Tag": "Checkpoint",
                          "Category": "Firewall",
                          "Type": "Security System",
                          "Description": "checkpoint_fw",
                          "Collector": "lea_fw.log"
                      },
                      "Event": {
                          "VendorID": 21,
                          "SystemID": 302021,
                          "Info": "The firewall dropped a connection",
                          "Category": " VPN-1 & FireWall-1",
                          "Action": "drop"
                      },
                      "Source": {
                          "IP": "ipv4",
                          "City": "Unknown",
                          "Country": "src_country",
                          "Location": "Unknown",
                          "Port": "src_port",
                          "Position": "out"
                      },
                      "Destination": {
                          "IP": "local_dst_ipv4",
                          "City": "Unknown",
                          "Country": "dst_country",
                          "Location": "Unknown",
                          "Port": "dst_port",
                          "Position": "in"
                      },
                      "Details": {
                          "I/fName": "eth2",
                          "Inzone": "Internal",
                          "Icmp": "Echo Request",
                          "Orig": "10.1.4.2",
                          "I/fDir": "inbound",
                          "OrigName": "MasterFW",
                          "Outzone": "External"
                      },
                      "Severity": {
                          "ID": 6,
                          "Name": "information"
                      },
                      "Protocol": {
                          "Name": "icmp"
                      },
                      "Rule": {
                          "Name": 54
                      },
                      "Session": {
                          "ID": "session_id"
                      },
                      "Time": {
                          "Generated": "es_date",
                          "Received": "es_date"
                      }
             },
             {
                     "_es_type": "nastedlog",
                     "EventMap": {
                         "Type": "Session",
                         "SubType": "Allow",
                         "Context": "Network"
                     },
                     "EventSource": {
                         "Vendor": "CheckPoint",
                         "IP": "192.168.1.156",
                         "PrefixID": 3020,
                         "Tag": "Checkpoint",
                         "Category": "Firewall",
                         "Type": "Security System",
                         "Description": "checkpoint_fw",
                         "Collector": "lea_fw.log"
                     },
                     "Event": {
                         "VendorID": 19,
                         "SystemID": 302019,
                         "Info": "The firewall decrypted a connection",
                         "Category": " VPN-1 & FireWall-1",
                         "Action": "decrypted"
                     },
                     "Source": {
                         "IP": "src_ipv4",
                         "City": "Unknown",
                         "Country": "Unknown",
                         "UserName": "username",
                         "HostName": "host_name",
                         "Location": "Unknown",
                         "Port": "src_port",
                         "Position": "in"
                     },
                     "Destination": {
                         "IP": "local_dst_ipv4",
                         "City": "Unknown",
                         "Country": "Unknown",
                         "Location": "Unknown",
                         "Port": "dst_port",
                         "Position": "in"
                     },
                     "Details": {
                         "I/fName": "eth2",
                         "Inzone": "External",
                         "DstName": "SRV_Master_DB",
                         "Community": "RemoteAccess",
                         "FwSubproduct": "VPN-1",
                         "Orig": "10.1.4.2",
                         "OrigName": "MasterFW",
                         "Outzone": "Internal",
                         "PeerGateway": "src_ipv4",
                         "Method": "ESP: 3DES + SHA1",
                         "Scheme": "IKE",
                         "VPNFeatureName": "VPN",
                         "VpnUser": "username"
                     },
                     "Severity": {
                         "ID": 6,
                         "Name": "information"
                     },
                     "Protocol": {
                         "Name": "tcp"
                     },
                     "Rule": {
                         "Name": 4
                     },
                     "Time": {
                         "Generated": "es_date",
                         "Received": "es_date"
                     }
             },
             {
                     "_es_type": "nastedlog",
                     "EventMap": {
                         "Type": "Session",
                         "SubType": "Allow",
                         "Context": "Network"
                     },
                     "EventSource": {
                         "Vendor": "CheckPoint",
                         "IP": "192.168.1.156",
                         "PrefixID": 3020,
                         "Tag": "Checkpoint",
                         "Category": "Firewall",
                         "Type": "Security System",
                         "Description": "checkpoint_fw",
                         "Collector": "lea_fw.log"
                     },
                     "Event": {
                         "VendorID": 19,
                         "SystemID": 302019,
                         "Info": "The firewall decrypted a connection",
                         "Category": " VPN-1 & FireWall-1",
                         "Action": "decrypted"
                     },
                     "Source": {
                         "IP": "src_ipv4",
                         "City": "Unknown",
                         "Country": "src_country",
                         "Location": "Unknown",
                         "Port": "src_port",
                         "Position": "in",
                         "HostName": "host_name"
                     },
                     "Destination": {
                         "IP": "local_dst_ipv4",
                         "City": "Unknown",
                         "Country": "src_country",
                         "Location": "Unknown",
                         "Port": "dst_port",
                         "Position": "in"
                     },
                     "Details": {
                         "I/fName": "eth2",
                         "Inzone": "External",
                         "Community": "RemoteConnections",
                         "DstName": "SAP_Master_DB",
                         "FwSubproduct": "VPN-1",
                         "Orig": "10.1.4.2",
                         "OrigName": "MasterFW",
                         "Outzone": "Internal",
                         "PeerGateway": "src_ipv4",
                         "Scheme": "SSL",
                         "VPNFeatureName": "VPN",
                         "VpnUser": "username"
                     },
                     "Severity": {
                         "ID": 6,
                         "Name": "information"
                     },
                     "Protocol": {
                         "Name": "tcp"
                     },
                     "Rule": {
                         "Name": 4
                     },
                     "Time": {
                         "Generated": "es_date",
                         "Received": "es_date"
                     }
             },
             {
                     "_es_type": "nastedlog",
                     "EventMap": {
                         "Type": "Session",
                         "SubType": "Allow",
                         "Context": "Network"
                     },
                     "EventSource": {
                         "Vendor": "CheckPoint",
                         "IP": "192.168.1.156",
                         "PrefixID": 3020,
                         "Tag": "Checkpoint",
                         "Category": "Firewall",
                         "Type": "Security System",
                         "Description": "checkpoint_fw",
                         "Collector": "lea_fw.log"
                     },
                     "Event": {
                         "VendorID": 20,
                         "SystemID": 302020,
                         "Info": "The firewall encrypted a connection",
                         "Category": " VPN-1 & FireWall-1",
                         "Action": "encrypted"
                     },
                     "Source": {
                         "IP": "src_ipv4",
                         "City": "Unknown",
                         "Country": "src_country",
                         "Location": "Unknown",
                         "Port": "src_port",
                         "Position": "in",
                         "HostName": "Tech_BIG_STORAGE"
                     },
                     "Destination": {
                         "IP": "local_dst_ipv4",
                         "City": "Unknown",
                         "Country": "src_country",
                         "Location": "Unknown",
                         "Port": "dst_port",
                         "Position": "in"
                     },
                     "Details": {
                         "I/fName": "eth4",
                         "Inzone": "Internal",
                         "Community": "Logsign_Europe",
                         "DstName": "SAP_Master_DB",
                         "FwSubproduct": "VPN-1",
                         "Orig": "10.1.4.2",
                         "OrigName": "MasterFW",
                         "Outzone": "External",
                         "PeerGateway": "ipv4",
                         "Method": "ESP: 3DES + SHA1",
                         "Scheme": "IKE",
                         "VPNFeatureName": "VPN"
                     },
                     "Severity": {
                         "ID": 6,
                         "Name": "information"
                     },
                     "Protocol": {
                         "Name": "tcp"
                     },
                     "Rule": {
                         "Name": 4
                     },
                     "Time": {
                         "Generated": "es_date",
                         "Received": "es_date"
                     }
             },
             {
                     "_es_type": "nastedlog",
                     "EventMap": {
                         "Type": "Session",
                         "SubType": "Info",
                         "Context": "Network"
                     },
                     "EventSource": {
                         "Vendor": "CheckPoint",
                         "IP": "192.168.1.156",
                         "PrefixID": 3020,
                         "Tag": "Checkpoint",
                         "Category": "Firewall",
                         "Type": "Security System",
                         "Description": "checkpoint_fw",
                         "Collector": "lea_fw.log"
                     },
                     "Event": {
                         "VendorID": 24,
                         "SystemID": 302024,
                         "Info": "Session not set",
                         "Category": " VPN-1 & FireWall-1"
                     },
                     "Source": {
                         "IP": "src_ipv4",
                         "City": "Unknown",
                         "Country": "src_country",
                         "Location": "Unknown",
                         "Port": "src_port",
                         "Position": "in",
                         "HostName": "Tech_BIG_STORAGE"
                     },
                     "Destination": {
                         "IP": "local_dst_ipv4",
                         "City": "Unknown",
                         "Country": "src_country",
                         "Location": "Unknown",
                         "Port": "dst_port",
                         "Position": "in"
                     },
                     "Details": {
                         "FwMessage": "Parameter 'Connections hash table size' changed from 32768 to 1048576",
                         "I/fDir": "inbound",
                         "Orig": "10.1.4.2",
                         "OrigName": "MasterFW",
                         "Outzone": "External",
                         "PeerGateway": "ipv4",
                         "Method": "ESP: 3DES + SHA1",
                         "Scheme": "IKE",
                         "VPNFeatureName": "VPN"
                     },
                     "Severity": {
                         "ID": 6,
                         "Name": "information"
                     },
                     "Protocol": {
                         "Name": "tcp"
                     },
                     "Rule": {
                         "Name": 4
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
                         "Vendor": "CheckPoint",
                         "IP": "192.168.1.156",
                         "PrefixID": 3020,
                         "Category": "Firewall",
                         "Tag": "Checkpoint",
                         "Type": "Security System",
                         "Description": "checkpoint_fw",
                         "Collector": "lea_fw.log"
                     },
                     "Event": {
                         "VendorID": 1,
                         "SystemID": 30201,
                         "Info": "The firewall allowed a URL",
                         "Category": "URL Filtering",
                         "Action": "allow"
                     },
                     "Source": {
                         "IP": "src_ipv4",
                         "HostName": "host_name",
                         "City": "Unknown",
                         "Country": "src_country",
                         "Location": "Unknown",
                         "Port": "src_port",
                         "Position": "in",
                         "UserName": "username"
                     },
                     "Destination": {
                         "IP": "dst_ipv4",
                         "Country": "dst_country",
                         "City": "Unknown",
                         "Location": "Unknown",
                         "Port": "dst_port",
                         "Position": "out"
                     },
                     "URL": {
                         "Domain": "url_domain",
                         "Path": "url_path",
                         "Category": "url_category",
                         "Scheme": "url_scheme"
                     },
                     "Severity": {
                         "ID": 6,
                         "Name": "information"
                     },
                     "Details": {
                         "AppProperties": "url_category",
                         "I/fDir": "outbound",
                         "I/fName": "eth1",
                         "AppRuleName": "Staffs_And_Admins_Allow",
                         "Orig": "192.168.1.156",
                         "ProxySrcIP": "src_ipv4",
                         "ProxySrcIPName": "username",
                         "WebClientType": "Chrome",
                         "WebServerType": "Other: nginx/1.8.0"
                     },
                     "Protocol": {
                         "Name": "tcp"
                     },
                     "Session": {
                         "ID": "session_id"
                     },
                     "Service": {
                         "Name": "url_scheme"
                     },
                     "Time": {
                         "Generated": "es_date",
                         "Received": "es_date"
                     }
             },
             {
                     "_es_type": "nastedlog",
                     "EventMap": {
                         "Type": "URL",
                         "SubType": "Block",
                         "Context": "Security"
                     },
                     "EventSource": {
                         "Vendor": "CheckPoint",
                         "IP": "192.168.1.156",
                         "PrefixID": 3020,
                         "Category": "Firewall",
                         "Tag": "Checkpoint",
                         "Type": "Security System",
                         "Description": "checkpoint_fw",
                         "Collector": "lea_fw.log"
                     },
                     "Event": {
                         "VendorID": 2,
                         "SystemID": 30202,
                         "Info": "The firewall blocked a URL",
                         "Category": "URL Filtering",
                         "Action": "block"
                     },
                     "Source": {
                         "IP": "src_ipv4",
                         "HostName": "host_name",
                         "City": "Unknown",
                         "Country": "src_country",
                         "Location": "Unknown",
                         "Port": "src_port",
                         "Position": "in",
                         "UserName": "username"
                     },
                     "Destination": {
                         "IP": "dst_ipv4",
                         "City": "Unknown",
                         "Country": "dst_country",
                         "Location": "Unknown",
                         "Port": "dst_port",
                         "Position": "out"
                     },
                     "URL": {
                         "Domain": "url_domain",
                         "Path": "url_path",
                         "Category": "url_category",
                         "Scheme": "url_scheme"
                     },
                     "Severity": {
                         "ID": 6,
                         "Name": "information"
                     },
                     "Details": {
                         "AppProperties": "url_category",
                         "I/fDir": "outbound",
                         "I/fName": "eth5",
                         "Orig": "192.168.1.156",
                         "ProxySrcIP": "src_ipv4",
                         "ProxySrcIPName": "username",
                         "UsercheckConfirmationLevel": "Application",
                         "WebClientType": "Firefox",
                         "WebServerType": "Other: ECS (fcn/41D2)"
                     },
                     "Protocol": {
                         "Name": "tcp"
                     },
                     "Session": {
                         "ID": "session_id"
                     },
                     "Service": {
                         "Name": "url_scheme"
                     },
                     "Time": {
                         "Generated": "es_date",
                         "Received": "es_date"
                     }
             },
             {
                     "_es_type": "nastedlog",
                     "EventMap": {
                         "Type": "URL",
                         "SubType": "Info",
                         "Context": "Security"
                     },
                     "EventSource": {
                         "Vendor": "CheckPoint",
                         "IP": "192.168.1.156",
                         "PrefixID": 3020,
                         "Category": "Firewall",
                         "Tag": "Checkpoint",
                         "Type": "Security System",
                         "Description": "checkpoint_fw",
                         "Collector": "lea_fw.log"
                     },
                     "Event": {
                         "VendorID": 92,
                         "SystemID": 302092,
                         "Info": "HTTPS Inspection info",
                         "Category": "URL Filtering",
                         "Action": "HTTPS Inspect"
                     },
                     "Source": {
                         "IP": "src_ipv4",
                         "HostName": "host_name",
                         "City": "Unknown",
                         "Country": "src_country",
                         "Location": "Unknown",
                         "Port": "src_port",
                         "Position": "in",
                         "UserName": "username"
                     },
                     "Destination": {
                         "IP": "dst_ipv4",
                         "City": "Unknown",
                         "Country": "dst_country",
                         "Location": "Unknown",
                         "Port": "dst_port",
                         "Position": "out"
                     },
                     "URL": {
                         "Domain": "url_domain",
                         "Path": "url_path",
                         "Category": "url_category",
                         "Scheme": "url_scheme"
                     },
                     "Severity": {
                         "ID": 6,
                         "Name": "information"
                     },
                     "Details": {
                         "AppProperties": "url_category",
                         "I/fDir": "inbound",
                         "HttpsInspectionAction" : "Inspect",
                         "I/fName": "eth2",
                         "Orig": "192.168.1.156",
                         "ProxySrcIP": "src_ipv4",
                         "ProxySrcIPName": "username"
                     },
                     "Protocol": {
                         "Name": "tcp"
                     },
                     "Application": {
                         "Name": "url_category"
                     },
                     "Session": {
                         "ID": "session_id"
                     },
                     "Service": {
                         "Name": "https"
                     },
                     "Time": {
                         "Generated": "es_date",
                         "Received": "es_date"
                     }
             },
             {
                     "_es_type": "nastedlog",
                     "EventMap": {
                         "Type": "URL",
                         "SubType": "Redirect",
                         "Context": "Security"
                     },
                     "EventSource": {
                         "Vendor": "CheckPoint",
                         "IP": "192.168.1.156",
                         "PrefixID": 3020,
                         "Category": "Firewall",
                         "Tag": "Checkpoint",
                         "Type": "Security System",
                         "Description": "checkpoint_fw",
                         "Collector": "lea_fw.log"
                     },
                     "Event": {
                         "VendorID": 57,
                         "SystemID": 302057,
                         "Info": "Application Control redirect",
                         "Category": "Application Control",
                         "Action": "redirect"
                     },
                     "Source": {
                         "IP": "src_ipv4",
                         "HostName": "host_name",
                         "City": "Unknown",
                         "Country": "src_country",
                         "Location": "Unknown",
                         "Port": "src_port",
                         "Position": "in",
                         "UserName": "username"
                     },
                     "Destination": {
                         "IP": "dst_ipv4",
                         "City": "Unknown",
                         "Country": "dst_country",
                         "Location": "Unknown",
                         "Port": "dst_port",
                         "Position": "out"
                     },
                     "URL": {
                         "Domain": "url_domain",
                         "Path": "url_path",
                         "Category": "url_category",
                         "Scheme": "url_scheme"
                     },
                     "Severity": {
                         "ID": 6,
                         "Name": "information"
                     },
                     "Details": {
                         "AppProperties": "url_category",
                         "I/fDir": "outbound",
                         "HttpsInspectionAction" : "Inspect",
                         "I/fName": "eth2",
                         "Orig": "192.168.1.156",
                         "ProxySrcIP": "src_ipv4",
                         "WebClientType": "Chrome"
                     },
                     "Protocol": {
                         "Name": "tcp"
                     },
                     "Application": {
                         "Category": "url_category"
                     },
                     "Session": {
                         "ID": "session_id"
                     },
                     "Service": {
                         "Name": "url_scheme"
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
                         "SubType": "Detect",
                         "Context": "Security"
                     },
                     "EventSource": {
                         "Vendor": "CheckPoint",
                         "IP": "192.168.1.156",
                         "PrefixID": 3020,
                         "Category": "Firewall",
                         "Tag": "Checkpoint",
                         "Type": "Security System",
                         "Description": "checkpoint_fw",
                         "Collector": "lea_fw.log"
                     },
                     "Event": {
                         "VendorID": 45,
                         "SystemID": 302045,
                         "Info": "Antivirus monitor",
                         "Note": "Connection was allowed because background classification mode was set. See sk74120 for more information.",
                         "Category": "New Anti Virus",
                         "Action": "monitor"
                     },
                     "Source": {
                         "IP": "src_ipv4",
                         "HostName": "host_name",
                         "City": "Unknown",
                         "Country": "src_country",
                         "Location": "Unknown",
                         "Port": "src_port",
                         "Position": "in"
                     },
                     "Destination": {
                         "IP": "dst_ipv4",
                         "City": "Unknown",
                         "Country": "dst_country",
                         "Location": "Unknown",
                         "Port": "53",
                         "Position": "out"
                     },
                     "Severity": {
                         "ID": 6,
                         "Name": "information"
                     },
                     "Details": {
                         "ActionDetails": "bypass",
                         "ConfidenceLevel": 5,
                         "DestinationDnsHostname": "everyshop.xyz",
                         "I/fDir": "outbound",
                         "HttpsInspectionAction" : "Inspect",
                         "I/fName": "eth3",
                         "MalwareAction": "Malicious DNS request",
                         "MalwareFamily": "Phishing",
                         "MalwareRuleID": "'000000E4-0027-004D-8808-68C4094D0EC9'",
                         "ProtectionName": "Phishing.cpwgum",
                         "ProtectionType": "DNS reputation",
                         "Scope": "src_ipv4",
                         "ScopeName": "host_name",
                         "Orig": "192.168.1.156",
                         "ProxySrcIP": "src_ipv4",
                         "WebClientType": "Chrome"
                     },
                     "Protocol": {
                         "Name": "udp"
                     },
                     "Session": {
                         "ID": "session_id"
                     },
                     "Service": {
                         "Name": "domain_udp"
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
                         "Vendor": "CheckPoint",
                         "IP": "192.168.1.156",
                         "PrefixID": 3020,
                         "Category": "Firewall",
                         "Tag": "Checkpoint",
                         "Type": "Security System",
                         "Description": "checkpoint_fw",
                         "Collector": "lea_fw.log"
                     },
                     "Event": {
                         "VendorID": 28,
                         "SystemID": 302028,
                         "Info": "Invalid checksum packet dropped",
                         "Category": "SmartDefense",
                         "Action": "drop"
                     },
                     "Source": {
                         "IP": "src_ipv4",
                         "HostName": "host_name",
                         "City": "Unknown",
                         "Country": "src_country",
                         "Location": "Unknown",
                         "Port": "src_port",
                         "Position": "in",
                         "UserName": "username"
                     },
                     "Destination": {
                         "IP": "dst_ipv4",
                         "City": "Unknown",
                         "Country": "dst_country",
                         "Location": "Unknown",
                         "Port": "dst_port",
                         "Position": "out"
                     },
                     "Severity": {
                         "ID": 6,
                         "Name": "information"
                     },
                     "Attack": {
                         "Name": "Streaming Engine: TCP Segment Limit Enforcement"
                     },
                     "Details": {
                         "AttackInfo": "TCP segment out of maximum allowed sequence. Packet dropped.",
                         "ConfidenceLevel": 0,
                         "I/fDir": "outbound",
                         "HttpsInspectionAction" : "Inspect",
                         "I/fName": "eth3",
                         "RuleUid": "'7405DBDD-A351-48C9-8611-29D92D42AA92'",
                         "ProtectionName": "TCP Segment Limit Enforcement",
                         "ProtectionType": "settings_tcp"
                     },
                     "Protocol": {
                         "Name": "tcp"
                     },
                     "Session": {
                         "ID": "session_id"
                     },
                     "Service": {
                         "Name": "https"
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
                         "SubType": "Detect",
                         "Context": "Security"
                     },
                     "EventSource": {
                         "Vendor": "CheckPoint",
                         "IP": "192.168.1.156",
                         "PrefixID": 3020,
                         "Category": "Firewall",
                         "Tag": "Checkpoint",
                         "Type": "Security System",
                         "Description": "checkpoint_fw",
                         "Collector": "lea_fw.log"
                     },
                     "Event": {
                         "VendorID": 30,
                         "SystemID": 302030,
                         "Info": "Smart defence accept",
                         "Category": "SmartDefense",
                         "Action": "accept"
                     },
                     "Source": {
                         "IP": "src_ipv4",
                         "HostName": "host_name",
                         "City": "Unknown",
                         "Country": "src_country",
                         "Location": "Unknown",
                         "Port": "src_port",
                         "Position": "in",
                         "UserName": "username"
                     },
                     "Destination": {
                         "IP": "dst_ipv4",
                         "City": "Unknown",
                         "Country": "dst_country",
                         "Location": "Unknown",
                         "Port": "dst_port",
                         "Position": "out"
                     },
                     "URL": {
                         "Domain": "url_domain",
                         "Path": "url_path",
                         "Category": "url_category",
                         "Scheme": "url_scheme"
                     },
                     "Severity": {
                         "ID": 6,
                         "Name": "information"
                     },
                     "Details": {
                         "I/fDir": "outbound",
                         "HttpsInspectionAction" : "Inspect",
                         "I/fName": "eth3",
                         "PreciseError": "unknown error",
                         "ProxySrcIP": "src_ipv4",
                         "Reason": "HTTP parsing error occurred, bypass request.",
                         "WebClientType": "Chrome"
                     },
                     "Protocol": {
                         "Name": "tcp"
                     },
                     "Session": {
                         "ID": "session_id"
                     },
                     "Service": {
                         "Name": "https"
                     },
                     "Time": {
                         "Generated": "es_date",
                         "Received": "es_date"
                     }
             },
             {
                     "_es_type": "nastedlog",
                     "EventMap": {
                         "Type": "Malware",
                         "SubType": "Info",
                         "Context": "Security"
                     },
                     "EventSource": {
                         "Vendor": "CheckPoint",
                         "IP": "192.168.1.156",
                         "PrefixID": 3020,
                         "Category": "Firewall",
                         "Tag": "Checkpoint",
                         "Type": "Security System",
                         "Description": "checkpoint_fw",
                         "Collector": "lea_fw.log"
                     },
                     "Event": {
                         "VendorID": 28,
                         "SystemID": 302028,
                         "Info": "Antimalware monitor",
                         "Note": "Spam email",
                         "Category": "Anti Malware",
                         "Action": "monitor"
                     },
                     "Source": {
                         "IP": "src_ipv4",
                         "HostName": "host_name",
                         "City": "Unknown",
                         "Country": "src_country",
                         "Location": "Unknown",
                         "Port": "src_port",
                         "Position": "in"
                     },
                     "Destination": {
                         "IP": "dst_ipv4",
                         "City": "Unknown",
                         "Country": "dst_country",
                         "Location": "Unknown",
                         "Port": 25,
                         "Position": "out"
                     },
                     "Severity": {
                         "ID": 6,
                         "Name": "information"
                     },
                     "Details": {
                         "ConfidenceLevel": 0,
                         "EmailControl": "Anti Malware",
                         "EmailID": 2439695431,
                         "EmailRecipientsNum": 1,
                         "EmailSessionID": "'56CC514B-0-204010A-C0000000'",
                         "From": "sales.europe@logsign.com",
                         "I/fDir": "outbound",
                         "I/fName": "SMTP transparent proxy",
                         "MalwareAction": "Spam",
                         "MalwareRuleID": "'000000E4-0027-004D-8808-68C4094D0EC9'",
                         "Orig": "src_ipv4",
                         "ProtectionName": "Mail analysis",
                         "ProtectionType": "email",
                         "Reason": "CFCHttpClient::ConnectHost() - SocketError: 111",
                         "ScanDirection": "Internal to External",
                         "To": "account@jfg-avtg.com lgsgn@xyz.com"
                     },
                     "Protocol": {
                         "Name": "tcp"
                     },
                     "Session": {
                         "ID": "session_id"
                     },
                     "Service": {
                         "Name": "smtp"
                     },
                     "Time": {
                         "Generated": "es_date",
                         "Received": "es_date"
                     }
             }
    ]
}
