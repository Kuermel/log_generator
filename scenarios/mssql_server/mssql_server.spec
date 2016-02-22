    {
    "fields" : [
        { "ipv4" : {"type": "random", "generate_type":"LocalIPv4" } },
        { "date": {"type": "random", "generate_type":"datetime", "format": "%d/%b/%Y:%H:%M:%S" } },
        { "es_date": {"type": "random", "generate_type":"datetime", "format": "%Y-%m-%d %H:%M:%S" } },
        { "url_category" : {"type": "from_list_file", "file" : "url_category.list", "method":"random" } },
        { "url_requesttype" : {"type": "from_list_file", "file" : "url_requesttype.list", "method":"random" } },
        { "application_name" : {"type": "from_list_file", "file" : "application_name.list", "method":"sequential" } },
        { "method" : {"type": "from_list_file", "file" : "method.list", "method":"random" } },
        { "file_offset" : {"type": "from_list_file", "file" : "file_offset.list", "method":"random" } },
        { "file_path" : {"type": "from_list_file", "file" : "file_path.list", "method":"random" } },
        { "server_name" : {"type": "from_list_file", "file" : "server_name.list", "method":"random" } },
        { "session_id" : {"type": "from_list_file", "file" : "session_id.list", "method":"random" } },
        { "sent" : {"type": "random", "generate_type":"integer", "min":1, "max":10000 } },
        { "port" : {"type": "from_list_file", "file" : "port.list", "method":"random" } },
        { "username" : {"type": "from_list_file", "file" : "username.list", "method":"random" } },
        { "database_name" : {"type": "from_list_file", "file" : "database_name.list", "method":"random" } },
        { "mssql_object_name" : {"type": "from_list_file", "file" : "mssql_object_name.list", "method":"random" } },
        { "mssql_schema_name" : {"type": "from_list_file", "file" : "mssql_schema_name.list", "method":"random" } },
        { "domain_name" : {"type": "from_list_file", "file" : "domain_name.list", "method":"random" } },
        { "recv" : {"type": "random", "generate_type":"integer", "min":1, "max":10000 } },
        { "error_date": {"type": "random", "generate_type":"datetime", "format": "%a %b %d %H:%M:%S %Y" } }
    ],
    "template" : [],
    "json_template": [
         {
             "_es_type": "nastedlog",
             "EventMap": {
                 "Type": "User",
                 "SubType": "Deny",
                 "Context": "Identity"
             },
             "Event": {
                 "Category": "LOGIN",
                 "Info": "LOGIN FAILED",
                 "SubCategory": "LOGIN"
             },
             "Source": {
                 "IP": "ipv4"
             },
             "Severity": {
                 "ID": 6,
                 "Name": "information"
             },
             "EventSource": {
                 "Category": "Relational Database",
                 "Collector": "mssql",
                 "Description": "MSSQL Server",
                 "IP": "192.168.1.155",
                 "PrefixID": 4002,
                 "Product": "MSSQL",
                 "Tag": "SQL",
                 "Type": "Database Server",
                 "Vendor": "Microsoft"
             },
             "MSSQL": {
                 "action_id": "LGIF",
                 "audit_file_offset": "file_offset",
                 "class_type": "LX",
                 "event_time": "",
                 "file_name": "file_path",
                 "sequence_number": 1,
                 "server_instance_name": "server_name",
                 "statement": "Network error code 0x6d occurred while establishing a connection; the connection has been closed. This may have been caused by client or server login timeout expiration."
             },
             "Time": {
                 "Generated": "es_date",
                 "Received": "es_date"
             }
         },
         {
             "_es_type": "nastedlog",
             "EventMap": {
                 "Type": "User",
                 "SubType": "Login",
                 "Context": "Identity"
             },
             "Event": {
                 "Category": "LOGIN",
                 "Info": "LOGIN SUCCEEDED",
                 "SubCategory": "LOGIN"
             },
             "Source": {
                 "UserName": "username"
             },
             "Severity": {
                 "ID": 6,
                 "Name": "information"
             },
             "EventSource": {
                 "Category": "Relational Database",
                 "Collector": "mssql",
                 "Description": "MSSQL Server",
                 "Tag": "SQL",
                 "IP": "192.168.1.155",
                 "PrefixID": 4002,
                 "Product": "MSSQL",
                 "Type": "Database Server",
                 "Vendor": "Microsoft"
             },
             "MSSQL": {
                 "action_id": "LGIS",
                 "audit_file_offset": "file_offset",
                 "class_type": "LX",
                 "file_name": "file_path",
                 "sequence_number": 1,
                 "server_instance_name": "server_name"
             },
             "Time": {
                 "Generated": "es_date",
                 "Received": "es_date"
             }
         },
         {
             "_es_type": "nastedlog",
             "EventMap": {
                 "Type": "User",
                 "SubType": "Logout",
                 "Context": "Identity"
             },
             "Event": {
                 "Category": "LOGIN",
                 "Info": "LOGOUT",
                 "SubCategory": "LOGIN"
             },
             "Source": {
                 "UserName": "username"
             },
             "Severity": {
                 "ID": 6,
                 "Name": "information"
             },
             "EventSource": {
                 "Category": "Relational Database",
                 "Collector": "mssql",
                 "Description": "MSSQL Server",
                 "Tag": "SQL",
                 "IP": "192.168.1.155",
                 "PrefixID": 4002,
                 "Product": "MSSQL",
                 "Type": "Database Server",
                 "Vendor": "Microsoft"
             },
             "MSSQL": {
                 "action_id": "LGO",
                 "audit_file_offset": "file_offset",
                 "class_type": "LX",
                 "file_name": "file_path",
                 "sequence_number": 1,
                 "server_instance_name": "server_name",
                 "server_principal_name": "username",
                 "succeeded": "true"
             },
             "Time": {
                 "Generated": "es_date",
                 "Received": "es_date"
             }
         },
         {
             "_es_type": "nastedlog",
             "EventMap": {
                 "Type": "Database",
                 "SubType": "Select",
                 "Context": "Object"
             },
             "Event": {
                 "Category": "OBJECT",
                 "Info": "SELECT",
                 "SubCategory": "TABLE"
             },
             "Source": {
                 "UserName": "username",
                 "Domain": "domain_name"
             },
             "Severity": {
                 "ID": 6,
                 "Name": "information"
             },
             "EventSource": {
                 "Category": "Relational Database",
                 "Collector": "mssql",
                 "Description": "MSSQL Server",
                 "IP": "192.168.1.155",
                 "PrefixID": 4002,
                 "Product": "MSSQL",
                 "Tag": "SQL",
                 "Type": "Database Server",
                 "Vendor": "Microsoft"
             },
             "MSSQL": {
                 "action_id": "SL",
                 "audit_file_offset": "file_offset",
                 "class_type": "P",
                 "database_name": "database_name",
                 "database_principal_name": "dbo",
                 "file_name": "file_path",
                 "is_column_permission": "True",
                 "object_id": 533406957,
                 "object_name": "mssql_object_name",
                 "schema_name": "dbo",
                 "server_instance_name": "server_name",
                 "server_principal_id": 269,
                 "server_principal_name": "username",
                 "sequence_number": 1,
                 "statement": "SELECT COUNT(RecordId) FROM LOGSIGN.RegisteredEmailAppeals WHERE LOGSIGN.Id = @value AND RecordId != @recId"
             },
             "Time": {
                 "Generated": "es_date",
                 "Received": "es_date"
             }
         },
         {
             "_es_type": "nastedlog",
             "EventMap": {
                 "Type": "Database",
                 "SubType": "Execute",
                 "Context": "Object"
             },
             "Event": {
                 "Category": "OBJECT",
                 "Info": "EXECUTE",
                 "SubCategory": "STORED PROCEDURE"
             },
             "Source": {
                 "UserName": "username",
                 "Domain": "domain_name"
             },
             "Severity": {
                 "ID": 6,
                 "Name": "information"
             },
             "EventSource": {
                 "Category": "Relational Database",
                 "Collector": "mssql",
                 "Description": "MSSQL Server",
                 "IP": "192.168.1.155",
                 "PrefixID": 4002,
                 "Product": "MSSQL",
                 "Tag": "SQL",
                 "Type": "Database Server",
                 "Vendor": "Microsoft"
             },
             "MSSQL": {
                 "action_id": "EX",
                 "audit_file_offset": "file_offset",
                 "class_type": "P",
                 "database_name": "database_name",
                 "database_principal_name": "dbo",
                 "file_name": "file_path",
                 "is_column_permission": "True",
                 "object_id": 702051870,
                 "object_name": "mssql_object_name",
                 "schema_name": "dbo",
                 "server_instance_name": "server_name",
                 "server_principal_id": 269,
                 "server_principal_name": "username",
                 "sequence_number": 1,
                 "succeeded": "true"
             },
             "Time": {
                 "Generated": "es_date",
                 "Received": "es_date"
             }
         },
         {
             "_es_type": "nastedlog",
             "EventMap": {
                 "Type": "Database",
                 "SubType": "Update",
                 "Context": "Object"
             },
             "Event": {
                 "Category": "OBJECT",
                 "Info": "UPDATE",
                 "SubCategory": "TABLE"
             },
             "Source": {
                 "UserName": "username",
                 "Domain": "domain_name"
             },
             "Severity": {
                 "ID": 6,
                 "Name": "information"
             },
             "EventSource": {
                 "Category": "Relational Database",
                 "Collector": "mssql",
                 "Description": "MSSQL Server",
                 "IP": "192.168.1.155",
                 "PrefixID": 4002,
                 "Product": "MSSQL",
                 "Tag": "SQL",
                 "Type": "Database Server",
                 "Vendor": "Microsoft"
             },
             "MSSQL": {
                 "action_id": "UP",
                 "audit_file_offset": "file_offset",
                 "class_type": "U",
                 "database_name": "database_name",
                 "database_principal_name": "dbo",
                 "file_name": "file_path",
                 "is_column_permission": "True",
                 "object_id": 49433108,
                 "object_name": "SALES_DATASHEET_DETAIL",
                 "schema_name": "CUSTOMER",
                 "server_instance_name": "server_name",
                 "server_principal_id": 269,
                 "server_principal_name": "username",
                 "sequence_number": 1,
                 "statement": "UPDATE CUSTOMER.SALES_DATASHEET_DETAIL SET Sales= '6000', Category='public institutions' WHERE Location = 'Turkey'"
             },
             "Time": {
                 "Generated": "es_date",
                 "Received": "es_date"
             }
         },
         {
             "_es_type": "nastedlog",
             "EventMap": {
                 "Type": "Database",
                 "SubType": "Update",
                 "Context": "Object"
             },
             "Event": {
                 "Category": "OBJECT",
                 "Info": "UPDATE",
                 "SubCategory": "TABLE"
             },
             "Source": {
                 "UserName": "username",
                 "Domain": "domain_name"
             },
             "Severity": {
                 "ID": 6,
                 "Name": "information"
             },
             "EventSource": {
                 "Category": "Relational Database",
                 "Collector": "mssql",
                 "Description": "MSSQL Server",
                 "IP": "192.168.1.155",
                 "PrefixID": 4002,
                 "Product": "MSSQL",
                 "Tag": "SQL",
                 "Type": "Database Server",
                 "Vendor": "Microsoft"
             },
             "MSSQL": {
                 "action_id": "UP",
                 "audit_file_offset": "file_offset",
                 "class_type": "U",
                 "database_name": "database_name",
                 "database_principal_name": "dbo",
                 "file_name": "file_path",
                 "is_column_permission": "True",
                 "object_id": 49433108,
                 "object_name": "FINANCE_DATA",
                 "schema_name": "INNOTIM",
                 "server_instance_name": "server_name",
                 "server_principal_id": 269,
                 "server_principal_name": "username",
                 "sequence_number": 1,
                 "statement": "UPDATE INNOTIM.FINANCE_DATA SET Payment = 10000$, Date = 'Feb-19-2016' WHERE Company_Name = 'TURKEY Logsign'"
             },
             "Time": {
                 "Generated": "es_date",
                 "Received": "es_date"
             }
         },
         {
             "_es_type": "nastedlog",
             "EventMap": {
                 "Type": "Database",
                 "SubType": "Delete",
                 "Context": "Object"
             },
             "Event": {
                 "Category": "OBJECT",
                 "Info": "DELETE",
                 "SubCategory": "TABLE"
             },
             "Source": {
                 "UserName": "username",
                 "Domain": "domain_name"
             },
             "Severity": {
                 "ID": 6,
                 "Name": "information"
             },
             "EventSource": {
                 "Category": "Relational Database",
                 "Collector": "mssql",
                 "Description": "MSSQL Server",
                 "IP": "192.168.1.155",
                 "PrefixID": 4002,
                 "Product": "MSSQL",
                 "Tag": "SQL",
                 "Type": "Database Server",
                 "Vendor": "Microsoft"
             },
             "MSSQL": {
                 "action_id": "DL",
                 "audit_file_offset": "file_offset",
                 "class_type": "U",
                 "database_name": "database_name",
                 "database_principal_name": "dbo",
                 "file_name": "file_path",
                 "is_column_permission": "True",
                 "object_id": 49433108,
                 "object_name": "Staff_Members",
                 "schema_name": "FOX",
                 "server_instance_name": "server_name",
                 "server_principal_id": 269,
                 "server_principal_name": "username",
                 "sequence_number": 1,
                 "statement": "DELETE From FOX.Staff_Members Where Joined_Date='20150210'"
             },
             "Time": {
                 "Generated": "es_date",
                 "Received": "es_date"
             }
         },
         {
             "_es_type": "nastedlog",
             "EventMap": {
                 "Type": "Database",
                 "SubType": "Delete",
                 "Context": "Object"
             },
             "Event": {
                 "Category": "OBJECT",
                 "Info": "DELETE",
                 "SubCategory": "TABLE"
             },
             "Source": {
                 "UserName": "username",
                 "Domain": "domain_name"
             },
             "Severity": {
                 "ID": 6,
                 "Name": "information"
             },
             "EventSource": {
                 "Category": "Relational Database",
                 "Collector": "mssql",
                 "Description": "MSSQL Server",
                 "IP": "192.168.1.155",
                 "PrefixID": 4002,
                 "Product": "MSSQL",
                 "Tag": "SQL",
                 "Type": "Database Server",
                 "Vendor": "Microsoft"
             },
             "MSSQL": {
                 "action_id": "DL",
                 "audit_file_offset": "file_offset",
                 "class_type": "U",
                 "database_name": "database_name",
                 "database_principal_name": "dbo",
                 "file_name": "file_path",
                 "is_column_permission": "True",
                 "object_id": 49433108,
                 "object_name": "Customer_Details",
                 "schema_name": "Logsign",
                 "server_instance_name": "server_name",
                 "server_principal_id": 271,
                 "server_principal_name": "username",
                 "sequence_number": 1,
                 "statement": "DELETE FROM Logsign.Customer_Details WHERE Store_Name IN (SELECT Store_Name FROM Countries WHERE Region_Name = 'EMEA');"
             },
             "Time": {
                 "Generated": "es_date",
                 "Received": "es_date"
             }
         },
         {
             "_es_type": "nastedlog",
             "EventMap": {
                 "Type": "Database",
                 "SubType": "Delete",
                 "Context": "Object"
             },
             "Event": {
                 "Category": "OBJECT",
                 "Info": "DELETE",
                 "SubCategory": "TABLE"
             },
             "Source": {
                 "UserName": "username",
                 "Domain": "domain_name"
             },
             "Severity": {
                 "ID": 6,
                 "Name": "information"
             },
             "EventSource": {
                 "Category": "Relational Database",
                 "Collector": "mssql",
                 "Description": "MSSQL Server",
                 "IP": "192.168.1.155",
                 "PrefixID": 4002,
                 "Product": "MSSQL",
                 "Tag": "SQL",
                 "Type": "Database Server",
                 "Vendor": "Microsoft"
             },
             "MSSQL": {
                 "action_id": "DL",
                 "audit_file_offset": "file_offset",
                 "class_type": "U",
                 "database_name": "database_name",
                 "database_principal_name": "dbo",
                 "file_name": "file_path",
                 "is_column_permission": "True",
                 "object_id": 49433108,
                 "object_name": "Companies",
                 "schema_name": "dbo",
                 "server_instance_name": "server_name",
                 "server_principal_id": 273,
                 "server_principal_name": "username",
                 "sequence_number": 1,
                 "session_server_principal_name": "username",
                 "statement": "DELETE FROM Companies WHERE (JobInfo=@P1) AND EXISTS (SELECT 'x' FROM JobInfo B WHERE ((B.FINISHING=@P2) AND (Companies.JobInfo=B.PAYMENT)))"
             },
             "Time": {
                 "Generated": "es_date",
                 "Received": "es_date"
             }
         },
         {
             "_es_type": "nastedlog",
             "EventMap": {
                 "Type": "Database",
                 "SubType": "Insert",
                 "Context": "Object"
             },
             "Event": {
                 "Category": "OBJECT",
                 "Info": "INSERT",
                 "SubCategory": "TABLE"
             },
             "Source": {
                 "UserName": "username",
                 "Domain": "domain_name"
             },
             "Severity": {
                 "ID": 6,
                 "Name": "information"
             },
             "EventSource": {
                 "Category": "Relational Database",
                 "Collector": "mssql",
                 "Description": "MSSQL Server",
                 "IP": "192.168.1.155",
                 "PrefixID": 4002,
                 "Product": "MSSQL",
                 "Tag": "SQL",
                 "Type": "Database Server",
                 "Vendor": "Microsoft"
             },
             "MSSQL": {
                 "action_id": "IN",
                 "audit_file_offset": "file_offset",
                 "class_type": "U",
                 "database_name": "database_name",
                 "database_principal_name": "dbo",
                 "file_name": "file_path",
                 "is_column_permission": "True",
                 "object_id": 49433108,
                 "object_name": "Store_Information",
                 "schema_name": "dbo",
                 "server_instance_name": "server_name",
                 "server_principal_id": 273,
                 "server_principal_name": "username",
                 "sequence_number": 1,
                 "session_server_principal_name": "username",
                 "statement": "INSERT INTO Store_Information (Store_Name, Manager_ID, Sales, Register_Date) VALUES ('San Francisco', 10, 900, 'Jan-10-2016');"
             },
             "Time": {
                 "Generated": "es_date",
                 "Received": "es_date"
             }
         },
         {
             "_es_type": "nastedlog",
             "EventMap": {
                 "Type": "Database",
                 "SubType": "Info",
                 "Context": "Object"
             },
             "Event": {
                 "Category": "OBJECT",
                 "Info": "ALTER",
                 "SubCategory": "TABLE"
             },
             "Source": {
                 "UserName": "username",
                 "Domain": "domain_name"
             },
             "Severity": {
                 "ID": 6,
                 "Name": "information"
             },
             "EventSource": {
                 "Category": "Relational Database",
                 "Collector": "mssql",
                 "Description": "MSSQL Server",
                 "IP": "192.168.1.155",
                 "PrefixID": 4002,
                 "Product": "MSSQL",
                 "Tag": "SQL",
                 "Type": "Database Server",
                 "Vendor": "Microsoft"
             },
             "MSSQL": {
                 "action_id": "AL",
                 "audit_file_offset": "file_offset",
                 "class_type": "U",
                 "database_name": "database_name",
                 "database_principal_name": "dbo",
                 "file_name": "file_path",
                 "is_column_permission": "True",
                 "object_id": 49433108,
                 "object_name": "Company_Info",
                 "schema_name": "dbo",
                 "server_instance_name": "server_name",
                 "server_principal_id": 273,
                 "server_principal_name": "username",
                 "sequence_number": 1,
                 "session_server_principal_name": "username",
                 "statement": "ALTER TABLE dbo.Company_Info RENAME COLUMN Address TO Addr;"
             },
             "Time": {
                 "Generated": "es_date",
                 "Received": "es_date"
             }
         },
         {
             "_es_type": "nastedlog",
             "EventMap": {
                 "Type": "Database",
                 "SubType": "Info",
                 "Context": "Object"
             },
             "Event": {
                 "Category": "OBJECT",
                 "Info": "ALTER",
                 "SubCategory": "TABLE"
             },
             "Source": {
                 "UserName": "username",
                 "Domain": "domain_name"
             },
             "Severity": {
                 "ID": 6,
                 "Name": "information"
             },
             "EventSource": {
                 "Category": "Relational Database",
                 "Collector": "mssql",
                 "Description": "MSSQL Server",
                 "IP": "192.168.1.155",
                 "PrefixID": 4002,
                 "Product": "MSSQL",
                 "Tag": "SQL",
                 "Type": "Database Server",
                 "Vendor": "Microsoft"
             },
             "MSSQL": {
                 "action_id": "AL",
                 "audit_file_offset": "file_offset",
                 "class_type": "U",
                 "database_name": "database_name",
                 "database_principal_name": "dbo",
                 "file_name": "file_path",
                 "is_column_permission": "True",
                 "object_id": 49433108,
                 "object_name": "Company_Info",
                 "schema_name": "dbo",
                 "server_instance_name": "server_name",
                 "server_principal_id": 273,
                 "server_principal_name": "username",
                 "sequence_number": 1,
                 "session_server_principal_name": "username",
                 "statement": "ALTER TABLE Company_Info ALTER COLUMN Address char(100);"
             },
             "Time": {
                 "Generated": "es_date",
                 "Received": "es_date"
             }
         },
         {
             "_es_type": "nastedlog",
             "EventMap": {
                 "Type": "Database",
                 "SubType": "Create",
                 "Context": "Object"
             },
             "Event": {
                 "Category": "OBJECT",
                 "Info": "CREATE",
                 "SubCategory": "TABLE"
             },
             "Source": {
                 "UserName": "username",
                 "Domain": "domain_name"
             },
             "Severity": {
                 "ID": 6,
                 "Name": "information"
             },
             "EventSource": {
                 "Category": "Relational Database",
                 "Collector": "mssql",
                 "Description": "MSSQL Server",
                 "IP": "192.168.1.155",
                 "PrefixID": 4002,
                 "Product": "MSSQL",
                 "Tag": "SQL",
                 "Type": "Database Server",
                 "Vendor": "Microsoft"
             },
             "MSSQL": {
                 "action_id": "CR",
                 "audit_file_offset": "file_offset",
                 "class_type": "U",
                 "database_name": "database_name",
                 "database_principal_name": "dbo",
                 "file_name": "file_path",
                 "is_column_permission": "True",
                 "object_id": 49433108,
                 "object_name": "Company_Info",
                 "schema_name": "dbo",
                 "server_instance_name": "server_name",
                 "server_principal_id": 273,
                 "server_principal_name": "username",
                 "sequence_number": 1,
                 "session_server_principal_name": "username",
                 "statement": "CREATE TABLE customers ( customer_id int NOT NULL, customer_name char(50) NOT NULL, address char(50), city char(50), state char(25), zip_code char(10), CONSTRAINT customers_pk PRIMARY KEY (customer_id));"
             },
             "Time": {
                 "Generated": "es_date",
                 "Received": "es_date"
             }
         }
     ]
}
