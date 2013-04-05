{
    "fields" : [
        { "templateCount" : {"count":5} },
        { "datetime": {"type": "random", "generate_type":"datetime", "format": "%b %d %H:%M:%S" } },
        { "port" : {"type": "random", "generate_type":"integer", "min":1, "max":10000 } },
        { "port2" : {"type": "random", "generate_type":"integer", "min":1, "max":5000 } },
        { "ip" : {"type": "random", "generate_type":"IPv4" } },
        { "ip2" : {"type": "from_list_file", "file" : "ip.list", "method":"random" } }
    ],
    "template" : [
          "${datetime} MikroTik forward: in:LAN out:INTERNET, src-mac 0x:y9:t3:z0:xx:yy, proto TCP (ACK), ${ip}:${port}->${ip2}:${port2}, len 80",
          "${datetime} MikroTik forward: in:Efl out:INTERNET_ULAK, proto TCP (ACK), ${ip}:${port}->${ip2}:${port2}, len 40",
          "${datetime} MikroTik hs-WIFI: static host ${ip} removed: idle timeout",
          "${datetime} MikroTik login failure for user root from ${ip} via ssh",
          "${datetime} MikroTik user admin logged in from ${ip} via winbox"
    ]
}
