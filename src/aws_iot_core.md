# AWS IoT Core

To use MQTT with AWS IoT Core you first need to create "a thing". The next
step is to create (or upload) a certificate to aws. A Certificate in aws
can either be "active" or "inactive". If you just created it, it will be
inactive and you need to activate it to be able to use it.

The Certificate will be used to connect the client. The certificate
should (?) be attached to the thing we created earlier. Also, the
certificate will need to have a policy attached with which we can
manage the access of that certificate (client) to the mqtt. More on
that later.





## Certificate and Keys

* The Device is created
* The Policy is created
* The Certificate is created (42d37198571a8bbabdf8789332807132d09d626ad9dc2ef68d7335d57d125e7f)

I have received:
* the certificate  ID-certificate.pem.crt
* the private key  ID-private.pem.key
* the public key   ID-public.pem.key
Also two Amazon certificates: AmazonRootCA1.cer and AmazonRootCA3.pem.cer


