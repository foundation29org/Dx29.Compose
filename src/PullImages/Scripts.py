import os

# Login in Azure
os.system('az login')

# Login in container registry
os.system('az acr login --name <acr_name>')

# Docker pull images

# Bioentity
output = os.popen('az acr repository show-tags --name <acr_name> --repository dx29bioentity --top 1 --orderby time_desc').read()
latest_tag = output.split("\n")
image_name = ('<acr_server>/dx29bioentity:' + latest_tag[1]).replace(" ", "")
os.system('docker pull ' + image_name)
os.system('docker image tag ' + image_name + ' dx29bioentity:latest')
os.system('docker rmi ' + image_name)

# BioNET
output = os.popen('az acr repository show-tags --name <acr_name> --repository dx29bionet --top 1 --orderby time_desc').read()
latest_tag = output.split("\n")
image_name = ('<acr_server>/dx29bionet:' + latest_tag[1]).replace(" ", "")
os.system('docker pull ' + image_name)
os.system('docker image tag ' + image_name + ' dx29bionet:latest')
os.system('docker rmi ' + image_name)

# PhenSimilarity
output = os.popen('az acr repository show-tags --name <acr_name> --repository dx29-phensimilarity --top 1 --orderby time_desc').read()
latest_tag = output.split("\n")
image_name = ('<acr_server>/dx29-phensimilarity:' + latest_tag[1]).replace(" ", "")
os.system('docker pull ' + image_name)
os.system('docker image tag ' + image_name + ' dx29-phensimilarity:latest')
os.system('docker rmi ' + image_name)

# Documents
output = os.popen('az acr repository show-tags --name <acr_name> --repository dx29-documents --top 1 --orderby time_desc').read()
latest_tag = output.split("\n")
image_name = ('<acr_server>/dx29-documents:' + latest_tag[1]).replace(" ", "")
os.system('docker pull ' + image_name)
os.system('docker image tag ' + image_name + ' dx29-documents:latest')
os.system('docker rmi ' + image_name)

# File storage
output = os.popen('az acr repository show-tags --name <acr_name> --repository dx29filestorage --top 1 --orderby time_desc').read()
latest_tag = output.split("\n")
image_name = ('<acr_server>/dx29filestorage:' + latest_tag[1]).replace(" ", "")
os.system('docker pull ' + image_name)
os.system('docker image tag ' + image_name + ' dx29filestorage:latest')
os.system('docker rmi ' + image_name)

# Localization
output = os.popen('az acr repository show-tags --name <acr_name> --repository dx29localization --top 1 --orderby time_desc').read()
latest_tag = output.split("\n")
image_name = ('<acr_server>/dx29localization:' + latest_tag[1]).replace(" ", "")
os.system('docker pull ' + image_name)
os.system('docker image tag ' + image_name + ' dx29localization:latest')
os.system('docker rmi ' + image_name)

# Medical History
output = os.popen('az acr repository show-tags --name <acr_name> --repository dx29medicalhistory --top 1 --orderby time_desc').read()
latest_tag = output.split("\n")
image_name = ('<acr_server>/dx29medicalhistory:' + latest_tag[1]).replace(" ", "")
os.system('docker pull ' + image_name)
os.system('docker image tag ' + image_name + ' dx29medicalhistory:latest')
os.system('docker rmi ' + image_name)

# Annotations
output = os.popen('az acr repository show-tags --name <acr_name> --repository dx29annotations --top 1 --orderby time_desc').read()
latest_tag = output.split("\n")
image_name = ('<acr_server>/dx29annotations:' + latest_tag[1]).replace(" ", "")
os.system('docker pull ' + image_name)
os.system('docker image tag ' + image_name + ' dx29annotations:latest')
os.system('docker rmi ' + image_name)

# Annotations Worker
output = os.popen('az acr repository show-tags --name <acr_name> --repository dx29annotationsworker --top 1 --orderby time_desc').read()
latest_tag = output.split("\n")
image_name = ('<acr_server>/dx29annotationsworker:' + latest_tag[1]).replace(" ", "")
os.system('docker pull ' + image_name)
os.system('docker image tag ' + image_name + ' dx29annotationsworker:latest')
os.system('docker rmi ' + image_name)

# Documents
output = os.popen('az acr repository show-tags --name <acr_name> --repository dx29-documents --top 1 --orderby time_desc').read()
latest_tag = output.split("\n")
image_name = ('<acr_server>/dx29-documents:' + latest_tag[1]).replace(" ", "")
os.system('docker pull ' + image_name)
os.system('docker image tag ' + image_name + ' dx29-documents:latest')
os.system('docker rmi ' + image_name)

# TermSearch2 
output = os.popen('az acr repository show-tags --name <acr_name> --repository dx29-termsearch2 --top 1 --orderby time_desc').read()
latest_tag = output.split("\n")
image_name = ('<acr_server>/dx29-termsearch2:' + latest_tag[1]).replace(" ", "")
os.system('docker pull ' + image_name)
os.system('docker image tag ' + image_name + ' dx29-termsearch2:latest')
os.system('docker rmi ' + image_name)

# Web
output = os.popen('az acr repository show-tags --name <acr_name> --repository dx29web --top 1 --orderby time_desc').read()
latest_tag = output.split("\n")
image_name = ('<acr_server>/dx29web:' + latest_tag[1]).replace(" ", "")
os.system('docker pull ' + image_name)
os.system('docker image tag ' + image_name + ' dx29web:latest')
os.system('docker rmi ' + image_name)

# Mailing
output = os.popen('az acr repository show-tags --name <acr_name> --repository dx29-mailing --top 1 --orderby time_desc').read()
latest_tag = output.split("\n")
image_name = ('<acr_server>/dx29-mailing:' + latest_tag[1]).replace(" ", "")
os.system('docker pull ' + image_name)
os.system('docker image tag ' + image_name + ' dx29-mailing:latest')
os.system('docker rmi ' + image_name)


# API-Gateway
#output = os.popen('az acr repository show-tags --name <acr_name> --repository dx29-api-gateway --top 1 --orderby time_desc').read()
#latest_tag = output.split("\n")
#image_name = ('<acr_server>/dx29-api-gateway:'+latest_tag[1]).replace(" ", "")
#os.system('docker pull '+image_name)
#os.system('docker image tag '+image_name+' dx29-api-gateway:latest')
#os.system('docker rmi '+image_name)
