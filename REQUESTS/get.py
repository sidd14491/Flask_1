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
headers = {'Content-Type': 'application/json'
           }
op = {
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
			"APP210"
		]
	}
}
delete = {
	"input": {
		"shared_object_info":{
		"object_type":"ADDRESS",
		 "object_uuids":[]	
	}   
}
}

############################################
#Comment :::  GENERATE AUTH-TOKEN
#  API
#############################################
#import pdb;pdb.set_trace()
def get_auth_token(headers,payloads):
    r=requests.post("http://10.213.18.39:5000/v3/auth/tokens",headers=headers,data=json.dumps(payloads))
    op = r.headers["x-subject-token"]
    return op
out = get_auth_token(headers,payloads)
headers1= headers
head = {'Content-Type': 'application/json',"X-Auth-Token":out}

############################################
#Comment :::  CREATE application
#  API
#############################################
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
			},
			{
				"to": [
					"default-domain",
					"default-project",
					"APP2"
				]
			},
			{
				"to": [
					"default-domain",
					"default-project",
					"APP3"
				]
			},
			{
				"to": [
					"default-domain",
					"default-project",
					"APP4"
				]
			},
			{
				"to": [
					"default-domain",
					"default-project",
					"APP5"
				]
			}
		]
	}
}
def put_application(head,uuid,data1):
    for i in range(len(uuid)):
        op = "http://10.213.18.39:80/shared-object/application/%s"%(uuid[i])
        r=requests.get(op,headers=head)
        out = r.json()
        op1["application"]["fq_name"][-1] = out["application"]["fq_name"][-1]
        print op1
        if out["application"]["fq_name"][-1] == "APP_1" or out["application"]["fq_name"][-1] == "APP_2" or out["application"]["fq_name"][-1] == "APP_3" or out["application"]["fq_name"][-1] == "APP_4" or out["application"]["fq_name"][-1] == "APP_5" :
                     pass
        else:
                 r=requests.put(op,headers=head,data=json.dumps(data1))
                 print r.text
#put_application()
#import pdb;pdb.set_trace()
fd = open("app.txt","w+")
def post_application(head,payloads):
    for i in range(5,300):
        #op_ref["application"]["fq_name"][-1] = "APP_%s"%i 
        #r=requests.post("http://10.213.18.39:80/shared-object/application",headers=head,data=json.dumps(payloads))
        #r=requests.put("http://10.213.18.39:80/shared-object/application",headers=head,data=json.dumps(payloads))
        #fd = open("app.txt","w+")
        #out=r.json
       if   threading.currentThread().getName()  == "Thread-1":
            print threading.currentThread().getName()
            for i in range(1,10000):
                   op["application"]["fq_name"][-1] = "APP_%s"%i
                   r=requests.post("http://10.213.18.39:80/shared-object/application",headers=head,data=json.dumps(payloads))
       elif   threading.currentThread().getName()  == "Thread-2":
            print threading.currentThread().getName()
            for i in range(10000,20000):
                   op["application"]["fq_name"][-1] = "APP_%s"%i
                   r=requests.post("http://10.213.18.39:80/shared-object/application",headers=head,data=json.dumps(payloads))
       elif   threading.currentThread().getName()  == "Thread-3":
            print threading.currentThread().getName()
            for i in range(20000,30000):
                   op["application"]["fq_name"][-1] = "APP_%s"%i
                   r=requests.post("http://10.213.18.39:80/shared-object/application",headers=head,data=json.dumps(payloads))
       elif   threading.currentThread().getName()  == "Thread-4":
            print threading.currentThread().getName()
            for i in range(30000,40000):
                   op["application"]["fq_name"][-1] = "APP_%s"%i
                   r=requests.post("http://10.213.18.39:80/shared-object/application",headers=head,data=json.dumps(payloads))
       elif   threading.currentThread().getName()  == "Thread-5":
            print threading.currentThread().getName()
            for i in range(40000,50000):
                   op["application"]["fq_name"][-1] = "APP_%s"%i
                   r=requests.post("http://10.213.18.39:80/shared-object/application",headers=head,data=json.dumps(payloads))
        #fd.write("%s:::::::%s#############\n"%(i,out))
