#
# Copyright (c) Innotim Yazilim Telekomunikasyon ve Danismanlik Ticaret LTD. STI.
# All rights reserved.
#
__author__ = 'Ozan Turksever (ozan.turksever@logsign.net)'
__copyright__ = 'Copyright (c) 2012 Innotim Yazilim Ltd.'
__license__ = 'GPLv2'
__version__ = '0.0.1'

import os
import re
import shutil

USER_AGENT_CONTENT = "Mozilla\nIE8\n"

URL_LIST_CONTENT = "http://www.logsign.net\nhttp://www.yahoo.com\n"

SENARIO_SPEC_1 = """
{
    "fields" : [
        { "date": {"type": "random", "generate_type":"datetime", "format": "%Y/%m/%d %H:%S:%M" } },
        { "src" : {"type": "random", "generate_type":"IPv4" } },
        { "dst" : {"type": "random", "generate_type":"IPv4" } },
        { "url" : {"type": "from_list_file", "file" : "url.list", "method":"sequential" } },
        { "user_agent" : {"type": "from_list_file", "file" : "user_agent.list", "method":"random" } },
        { "respond_code" : {"type": "from_list_file", "file": "respond_codes.list", "method":"ratio", "ratio":"50,50" } },
        { "sent" : {"type": "random", "generate_type":"integer", "min":1, "max":1000 } },
        { "recv" : {"type": "random", "generate_type":"integer", "min":1, "max":1000000 } }
    ],
    "template" : "date=\\"${date}\\" src=\\"${src}\\" dst=\\"${dst}\\" recv=\\"${recv}\\" sent=\\"${sent}\\" user_agent=\\"${user_agent}\\" respond_code=\\"${respond_code}\\"",
    "output" : [ {"method":"syslog", "host":"1.1.1.1"},{ "method":"file","file":"out.log"} ]
}
        """

SCENARIO1 = 'scenario1'
SCENARIO2 = 'scenario2'

def setupScenario(name, data_dir, spec):
    if os.path.exists(data_dir):
        shutil.rmtree(data_dir)
    os.makedirs(data_dir)
    spec_file = open(data_dir+'/'+name+'.spec',"w")
    spec_file.write(spec)
    spec_file.close()

    url_file = open(data_dir+'/url.list',"w")
    url_file.write(URL_LIST_CONTENT)
    url_file.close()

    url_file = open(data_dir+'/user_agent.list',"w")
    url_file.write(USER_AGENT_CONTENT)
    url_file.close()

    url_file = open(data_dir+'/respond_codes.list',"w")
    url_file.write("200\n404\n")
    url_file.close()


# borrowed from: http://stackoverflow.com/questions/319279/how-to-validate-ip-address-in-python
def is_valid_ipv4(ip):
    """Validates IPv4 addresses.
    """
    pattern = re.compile(r"""
        ^
        (?:
          # Dotted variants:
          (?:
            # Decimal 1-255 (no leading 0's)
            [3-9]\d?|2(?:5[0-5]|[0-4]?\d)?|1\d{0,2}
          |
            0x0*[0-9a-f]{1,2}  # Hexadecimal 0x0 - 0xFF (possible leading 0's)
          |
            0+[1-3]?[0-7]{0,2} # Octal 0 - 0377 (possible leading 0's)
          )
          (?:                  # Repeat 0-3 times, separated by a dot
            \.
            (?:
              [3-9]\d?|2(?:5[0-5]|[0-4]?\d)?|1\d{0,2}
            |
              0x0*[0-9a-f]{1,2}
            |
              0+[1-3]?[0-7]{0,2}
            )
          ){0,3}
        |
          0x0*[0-9a-f]{1,8}    # Hexadecimal notation, 0x0 - 0xffffffff
        |
          0+[0-3]?[0-7]{0,10}  # Octal notation, 0 - 037777777777
        |
          # Decimal notation, 1-4294967295:
          429496729[0-5]|42949672[0-8]\d|4294967[01]\d\d|429496[0-6]\d{3}|
          42949[0-5]\d{4}|4294[0-8]\d{5}|429[0-3]\d{6}|42[0-8]\d{7}|
          4[01]\d{8}|[1-3]\d{0,9}|[4-9]\d{0,8}
        )
        $
    """, re.VERBOSE | re.IGNORECASE)
    return pattern.match(ip) is not None
