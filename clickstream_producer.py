import json
import time
import random
import uuid
from datetime import datetime
from confluent_kafka import Producer

# === Kafka connection config (Aiven credentials go here) ===
kafka_config = {
    'bootstrap.servers': 'demo-kafka-real-time-demo.e.aivencloud.com:11859',
    'security.protocol': 'SSL',
    'ssl.ca.location': 'ca.pem',
    'ssl.certificate.location': 'service.cert',
    'ssl.key.location': 'service.key'
}

# === Set up the producer ===
try:
    producer = Producer(kafka_config)
    print("✅ Kafka producer initialized.")
except Exception as e:
    print(f"❌ Failed to initialize Kafka producer: {e}")
    exit(1)

TOPIC = "clickstream-events"

# === Simulated page traffic ===
users = [f"user_{i}" for i in range(1, 6)]
pages = ["/", "/about", "/pricing", "/blog", "/signup"]

def generate_event():
    return {
        "event_id": str(uuid.uuid4()),
        "user_id": random.choice(users),
        "page": random.choice(pages),
        "timestamp": datetime.utcnow().isoformat()
    }

def delivery_report(err, msg):
    if err:
        print(f"❌ Delivery failed: {err}")
    else:
        print(f"✅ Delivered to {msg.topic()} [{msg.partition()}]")

# === Event loop ===
print("🚀 Sending clickstream events to Kafka... (Ctrl+C to stop)")

try:
    while True:
        event = generate_event()
        print("📤 Sending event:", event)  # ← Debug print

        try:
            producer.produce(
                TOPIC,
                key=event["user_id"],
                value=json.dumps(event),
                callback=delivery_report
            )
        except Exception as e:
            print(f"❌ Kafka produce error: {e}")

        producer.poll(0.1)
        time.sleep(1)

except KeyboardInterrupt:
    print("🛑 Producer stopped by user.")

finally:
    print("🔄 Flushing remaining messages...")
    producer.flush()
