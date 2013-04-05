{
    "fields" : [
        { "templateCount" : {"count":3} },
        { "url" : {"type": "from_list_file", "file" : "url.list", "method":"sequential" } },
        { "category" : {"type": "from_list_file", "file" : "category.list", "method":"sequential" } },
        { "date": {"type": "random", "generate_type":"datetime", "format": "Y-%m-%d" } },
        { "time": {"type": "random", "generate_type":"datetime", "format": "%H:%M:%S" } },
        { "ip" : {"type": "random", "generate_type":"IPv4" } },
        { "ip2" : {"type": "from_list_file", "file" : "ip.list", "method":"random" } },
        { "port" : {"type": "random", "generate_type":"integer", "min":1, "max":10000 } },
        { "port2" : {"type": "random", "generate_type":"integer", "min":1, "max":5000 } },
        { "number" : {"type": "random", "generate_type":"integer", "min":1, "max":5000 } }
    ],
    "template" : [
          "date=${date} time=${time} timezone=\"IST\" device_name=\"CR500i\" device_id=C010600411 deployment_mode=\"route\" log_id=010101600001 log_type=\"Firewall\" log_component=\"Firewall Rule\" log_subtype=\"Allowed\" priority=Information duration=0 fw_rule_id=85 user_name=\"xx\" user_gp=\"yy\" iap=16 application=\"zzz\" application_id=\"\" in_interface=\"Port A\" out_interface=\"Port B\" src_ip=${ip} src_mac=\"01:23:45:67:89:ab\" dst_ip=${ip2} protocol=\"TCP\" src_port=${port} dst_port=${port2} icmp_type=\"\" icmp_code=\"\" sent_pkts=45 recv_pkts=12 sent_bytes=${number} recv_bytes=${number} tran_src_ip=${ip} tran_src_port=\"${port}\" tran_dst_ip=\"${ip2}\" tran_dst_port=\"${port2}\" srczonetype=\"LAN\" dstzonetype=\"WAN\" dir_disp=\"org\" connevent=\"start\" connid=\"${number}\" vconnid=\"\"",
          "date=${date} time=${time} timezone=\"EET\" device_name=\"CR50ia\" device_id=C105600516-QY4U5F deployment_mode=\"Route\" log_id=050902616002 log_type=\"Content Filtering\" log_component=\"HTTP\" log_subtype=\"Denied\" status=\"\" priority=Information fw_rule_id=0 user_name=\"xy\" user_gp=\"yz\" iap=12 category=\"${category}\" category_type=\"Non Working\" url=\"${url}\" contenttype=\"\" httpresponsecode=\"\" src_ip=${ip} dst_ip=${ip2} protocol=\"TCP\" src_port=${port} dst_port=${port2} sent_bytes=0 recv_bytes=${number} domain=${url}",
          "date=${date} time=${time} timezone=\"EET\" device_name=\"CR50ia\" device_id=C105600516-QY4U5F log_id=063411660020 log_type=\"Event\" log_component=\"DHCP Server\" log_subtype=\"System\" status=\"Renew\" priority=Information ipaddress=\"${ip}\" client_physical_address=\"x8:00:c6:08:zz:yy\"' client_host_name=\"\" message=\"Lease 172.16.0.141 renewed\" raw_data=\"172.16.0.141   Thu 21 Mar 14:08:46 2013        Sat 23 Mar 14:08:46 2013        x4:y3:z5:1a:00:tt       -\""
    ]
}
