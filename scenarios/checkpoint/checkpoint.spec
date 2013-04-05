{
    "fields" : [
        { "templateCount" : {"count":2} },
        { "url" : {"type": "from_list_file", "file" : "url.list", "method":"sequential" } },
        { "date": {"type": "random", "generate_type":"datetime", "format": "%d%b%Y %H:%M:%S" } },
        { "ip" : {"type": "from_list_file", "file" : "ip.list", "method":"random" } },
        { "port" : {"type": "random", "generate_type":"integer", "min":1, "max":10000 } }
    ],
    "template" : [
          "loc=780573|filename=fw.log|fileid=1358459940|time=${date}|action=allow|orig=${ip}|orig_name=fw1|i/f_dir=outbound|i/f_name=eth2|has_accounting=0|product=URL Filtering|__policy_id_tag=product=VPN-1 & FireWall-1[db_tag={00000052-0040-004B-86F9-0BC8ACA9E733};mgmt=fw1;date=1357897393;policy_name=Standard]|user=Name Surname (name@domain.local)/n|src_user_name=Name Surname (name@domain.local)/n|src_machine_name=box@domain.local|snid=d283b405|src=${ip}|s_port=${port}|dst=${ip}|service=80|service_name=http|proto=tcp|appi_name=*** Confidential ***|app_desc=*** Confidential ***|app_id=-1093427800|app_category=*** Confidential ***|matched_category=*** Confidential ***|app_properties=*** Confidential ***|app_risk=*** Confidential ***|app_rule_id=*** Confidential ***|app_rule_name=*** Confidential ***|proxy_src_ip=10.1.4.103|bytes=40821|sent_bytes=3366|received_bytes=37455|Suppressed logs=54|Referrer_self_uid=*** Confidential ***|ICMP Code=hede|ICMP Type=hayda|TCP packet out of state=heyoo",
          "loc=477|filename=fw.adtlog|fileid=-1|time=${date}|action=accept|orig=${ip}|orig_name=cpmodule|i/f_dir=outbound|i/f_name=|has_accounting=0|product=SmartDashboard|ObjectName=cpmodule|ObjectType=firewall_application|ObjectTable=applications|Operation=Install Policy|Uid={000000FF-00C2-004D-B087-1E87F2B35AB9}|Administrator=admin|Machine=TestXp|Subject=Policy Installation|Audit Status=Success|Additional Info=Security Policy : Standard|Operation Number=7|client_ip=${ip}"
    ]
}