{
    "fields" : [
            { "templateCount" : {"count":4} },
            { "date": {"type": "random", "generate_type":"datetime", "format": "%m/%d/%Y:%H:%M:%S" } },
            { "ip" : {"type": "from_list_file", "file" : "ip.list", "method":"random" } },
            { "ip2" : {"type": "random", "generate_type":"IPv4" } },
            { "port" : {"type": "random", "generate_type":"integer", "min":1, "max":10000 } },
            { "port2" : {"type": "random", "generate_type":"integer", "min":1, "max":5000 } },
            { "number" : {"type": "random", "generate_type":"integer", "min":1, "max":1000 } }
    ],
    "template" : [
          "${date} GMT GroupName PPE-0 : SSLLOG SSL_HANDSHAKE_SUCCESS 6773 :  SPCBId 2232689 - ClientIP ${ip} - ClientPort ${port} - VserverServiceIP ${ip2} - VserverServicePort ${port2} - ClientVersion TLSv1.0 - CipherSuite \"RC4-MD5 TLSv1 Non-Export 128-bit\" - Session New",
          "${date} GMT NSCT PPE-0 : TCP CONN_TERMINATE 7104216 :  Source ${ip}:${port} - Destination ${ip2}:${port2} - Start Time ${date} GMT - End Time ${date} GMT - Total_bytes_send ${number} - Total_bytes_recv ${number}",
          "${date} GMT NSCT PPE-0 : TCP CONN_DELINK 7104217 :  Source ${ip}:${port} - Vserver ${ip2}:${port2} - NatIP ${ip}:${port} - Destination ${ip2}:${port2} - Delink Time ${date} GMT - Total_bytes_send ${number} - Total_bytes_recv ${number}",
          "${date} GMT NSCT PPE-0 : UI CMD_EXECUTED 8539403 :  User nsroot  - Remote_ip ${ip} - Command \"stat protocol tcp\" - Status \"Success\""
    ]
}