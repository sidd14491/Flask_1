import requests,json,threading
from multiprocessing import Process
op={
	"address": {
		"fq_name": [
			"default-domain",
			"default-project",
			"IP_1"
		],
		"description": "Custom any - ipv4 address ",
		"addr_name": "Any-NEW-IP",
		"definition_type": "CUSTOM",
		"display_name": "Any-NEW-IP",
		"address_type": "ANY_IPV4",
		"name": "Any-NEW-IP"
	}
}
op1 = {
  "address": {
    "fq_name": [
      "default-domain",
      "default-project",
      "IP_58"
    ],
    "addr_name": "Any-NEW-IP",
    "definition_type": "CUSTOM",
    "display_name": "Any-NEW-IP",
    "address_type": "ANY_IPV4",
    "name": "IP_58",
    "address_refs": [{
                                "to": [
                                        "default-domain",
                                        "default-project",
                                        "IP_1"
                                ]
                },
                {
                                "to": [
                                        "default-domain",
                                        "default-project",
                                        "IP_2"
                                ]
                },
                {
                                "to": [
                                        "default-domain",
                                        "default-project",
                                        "IP_3"
                                ]
                },
                {
                                "to": [
                                        "default-domain",
                                        "default-project",
                                        "IP_4"
                                ]
                },
                {
                                "to": [
                                        "default-domain",
                                        "default-project",
                                        "IP_5"
                                ]
                }

                ]
  }
}
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
headers = {'Content-Type': 'application/json'
           }
def get_auth_token(headers,payloads):
    r=requests.post("http://10.213.18.39:5000/v3/auth/tokens",headers=headers,data=json.dumps(payloads))
    op = r.headers["x-subject-token"]
    return op
out = get_auth_token(headers,payloads)
#headers1= headers
head = {'Content-Type': 'application/json',"X-Auth-Token":out}

def post_address(head,addr):
       if   threading.currentThread().getName()  == "Thread-1":
            print threading.currentThread().getName()
            for i in range(15,10000):
                   op["address"]["fq_name"][-1] = "IP_%s"%i 
                   r=requests.post("http://10.213.18.39:80/shared-object/address",headers=head,data=json.dumps(addr))
       elif   threading.currentThread().getName()  == "Thread-2":
            print threading.currentThread().getName()
            for i in range(10000,20000):
                   op["address"]["fq_name"][-1] = "IP_%s"%i 
                   r=requests.post("http://10.213.18.39:80/shared-object/address",headers=head,data=json.dumps(addr))
       elif   threading.currentThread().getName()  == "Thread-3":
            print threading.currentThread().getName()
            for i in range(20000,30000):
                   op["address"]["fq_name"][-1] = "IP_%s"%i 
                   r=requests.post("http://10.213.18.39:80/shared-object/address",headers=head,data=json.dumps(addr))
       elif   threading.currentThread().getName()  == "Thread-4":
            print threading.currentThread().getName()
            for i in range(30000,40000):
                   op["address"]["fq_name"][-1] = "IP_%s"%i 
                   r=requests.post("http://10.213.18.39:80/shared-object/address",headers=head,data=json.dumps(addr))
       elif   threading.currentThread().getName()  == "Thread-5":
            print threading.currentThread().getName()
            for i in range(40000,50000):
                   op["address"]["fq_name"][-1] = "IP_%s"%i 
                   r=requests.post("http://10.213.18.39:80/shared-object/address",headers=head,data=json.dumps(addr))
       elif   threading.currentThread().getName()  == "Thread-6":
            print threading.currentThread().getName()
            for i in range(50000,60000):
                   op["address"]["fq_name"][-1] = "IP_%s"%i 
                   r=requests.post("http://10.213.18.39:80/shared-object/address",headers=head,data=json.dumps(addr))
       elif   threading.currentThread().getName()  == "Thread-7":
            print threading.currentThread().getName()
            for i in range(60000,70000):
                   op["address"]["fq_name"][-1] = "IP_%s"%i 
                   r=requests.post("http://10.213.18.39:80/shared-object/address",headers=head,data=json.dumps(addr))
       elif   threading.currentThread().getName()  == "Thread-8":
            print threading.currentThread().getName()
            for i in range(70000,80000):
                   op["address"]["fq_name"][-1] = "IP_%s"%i 
                   r=requests.post("http://10.213.18.39:80/shared-object/address",headers=head,data=json.dumps(addr))
       elif   threading.currentThread().getName()  == "Thread-9":
            print threading.currentThread().getName()
            for i in range(80000,90000):
                   op["address"]["fq_name"][-1] = "IP_%s"%i 
                   r=requests.post("http://10.213.18.39:80/shared-object/address",headers=head,data=json.dumps(addr))
       elif   threading.currentThread().getName()  == "Thread-10":
            print threading.currentThread().getName()
            for i in range(90000,100000):
                   op["address"]["fq_name"][-1] = "IP_%s"%i 
                   r=requests.post("http://10.213.18.39:80/shared-object/address",headers=head,data=json.dumps(addr))

def get_application(head):
                 r=requests.get("http://10.213.18.39:80/shared-object/address?size=10000",headers=head)
                 obj_uuid = []
                 out = r.json()
                 #print out
                 out1 = out["address"]
                 op = out['total']
                 print threading.currentThread().getName(), 'Starting'
                 #time.sleep(2)
                 for i in range(len(out["address"])):
                        if "IP_" in out1[i]["fq_name"][-1]:
                              print "%s::::::::::::::::::%s"%(out1[i]["fq_name"][-1],out1[i]["uuid"])
                              obj_uuid.append(str(out1[i]["uuid"]))

                 return obj_uuid
#uuid = get_application(head)
#print len(uuid)
def put_address(head,uuid,data1):
    for i in range(len(uuid)):
        op = "http://10.213.18.39:80/shared-object/address/%s"%(uuid[i])
        r=requests.get(op,headers=head)
        out = r.json()
        op1["address"]["fq_name"][-1] = out["address"]["fq_name"][-1]
        print op1
        if out["address"]["fq_name"][-1] == "IP_1" or out["address"]["fq_name"][-1] == "IP_2" or out["address"]["fq_name"][-1] == "IP_3" or out["address"]["fq_name"][-1] == "IP_4" or out["address"]["fq_name"][-1] == "IP_5" :
                     pass   
        else:
                 r=requests.put(op,headers=head,data=json.dumps(data1))
                 print r.text
import pdb;pdb.set_trace()
#put_address(head,uuid,op1)
#post_address1(head,op1)

#import pdb;pdb.set_trace()

threads = []
for i in range(10):

     p1 = threading.Thread(target = post_address,args=(head,op))
     threads.append(p1)
     p1.start()
