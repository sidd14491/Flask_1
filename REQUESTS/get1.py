import requests,json
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
    "app_name": "APP102",
    "app_device_specific_name": "APP102",
    "parent_type": "project",
    "definition_type": "CUSTOM",
    "display_name": "APP102",
    "name": "APP105",
    "app_sig_type": "GROUP",
    "fq_name": [
      "default-domain",
      "default-project",
      "APP106"
    ],
    "application_refs": [
      {
        "to": [
          "default-domain",
          "default-project",
          "APP1"
        ],
        "to": [
          "default-domain",
          "default-project",
          "APP1"
        ],
      }
    ]
  }
}
delete = {
	"input": {
		"shared_object_info":{
		"object_type":"APPLICATION",
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
		"application_refs": [
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
import pdb;pdb.set_trace()
fd = open("app.txt","w+")
def put_applicatio(head,payloads):
    for i in range(6,2500):
        op_ref["application"]["fq_name"][-1] = "APP%s"%i 
        r=requests.put("http://10.213.18.39:80/shared-object/application",headers=head,data=json.dumps(payloads))
        #fd = open("app.txt","w+")
        out=r.json
        fd.write("%s:::::::%s#############\n"%(i,out))
put_applicatio(head,op_ref)
#fp = open("app1.txt","w+")
############################################
#Comment :::  Get application by uuid
#  API
#############################################
def get_application(head):
        r=requests.get("http://10.213.18.39:80/shared-object/application?size=6000",headers=head)
        out = r.json()
        #fp.write("%s"%out)
        obj_uuid = []
        out1 = out["application"]
        op = out['total']
        for i in range(len(out["application"])):
                #if "APP1" in  out1[i]["fq_name"][-1]:
                if "APP1"  ==   out1[i]["fq_name"][-1] or "APP2"  ==   out1[i]["fq_name"][-1] or "APP3"  ==   out1[i]["fq_name"][-1] or "APP4"  ==   out1[i]["fq_name"][-1] or "APP5"  ==   out1[i]["fq_name"][-1]:
                       pass 
                else:
                      obj_uuid.append(str(out1[i]["uuid"]))
        return obj_uuid
        #fp.write("%s"%out)

import pdb;pdb.set_trace()
obj_uuid = get_application(head)
delete["input"]["shared_object_info"]["object_uuids"] = obj_uuid
print len(delete)
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
get_uuid["input"]["object_uuids"] = obj_uuid[1:470]
fp = open("app4.txt","w+")
def get_application_uuid(head,payloads):
       r = requests.post("http://10.213.18.39:80/shared-object/get_application_by_uuids",headers=head,data=json.dumps(payloads))
       print  r.text
#get_application_uuid(head,get_uuid)

############################################
#Comment :::  DELETE application by uuid
#  API
#############################################
def app_delete(head,uuid):
     for i in  range(len(uuid)):
        r = requests.delete('http://10.213.18.39:80/shared-object/application/%s'%uuid[i],headers=head)
        print r.text
#uuid = obj_uuid
#app_delete(head,uuid)
