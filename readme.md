

### Important

Change the Broker info in Python file, regenrate the docker

    rpk topic create temperatures --brokers localhost:54595,localhost:54601,localhost:54600

    kcat -C -b localhost:54595,localhost:54601,localhost:54600 -t temperatures -o beginning

    set env KAFKA_BROKERS=host.docker.internal:51209,host.docker.internal:51214,host.docker.internal:51215

#### Kowl UI

    docker run --network=host -p 8080:8080 -e KAFKA_BROKERS=localhost:54595,localhost:54601,localhost:54600 docker.redpanda.com/vectorized/console:latest
    docker run -p 8080:8080 -e KAFKA_BROKERS=localhost:54595,localhost:54601,localhost:54600 docker.redpanda.com/vectorized/console:latest

    docker run -p 8080:8080 -e KAFKA_BROKERS=host.docker.internal:9093 docker.redpanda.com/vectorized/console:latest


