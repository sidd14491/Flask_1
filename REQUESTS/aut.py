import requests
op  = requests.get("http://10.213.5.78:80/shared-object/address")
if  op.text == "Authentication required":
    print "yes"