#post_applicatio(head,op_ref)
#import pdb;pdb.set_trace()
#threads = []
#for i in range(5):
#
#     p1 = threading.Thread(target = post_application,args=(head,op))
#     threads.append(p1)
#     p1.start()
#fp = open("app1.txt","w+")
############################################
#Comment :::  Get application by uuid
#  API
#############################################
def get_application(head,option=""):
        #fp.write("%s"%out)
        obj_uuid = []
        obj_uuid2 = []
        obj_uuid3 = []
        obj_uuid4 = []
        obj_uuid5 = []
        obj_uuid6 = []
        obj_uuid7= []
        obj_uuid8 = []
        obj_uuid9 = []
        if option == "Application":
                 r=requests.get("http://10.213.18.39:80/shared-object/application?size=10000",headers=head)
                 #r=requests.get("http://10.213.18.39:80/shared-object/application?range:gte=40000&lte=12100",headers=head)
                 out = r.json()
                 print len(out["application"])
                 out1 = out["application"]
                 op = out['total']
                 for i in range(len(out["application"])):
                     if out1[i]["fq_name"][-1] == "APP_1" or out1[i]["fq_name"][-1] == "APP_2" or out1[i]["fq_name"][-1] == "APP_3" or out1[i]["fq_name"][-1] == "APP_4" or out1[i]["fq_name"][-1] == "APP_5":
                            pass
                     elif  out1[i]["fq_name"][-1].startswith("APP_"):
                              print "%s::::::::::::::::::%s"%(out1[i]["fq_name"][-1],out1[i]["uuid"])
                              obj_uuid.append(str(out1[i]["uuid"]))
        elif option == "Address":
              
                 #r=requests.get("http://10.213.18.39:80/shared-object/address?size=10000",headers=head)
                 r=requests.get("http://10.213.18.39:80/shared-object/address?q=fq_name:IP_1*&size=10000",headers=head)
                 r2=requests.get("http://10.213.18.39:80/shared-object/address?q=fq_name:IP_2*&size=10000",headers=head)
                 r3=requests.get("http://10.213.18.39:80/shared-object/address?q=fq_name:IP_3*&size=10000",headers=head)
                 r4=requests.get("http://10.213.18.39:80/shared-object/address?q=fq_name:IP_4*&size=10000",headers=head)
                 r5=requests.get("http://10.213.18.39:80/shared-object/address?q=fq_name:IP_5*&size=10000",headers=head)
                 r6=requests.get("http://10.213.18.39:80/shared-object/address?q=fq_name:IP_6*&size=10000",headers=head)
                 r7=requests.get("http://10.213.18.39:80/shared-object/address?q=fq_name:IP_7*&size=10000",headers=head)
                 r8=requests.get("http://10.213.18.39:80/shared-object/address?q=fq_name:IP_8*&size=10000",headers=head)
                 r9=requests.get("http://10.213.18.39:80/shared-object/address?q=fq_name:IP_9*&size=10000",headers=head)
                 #r5=requests.get("http://10.213.18.39:80/shared-object/address?q=fq_name:IP_8*&size=10000",headers=head)
                 out,out2,out3,out4,out5,out6,out7,out8,out9 = r.json(),r2.json(),r3.json(),r4.json(),r5.json(),r6.json(),r7.json(),r8.json(),r9.json()
                 #out = r.json()
                 #print out
                 out1,out21,out31,out41,out51,out61,out71,out81,out91 = out["address"], out2["address"], out3["address"],out4["address"], out5["address"],out6["address"], out7["address"],out8["address"], out9["address"]
                 #out1 = out["address"]
                 #op = out['total']
                 #print threading.currentThread().getName(), 'Starting'
                 #time.sleep(2)
              
              #if   threading.currentThread().getName()  == "Thread-1":
              #   r=requests.get("http://10.213.18.39:80/shared-object/address?q=fq_name:IP_1*&size=10000",headers=head)
              #   out = r.json()
              #   out1 = out["address"]
                 for i in range(len(out["address"])):
                        if "IP_" in out1[i]["fq_name"][-1]:
                              print "%s::::::::::::::::::%s"%(out1[i]["fq_name"][-1],out1[i]["uuid"])
                              obj_uuid.append(str(out1[i]["uuid"]))
              #elif   threading.currentThread().getName()  == "Thread-2":    
              #   r2=requests.get("http://10.213.18.39:80/shared-object/address?q=fq_name:IP_2*&size=10000",headers=head)
              #   out2 = r2.json()
              #   out21 = out2["address"]
                 for i in range(len(out2["address"])):
                        if "IP_" in out21[i]["fq_name"][-1]:
                              print "%s::::::::::::::::::%s"%(out21[i]["fq_name"][-1],out21[i]["uuid"])
                              obj_uuid2.append(str(out21[i]["uuid"]))
              #elif   threading.currentThread().getName()  == "Thread-3":
                # r3=requests.get("http://10.213.18.39:80/shared-object/address?q=fq_name:IP_3*&size=10000",headers=head)
                # out3 = r3.json()
                # out31 = out3["address"]
                 for i in range(len(out3["address"])):
                        if "IP_" in out31[i]["fq_name"][-1]:
                              print "%s::::::::::::::::::%s"%(out31[i]["fq_name"][-1],out31[i]["uuid"])
                              obj_uuid3.append(str(out31[i]["uuid"]))
             # elif   threading.currentThread().getName()  == "Thread-4":
             #    r4=requests.get("http://10.213.18.39:80/shared-object/address?q=fq_name:IP_4*&size=10000",headers=head)
             #    out4 = r4.json()
             #    out41 = out4["address"]
                 for i in range(len(out4["address"])):
                        if "IP_" in out41[i]["fq_name"][-1]:
                              print "%s::::::::::::::::::%s"%(out41[i]["fq_name"][-1],out41[i]["uuid"])
                              obj_uuid4.append(str(out41[i]["uuid"]))
              #elif   threading.currentThread().getName()  == "Thread-5":
              #   r5=requests.get("http://10.213.18.39:80/shared-object/address?q=fq_name:IP_5*&size=10000",headers=head)
              #   out5 = r5.json()
              #   out51 = out5["address"]
                 for i in range(len(out5["address"])):
                        if  out51[i]["fq_name"][-1] == "APP_5" :
                              pass
                        else :
                              print "%s::::::::::::::::::%s"%(out51[i]["fq_name"][-1],out51[i]["uuid"])
                              obj_uuid5.append(str(out51[i]["uuid"]))
              #elif   threading.currentThread().getName()  == "Thread-6":
              #   r6=requests.get("http://10.213.18.39:80/shared-object/address?q=fq_name:IP_6*&size=10000",headers=head)
              #   out6 = r6.json()
              #   out61 = out6["address"]
                 for i in range(len(out6["address"])):
                        if "IP_" in out61[i]["fq_name"][-1]:
                              print "%s::::::::::::::::::%s"%(out61[i]["fq_name"][-1],out61[i]["uuid"])
                              obj_uuid6.append(str(out61[i]["uuid"]))
              #elif   threading.currentThread().getName()  == "Thread-7":
              #   r7=requests.get("http://10.213.18.39:80/shared-object/address?q=fq_name:IP_7*&size=10000",headers=head)
              #   out7 = r7.json()
              #   out71 = out7["address"]
                 for i in range(len(out7["address"])):
                        if "IP_" in out71[i]["fq_name"][-1]:
                              print "%s::::::::::::::::::%s"%(out71[i]["fq_name"][-1],out71[i]["uuid"])
                              obj_uuid7.append(str(out71[i]["uuid"]))
              #elif   threading.currentThread().getName()  == "Thread-8":
              #   r8=requests.get("http://10.213.18.39:80/shared-object/address?q=fq_name:IP_8*&size=10000",headers=head)
              #   out8 = r8.json()
              #   out81 = out8["address"]
                 for i in range(len(out8["address"])):
                        if "IP_" in out81[i]["fq_name"][-1]:
                              print "%s::::::::::::::::::%s"%(out81[i]["fq_name"][-1],out81[i]["uuid"])
                              obj_uuid8.append(str(out81[i]["uuid"]))
              #elif   threading.currentThread().getName()  == "Thread-9":
              #   r9=requests.get("http://10.213.18.39:80/shared-object/address?q=fq_name:IP_9*&size=10000",headers=head)
              #   out9 = r9.json()
              #   out91 = out9["address"]
                 for i in range(len(out9["address"])):
                        if "IP_" in out91[i]["fq_name"][-1]:
                              print "%s::::::::::::::::::%s"%(out91[i]["fq_name"][-1],out91[i]["uuid"])
                              obj_uuid9.append(str(out91[i]["uuid"]))
                 
        return (obj_uuid,obj_uuid2,obj_uuid3,obj_uuid4,obj_uuid5,obj_uuid6,obj_uuid7,obj_uuid8,obj_uuid9)
        #return (obj_uuid)
        #fp.write("%s"%out)

