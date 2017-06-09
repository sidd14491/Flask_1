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
          "APP107"
        ]
      }
    ]
  }
}
#op["application"]["fq_name"].update = "APP12")
for i in range(20):
     op["application"]["fq_name"][-1] = "APP%s"%i
     print "###############################"
     print op

