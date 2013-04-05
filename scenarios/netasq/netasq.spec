{
    "fields" : [
        { "templateCount" : {"count":3} },
        { "datetime": {"type": "random", "generate_type":"datetime", "format": "%Y-%m-%d %H:%M:%S" } },
        { "pri" : {"type": "random", "generate_type":"integer", "min":0, "max":8 } },
        { "ip" : {"type": "random", "generate_type":"IPv4" } },
        { "ip2" : {"type": "from_list_file", "file" : "ip.list", "method":"random" } },
        { "port" : {"type": "random", "generate_type":"integer", "min":1, "max":10000 } },
        { "port2" : {"type": "random", "generate_type":"integer", "min":1, "max":5000 } },
        { "sent" : {"type": "random", "generate_type":"integer", "min":1, "max":10000 } },
        { "rcvd" : {"type": "random", "generate_type":"integer", "min":1, "max":10000 } },
        { "duration" : {"type": "random", "generate_type":"integer", "min":0, "max":20 } },
        { "duration2" : {"type": "random", "generate_type":"integer", "min":0, "max":59 } },
        { "url" : {"type": "from_list_file", "file" : "url.list", "method":"random" } },
        { "arg" : {"type": "from_list_file", "file" : "arg.list", "method":"random" } }
    ],
    "template" : [
          "id=firewall time=\"${datetime}\" fw=\"CompanyXXX\" tz=+0200 startime=\"${datetime}\" pri=${pri} proto=http contentpolicy=0 ruleid=10 op=POST result=200 user= src=${ip} srcport=${port} dst=${ip2} dstport=${port2} dstportname=http srcname=Client_Range_ADSL dstname=${url} modsrc=${ip} modsrcport=${port} origdst=${ip2} origdstport=${port2} sent=${sent} rcvd=${rcvd} duration=${duration}.${duration2} action=pass cat_site=\"{any}\" arg=\"${arg}\" logtype=\"web\"",
          "id=firewall time=\"${datetime}\" fw=\"CompanyXXX\" tz=+0200 startime=\"${datetime}\" pri=${pri} confid=01 slotlevel=2 ruleid=65 srcif=\"Ethernet1\" srcifname=\"in\" ipproto=tcp dstif=\"Ethernet0\" dstifname=\"out\" proto=https src=${ip} srcport=${port} srcportname=ephemeral_fw_tcp srcname=user_phone dst=${ip2} dstport=${port2} dstportname=https dstname=Exchange_Out action=pass logtype=\"filter\"",
          "id=firewall time=\"${datetime}\" fw=\"CompanyXXX\" tz=+0200 startime=\"${datetime}\" pri=${pri} confid=01 slotlevel=2 ruleid=68 srcif=\"Ethernet1\" srcifname=\"in\" ipproto=tcp dstif=\"Ethernet0\" dstifname=\"out\" proto=https src=${ip} srcport=${port} srcportname=ephemeral_fw_tcp srcname=Client_Range dst=${ip2} dstport=${port2} dstportname=https dstname=${url} modsrc=${ip} modsrcport=${port} origdst=${ip2} origdstport=${port2} sent=${sent} rcvd=${rcvd} duration=${duration}.${duration2} logtype=\"connection\""
    ]
}
