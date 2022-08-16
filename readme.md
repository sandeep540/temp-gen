

### Important

Change the Broker info in Python file, regenrate the docker

    rpk topic create temperatures --brokers localhost:51209,localhost:51214,localhost:51215

    kcat -C -b localhost:51209,localhost:51214,localhost:51215 -t temperatures -o beginning