#import pdb;pdb.set_trace()
obj_uuid,obj_uuid2,obj_uuid3,obj_uuid4,obj_uuid5,obj_uuid6,obj_uuid7,obj_uuid8,obj_uuid9 = get_application(head,option="Address")
#obj_uuid = get_application(head,option="Address")
print len(obj_uuid),len(obj_uuid2),len(obj_uuid3),len(obj_uuid4),len(obj_uuid5),len(obj_uuid6),len(obj_uuid7),len(obj_uuid8),len(obj_uuid9)
#print len(obj_uuid)
"""
threads = []
for i in range(2):
    t = threading.Thread(target=get_application,args=(head,"Address"))
   # threading.settrace(get_application(head,option="Address"))
    #threads.append(t)
    t.start()
    threads.append(t)
for process in threads:
    print process
"""
def put_application(head,uuid,data1):
    for i in range(len(uuid)):
        op = "http://10.213.18.39:80/shared-object/application/%s"%(uuid[i])
        r=requests.get(op,headers=head)
        out = r.json()
        op_ref["application"]["fq_name"][-1] = out["application"]["fq_name"][-1]
        print out["application"]["fq_name"][-1]
        
        if out["application"]["fq_name"][-1] == "APP_1" or out["application"]["fq_name"][-1] == "APP_2" or out["application"]["fq_name"][-1] == "APP_3" or out["application"]["fq_name"][-1] == "APP_4" or out["application"]["fq_name"][-1] == "APP_5" :
                     pass
        else:
                 r=requests.put(op,headers=head,data=json.dumps(data1))
                 print r.text

