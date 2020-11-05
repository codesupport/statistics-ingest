import os

service_account = os.environ["GOOGLE_SERVICE_ACCOUNT"]

print("Attempting to generate service account...")

file = open("./service-account.json", "w+")
file.write(service_account)
file.close()

print("Successfully generated service account.")
