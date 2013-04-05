{
    "fields" : [
        { "templateCount" : {"count":2} },
        { "datetime": {"type": "random", "generate_type":"datetime", "format": "%b %d %H:%M:%S" } },
        { "date": {"type": "random", "generate_type":"datetime", "format": "%m/%d/%Y" } },
        { "time": {"type": "random", "generate_type":"datetime", "format": "%H:%M:%S" } },
        { "ip" : {"type": "random", "generate_type":"IPv4" } },
        { "ip2" : {"type": "from_list_file", "file" : "ip.list", "method":"random" } }
    ],
    "template" : [
          "${ip},XXX\\YYY,${date},${time},IAS,TRIST0140,25,311 1 ${ip2} ${date} ${time} 59904,27,30,4130,XXX\\YYY,4129,XXX\\YYY,4108,${ip},4116,0,4128,DNETWKS15,4154,Wireless XXX Users,4155,1,4136,11,4142,7",
          "${datetime} company.domain.com [0]:${ip},XXX/YYY,${date},${time},IAS,TRIST0140,4,${ip2},61,19,5,0,12,1400,31,0022faf5ae3a,30,0019bbfe0363,32,Wireless,4108,10.184.22.49,4116,0,4128,XNET,4154,Wireless XXX Users,4155,1,4129,XXX\\YYY,4130,XXX\\YYY,25,311 1 ${ip2} ${date} ${time} 167722,4136,1,4142,0"
    ]
}
