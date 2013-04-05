{
    "fields" : [
        { "templateCount" : {"count":1 } },
        { "date": {"type": "random", "generate_type":"datetime", "format": "%Y-%m-%d" } },
        { "time": {"type": "random", "generate_type":"datetime", "format": "%H:%S:%M" } },
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
        "date=${date},time=${time},devname=XXX,device_id=FG224B3907501199,log_id=0315013317,type=webfilter,subtype=urlfilter,pri=notice,vd=\"root\",policyid=86,intf_policyid=0,identidx=1,serial=62551133,user=\"XXXYYYZZZ\",group=\"internet_staff\",src=${ip},sport=${port},src_port=${port},src_int=\"port26\",dst=${ip2},dport=${port2},dst_port=${port2},dst_int=\"port20\",service=\"http\",hostname=\"${url}\",carrier_ep=\"N/A\",profiletype=\"Webfilter_Profile\",profilegroup=\"N/A\",profile=\"Staff_Koruma\",status=\"passthrough\",req_type=\"referral\",url=\"/pagead/imgad?id=CICAgIDQ8fyNwgEQsgIY_wEyCGI6EeDZ4Hk3\",sent=${sent},rcvd=${rcvd},msg=\"URL has been visited\",method=domain,class=0,class_desc=\"N/A\",cat=17,cat_desc=\"Advertising\""
     ]
}
