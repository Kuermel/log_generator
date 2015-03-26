{
    "fields" : [
        { "templateCount" : {"count":2 } },
        { "date": {"type": "random", "generate_type":"datetime", "format": "%Y-%m-%d" } },
        { "time": {"type": "random", "generate_type":"datetime", "format": "%H:%M:%S" } },
        { "url" : {"type": "from_list_file", "file" : "url.list", "method":"sequential" } },
        { "ip" : {"type": "from_list_file", "file" : "ip.list", "method":"random" } },
        { "ip2" : {"type": "random", "generate_type":"IPv4" } },
        { "port" : {"type": "random", "generate_type":"integer", "min":1, "max":10000 } },
        { "port2" : {"type": "random", "generate_type":"integer", "min":1, "max":5000 } },
        { "pri" : {"type": "from_list_file", "file" : "pri.list", "method":"random" } },
        { "sent" : {"type": "random", "generate_type":"integer", "min":1, "max":10000 } },
        { "rcvd" : {"type": "random", "generate_type":"integer", "min":1, "max":10000 } }
    ],
    "template" : [
        "date=${date},time=${time},devname=XXX,device_id=FG224B3907501199,log_id=0315013317,type=webfilter,subtype=urlfilter,pri=notice,vd=\"root\",policyid=86,intf_policyid=0,identidx=1,serial=62551133,user=\"XXXYYYZZZ\",group=\"internet_staff\",src=${ip},sport=${port},src_port=${port},src_int=\"port26\",dst=${ip2},dport=${port2},dst_port=${port2},dst_int=\"port20\",service=\"http\",hostname=\"${url}\",carrier_ep=\"N/A\",profiletype=\"Webfilter_Profile\",profilegroup=\"N/A\",profile=\"Staff_Koruma\",status=\"passthrough\",req_type=\"referral\",url=\"/pagead/imgad?id=CICAgIDQ8fyNwgEQsgIY_wEyCGI6EeDZ4Hk3\",sent=${sent},rcvd=${rcvd},msg=\"URL has been visited\",method=domain,class=0,class_desc=\"N/A\",cat=17,cat_desc=\"Advertising\"",
        "date=${date} time=${time} devname=FGT60C3G10006819 device_id=FGT60C3G10006819 log_id=0211008192 type=virus subtype=infected pri=warning vd=\"root\" msg=\"File is infected.\" status=\"blocked\" service=\"http\" src=${ip} dst=${ip} sport=${port} src_port=${port} dport=${port} dst_port=${port} src_int=\"internal\" dst_int=\"wan1\" policyid=1 identidx=0 serial=1467 dir=N/A file=\"eicarcom2.zip\" checksum=\"N/A\" quarskip=\"No skip\" virus=\"EICAR_TEST_FILE\" dtype=\"Virus\" ref=\"http://www.fortinet.com/ve?vid=2172\" url=\"http://www.eicar.org/download/eicarcom2.zip\" carrier_ep=\"N/A\" profile=\"test_av\" profiletype=\"Antivirus_Profile\" profilegroup=\"N/A\" user=\"N/A\" group=\"N/A\" agent=\"N/A\" from=\"N/A\" to=\"N/A\""
     ]
}
