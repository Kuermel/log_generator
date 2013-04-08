{
    "fields" : [
        { "templateCount" : {"count":15 } },
        { "ip" : {"type": "random", "generate_type":"IPv4" } },
        { "ip2" : {"type": "from_list_file", "file" : "ip.list", "method":"random" } },
        { "date": {"type": "random", "generate_type":"datetime", "format": "%Y-%m-%d %H:%S:%M" } },
        { "url" : {"type": "from_list_file", "file" : "url.list", "method":"sequential" } },
        { "protocol" : {"type": "from_list_file", "file" : "protocol.list", "method":"random" } },
        { "src" : {"type": "from_list_file", "file" : "ip.list", "method":"random" } },
        { "port" : {"type": "random", "generate_type":"integer", "min":1, "max":10000 } },
        { "port2" : {"type": "random", "generate_type":"integer", "min":1, "max":5000 } },
        { "sent" : {"type": "random", "generate_type":"integer", "min":1, "max":10000 } },
        { "rcvd" : {"type": "random", "generate_type":"integer", "min":1, "max":10000 } },
        { "pri" : {"type": "random", "generate_type":"integer", "min":0, "max":8 } },
        { "m" : {"type": "from_list_file", "file" : "m.list", "method":"random" } }
    ],
    "template" : [
      "id=firewall sn=C0EAE41C0ECC time=\"${date}\" fw=${ip} pri=${pri} c=0 m=1154  msg=\"Application Control Detection Alert: PROTOCOLS HTTP -- GET\" sid=5147 appcat=PROTOCOLS appid=1277   n=118712 src=${ip}:${port}:X0: dst=${ip2}:${port2}:X1: ",
      "id=firewall sn=C0EAE41C0ECC time=\"${date}\" fw=${ip} pri=${pri} c=1024 m=97 n=12902 src=${ip}:${port}:X0: dst=${ip2}:${port2}:X1: proto=tcp/http op=GET sent=${sent} rcvd=${rcvd} result=0 dstname=${url}  code=29 Category=\"Search Engines and Portals\" ",
      "id=firewall sn=C0EAE41C0ECC time=\"${date}\" fw=${ip} pri=${pri} c=1024 m=97 sess=Web n=13023 usr=\"admin\" src=${ip}:${port}:X0: dst=${ip2}:${port2}:X1: proto=tcp/http op=GET sent=${sent} rcvd=${rcvd} result=0 dstname=torrentleech.org arg=/templates/tl_default/images/memberback.png  code=22 Category=\"Games\" ",
      "id=firewall sn=C0EAE41C0ECC time=\"${date}\" fw=${ip} pri=${pri} c=262144 m=98 msg=\"Connection Opened\" sess=Web n=34293 usr=\"admin\" src=${ip}:${port}:X0: dst=${ip2}:${port2}:X1: proto=tcp/http   ",
      "id=firewall sn=C0EAE41C0ECC time=\"${date}\" fw=${ip} pri=${pri} c=512 m=598 msg=\"ICMP packet from LAN allowed\" n=5373 src=${ip}:${port}:X0: dst=${ip2}:${port2}:X0: type=8 code=0 ",
      "id=firewall sn=C0EAE41C0ECC time=\"${date}\" fw=${ip} pri=${pri} c=1024 m=537 msg=\"Connection Closed\" f=15 n=38632 src=${ip}:${port}:X0: dst=${ip2}:${port2}:X0: proto=udp/netbios-ns sent=${sent}   ",
      "id=firewall sn=C0EAE41C0ECC time=\"${date}\" fw=${ip} pri=${pri} c=512 m=888 msg=\"TCP packet received on non-existent/closed connection; TCP packet dropped\" n=1683 src=${ip}:${port}:X1: dst=${ip2}:${port2}:X1: note=\"TCP Flag(s): ACK\"",
      "id=firewall sn=C0EAE41C0ECC time=\"${date}\" fw=${ip} pri=${pri} c=512 m=181 msg=\"TCP FIN packet dropped \" n=99 src=${ip2}:${port}:X1: dst=${ip2}:${port2}:X1: ",
      "id=firewall sn=C0EAE41C0ECC time=\"${date}\" fw=${ip} pri=${pri} c=512 m=713 msg=\"TCP connection abort received; TCP connection dropped\" n=2170 src=${ip}:${port}:X0: dst=${ip2}:${port2}:X1: note=\"TCP Flag(s): RST\" ",
      "id=firewall sn=C0EAE41C0ECC time=\"${date}\" fw=${ip} pri=${pri} c=512 m=46 msg=\"Broadcast packet dropped\" n=2977 src=${ip}:${port}:X0: dst=${ip2}:${port2}:: proto=udp/netbios-ns ",
      "id=firewall sn=C0EAE41C0ECC time=\"${date}\" fw=${ip} pri=${pri} c=512 m=602 msg=\"DNS packet allowed\" n=18282 src=${ip}:${port}:X1: dst=${ip2}:${port2}:X0: proto=udp/51825  ",
      "id=firewall sn=C0EAE41C0ECC time=\"${date}\" fw=${ip} pri=${pri} c=6144 m=174 msg=\"UDP packet from LAN dropped\" n=1977 src=${ip}:${port}:X0: dst=${ip2}:${port2}:X0: proto=0 ",
      "id=firewall sn=C0EAE41C0ECC time=\"${date}\" fw=${ip} pri=${pri} c=10240 m=175 msg=\"ICMP packet from LAN dropped\" n=3866 src=${ip}:${port}:X0: dst=${ip2}:${port2}:X0: type=3 code=3 ",
      "id=firewall sn=C0EAE41C0ECC time=\"${date}\" fw=${ip} pri=${pri} c=256 m=38 msg=\"ICMP packet dropped due to policy\" n=2502 src=${ip}:${port}:X1: dst=${ip2}:${port2}:X1:  type=3 code=3  ",
      "id=firewall sn=C0EAE41C0ECC time=\"${date}\" fw=${ip} pri=${pri} c=64 m=36 msg=\"TCP connection dropped\" n=7971 src=${ip}:${port}:X1: dst=${ip2}:${port2}:X1: proto=tcp/6881  "
     ]
}
