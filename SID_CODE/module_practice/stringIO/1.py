import StringIO
message = "Hi Sid How are You"
file = StringIO.StringIO(message)
print file.getvalue()
