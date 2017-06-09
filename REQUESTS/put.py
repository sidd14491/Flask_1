import requests,json,threading,time
payloads = {
                "auth": {
                        "scope": {
                                "project": {
                                        "domain": {
                                                "id": "default"
                                        },
                                        "name": "admin"
                                }
                        },
                        "identity": {
                                "password": {
                                        "user": {
                                                "domain": {
                                                        "id": "default"
                                                },
                                                "password": "passw0rd",
                                                "name": "admin"
                                        }
                                },
                                "methods": ["password"]
                        }
                }
        }
headers = {'Content-Type': 'application/json'}
def get_auth_token(headers,payloads):
    r=requests.post("http://10.213.18.39:5000/v3/auth/tokens",headers=headers,data=json.dumps(payloads))
    op = r.headers["x-subject-token"]
    return op
out = get_auth_token(headers,payloads)
headers1= headers
head = {'Content-Type': 'application/json',"X-Auth-Token":out}
op_ref ={
        "application": {
                "app_name": "APP1",
                "definition_type": "CUSTOM",
                "parent_type": "project",

                "display_name": "APP1",
                "name": "APP1",
                "app_sig_type": "GROUP",
                "fq_name": [
                        "default-domain",
                        "default-project",
                        "APP2"
                ],
                "application_refs": [{
                                "to": [
                                        "default-domain",
                                        "default-project",
                                        "APP1"
                                ]
                        }
                ]
        }
}
def post_application(head,payloads):
        #op_ref["application"]["fq_name"][-1] = "APP_%s"%i
        #r=requests.post("http://10.213.18.39:80/shared-object/application",headers=head,data=json.dumps(payloads))
        #r=requests.put("http://10.213.18.39:80/shared-object/application",headers=head,data=json.dumps(payloads))
        #fd = open("app.txt","w+")
        #out=r.json
            for i in range(2,4):
                   op_ref["application"]["name"] = "APP_%s"%i
                   op_ref["application"]["app_name"] = "APP_%s"%i
                   op_ref["application"]["display_name"] = "APP_%s"%i
                   op_ref["application"]["fq_name"][-1] = "APP_%s"%i
                   op_ref["application"]["application_refs"][0]["to"][-1] = "APP_%s"%(i-1)
                   r=requests.post("http://10.213.18.39:80/shared-object/application",headers=head,data=json.dumps(payloads))
                   if r.reason == 'OK':
                        print r.json()
                   else:
                        print "        FAIL    "
                        print r.text
#import pdb;pdb.set_trace()
#post_application(head,op_ref)
op_ref1 ={
        "application": {
                "app_name": "APP1",
                "definition_type": "CUSTOM",
                "parent_type": "project",

                "display_name": "APP1",
                "name": "APP1",
                "app_sig_type": "GROUP",
                "fq_name": [
                        "default-domain",
                        "default-project",
                        "APP21"
                ]
        }
}
def with_one_app(head,payloads):
       r=requests.post("http://10.213.18.39:80/shared-object/application",headers=head,data=json.dumps(payloads))
       if r.content == 'Please select atleast one application signature':
           print "  Test Case Passed "
           print " Provide on application_back_ref "
       else:
           print " Test case Failed "
       print r.json()
#import pdb;pdb.set_trace()
with_one_app(head,op_ref1),
