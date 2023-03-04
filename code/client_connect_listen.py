import paho.mqtt.client as mqtt # ?
from pathlib import Path
import os

MQTT_HOST = os.getenv("MQTT_HOST", None)

ROOTDIR = Path(__file__).parent
CERTID = "42d37198571a8bbabdf8789332807132d09d626ad9dc2ef68d7335d57d125e7f"
CA = Path(ROOTDIR).joinpath(f"../assets/AmazonRootCA1.cer")
CERT = Path(ROOTDIR).joinpath(f"../assets/{CERTID}-certificate.pem.crt")
KEY = Path(ROOTDIR).joinpath(f"../assets/{CERTID}-private.pem.key")

def on_connect(client, userdata, flags, reasonCode, properties):
        print("Connection returned " + str(reasonCode))

def main():
    mqtt_client = mqtt.Client(protocol=mqtt.MQTTv5)
    mqtt_client.on_connect = on_connect
    mqtt_client.tls_set(
        ca_certs=CA,
        certfile=CERT,
        keyfile=KEY
    )
    print(MQTT_HOST)
    mqtt_client.connect(MQTT_HOST, port=8883)
    mqtt_client.subscribe("sometopic/#")
    mqtt_client.loop_forever()

if __name__ == "__main__":
    main()