#import pdb;pdb.set_trace()
#put_application(head,obj_uuid,op_ref)
#threads = []
#for i in range(5):
#    t = threading.Thread(target=get_application,args=(head,"Address"))
#   # threading.settrace(get_application(head,option="Address"))
#    threads.append(t)
#    t.start()
        
#print len(obj_uuid)
#delete["input"]["shared_object_info"]["object_uuids"] = obj_uuid[1:360]
#print len(delete["input"]["shared_object_info"]["object_uuids"])
############################################
#Comment :::  Delete application by uuid
#  API
#############################################
def delete_application(head,payloads):
       
        r = requests.post("http://10.213.18.39:80/shared-object/bulk_delete",headers=head,data=json.dumps(payloads))
        print r.text
#delete_application(head,delete)

############################################
#Comment :::  GET application by uuid
#  API
#############################################
get_uuid ={
	"input": {
		"object_uuids": ["758110dd-6abb-4de9-89fc-ac85dc20b6cb"]
	}

}
#import pdb;pdb.set_trace()
get_uuid["input"]["object_uuids"] = obj_uuid[1:1380]
#print len(get_uuid["input"]["object_uuids"])
#print len(obj_uuid)
fp = open("app4.txt","w+")
def get_application_uuid(head,payloads,option=""):
       if option == "application":
                 r = requests.post("http://10.213.18.39:80/shared-object/get_application_by_uuids",headers=head,data=json.dumps(payloads))
                 print  r.text
       elif option == "address":
                 r = requests.post("http://10.213.18.39:80/shared-object/get_address_by_uuids",headers=head,data=json.dumps(payloads))
                 print  r.text
