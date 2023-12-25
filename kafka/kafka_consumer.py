from pykafka import KafkaClient
import json

kafka_topic = "stack_exchange"
kafka_bootstrap_servers = "localhost:39092"

def kafka_consumer():
    client = KafkaClient(hosts=kafka_bootstrap_servers)
    topic = client.topics[kafka_topic]

    consumer = topic.get_simple_consumer(
        consumer_group=b"spark_preprocessing",
        auto_offset_reset=2,
        reset_offset_on_start=True,
    )

    for message in consumer:
        if message is not None:
            data = json.loads(message.value.decode("utf-8"))
            print("Received message:", data)


if __name__ == "__main__":
    kafka_consumer()
