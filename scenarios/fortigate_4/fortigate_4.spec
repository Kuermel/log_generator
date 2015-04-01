{
    "fields" : [
        { "templateCount" : {"count":3 } },
        { "date": {"type": "random", "generate_type":"datetime", "format": "%Y-%m-%d" } },
        { "time": {"type": "random", "generate_type":"datetime", "format": "%H:%M:%S" } },
        { "url" : {"type": "from_list_file", "file" : "url.list", "method":"sequential" } },
        { "ip" : {"type": "from_list_file", "file" : "ip.list", "method":"random" } },
        { "ip2" : {"type": "random", "generate_type":"IPv4" } },
        { "port" : {"type": "random", "generate_type":"integer", "min":1, "max":10000 } },
        { "port2" : {"type": "random", "generate_type":"integer", "min":1, "max":5000 } },
        { "pri" : {"type": "from_list_file", "file" : "pri.list", "method":"random" } }
    ],
    "template" : [
        "date=${date} time=${time} devname=FGT60B3907506583 device_id=FGT60B3907506583 log_id=1059028704 type=app-ctrl subtype=app-ctrl-all pri=${pri} vd=\"root\" attack_id=16195 user=\"N/A\" group=\"N/A\" src=${ip} src_port=${port} src_int=\"internal\" dst=${ip2} dst_port=${port2} dst_int=\"wan1\" src_name=\"${ip}\" dst_name=\"${ip2}\" profilegroup=\"N/A\" profiletype=\"N/A\" profile=\"N/A\" proto=17 service=\"dns\" policyid=1 serial=2732 app_list=\"monitor-all\" app_type=\"network-service\" app=\"DNS\" action=pass count=1 msg=\"network-service: DNS\"",
        "date=${date} time=${time} devname=FGT60C3G10006819 device_id=FGT60C3G10006819 log_id=0211008192 type=virus subtype=infected pri=${pri} vd=\"root\" msg=\"File is infected.\" status=\"blocked\" service=\"http\" src=${ip} dst=${ip2} sport=${port} src_port=${port} dport=${port2} dst_port=${port2} src_int=\"internal\" dst_int=\"wan1\" policyid=1 identidx=0 serial=1467 dir=N/A file=\"eicarcom2.zip\" checksum=\"N/A\" quarskip=\"No skip\" virus=\"EICAR_TEST_FILE\" dtype=\"Virus\" ref=\"http://www.fortinet.com/ve?vid=2172\" url=\"${url}\" carrier_ep=\"N/A\" profile=\"test_av\" profiletype=\"Antivirus_Profile\" profilegroup=\"N/A\" user=\"N/A\" group=\"N/A\" agent=\"N/A\" from=\"N/A\" to=\"N/A\"",
        "date=${date} time=${time} devname=FGT60C3G10006819 device_id=FGT60C3G10006819 log_id=0102026001 type=event subtype=dhcp pri=${pri} vd=root dhcp_msg=\"Ack\" dir=Sent mac=x0:y6:z2:00:00:00 ip=${ip} lease=604800 hostname=\"Ty-Pc\" msg=\"Assigns IP address/configuration parameters to the client\""
     ]
}