#import pdb;pdb.set_trace()
#get_application_uuid(head,get_uuid,option="application")
#get_application_uuid(head,get_uuid,option="address")

############################################
#Comment :::  DELETE application by uuid
#  API
#############################################
def app_delete(head,uuid):
     for i in  range(len(uuid)):
        r = requests.delete('http://10.213.18.39:80/shared-object/address/%s'%uuid[i],headers=head)
        if r.text == "Authentication required":
                       out = get_auth_token(headers,payloads)
                       head = {'Content-Type': 'application/json',"X-Auth-Token":out} 
                       r = requests.delete('http://10.213.18.39:80/shared-object/address/%s'%uuid[i],headers=head)
        print r.text
uuid = obj_uuid
uuid2 = obj_uuid2
uuid3= obj_uuid3
uuid4= obj_uuid4
uuid5= obj_uuid5
uuid6 = obj_uuid6
uuid7= obj_uuid7
uuid8= obj_uuid8
uuid9= obj_uuid9

#app_delete(head,uuid)


t1 = threading.Thread(target=app_delete,args=(head,uuid))

t2 = threading.Thread(target=app_delete,args=(head,uuid2))
t3 = threading.Thread(target=app_delete,args=(head,uuid3))
t4 = threading.Thread(target=app_delete,args=(head,uuid4))
t5 = threading.Thread(target=app_delete,args=(head,uuid5))
t6 = threading.Thread(target=app_delete,args=(head,uuid6))
t7 = threading.Thread(target=app_delete,args=(head,uuid7))
t8 = threading.Thread(target=app_delete,args=(head,uuid8))
t9 = threading.Thread(target=app_delete,args=(head,uuid9))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()
t9.start()





data = {
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




def put_address(head,uuid,data):
             for i in range(len(uuid)):
                    #import pdb;pdb.set_trace()
                    op = "http://10.213.18.39:80/shared-object/address/%s"%(uuid[i])
                    r=requests.get(op,headers=head)
                    if r.text == "Authentication required":
                       out = get_auth_token(headers,payloads)
                       head = {'Content-Type': 'application/json',"X-Auth-Token":out} 
                    #import pdb;pdb.set_trace()
                    out = r.json()
                    data["address"]["fq_name"][-1] = out["address"]["fq_name"][-1]
                    print data
                    if out["address"]["fq_name"][-1] == "IP_1" or out["address"]["fq_name"][-1] == "IP_2" or out["address"]["fq_name"][-1] == "IP_3" or out["address"]["fq_name"][-1] == "IP_4" or out["address"]["fq_name"][-1] == "IP_5" :
                            pass
                    else:
                          r=requests.put(op,headers=head,data=json.dumps(data))
                          print r.text
uuid1,uuid2,uuid3,uuid4,uuid5,uuid6,uuid7,uuid8,uuid9=obj_uuid,obj_uuid2,obj_uuid3,obj_uuid4,obj_uuid5,obj_uuid6,obj_uuid7,obj_uuid8,obj_uuid9
threads=[]
#import pdb;pdb.set_trace()
#put_address(head,uuid5,data)
#p1 = threading.Thread(target = put_address,args=(head,uuid1,data))
#p2 = threading.Thread(target = put_address,args=(head,uuid3,data))
#p3 = threading.Thread(target = put_address,args=(head,uuid3,data))
#p4 = threading.Thread(target = put_address,args=(head,uuid4,data))
#p5 = threading.Thread(target = put_address,args=(head,uuid5,data))
#p6 = threading.Thread(target = put_address,args=(head,uuid6,data))
#p7 = threading.Thread(target = put_address,args=(head,uuid7,data))
#p8 = threading.Thread(target = put_address,args=(head,uuid8,data))
#p9 = threading.Thread(target = put_address,args=(head,uuid9,data))
#p1.start()
#p2.start()
#p3.start()
#p4.start()
#p5.start()
#p6.start()
#p7.start()
#p8.start()
#p9.start()
