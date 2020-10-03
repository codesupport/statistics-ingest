import os

service_account = os.environ["GOOGLE_SERVICE_ACCOUNT"]

file = open("./service-account.json", "w+")
file.write(service_account)
file.close()
