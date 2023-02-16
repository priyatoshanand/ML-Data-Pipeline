
import os





#API DETAILS 
API_KEY ="KLZDAMWDPRLJ7XYQ" #os.getenv('API_KEY',None)

API_SECRET_KEY ="OYS8Kcdp8+5VzWRQtgNZNVF11ns+Unm/iKhjNMCgcAAD5S+tvPjiCHTu/GKG9m2D"  #os.getenv('API_SECRET_KEY',None)
BOOTSTRAP_SERVER ="pkc-6ojv2.us-west4.gcp.confluent.cloud:9092" #os.getenv('BOOTSTRAP_SERVER',None)

# authentication related details
# SECURITY_PROTOCOL = os.getenv('SECURITY_PROTOCOL',None)
# SSL_MACHENISM = os.getenv('SSL_MACHENISM',None)
SECURITY_PROTOCOL="SASL_SSL"
SSL_MACHENISM="PLAIN"

#Schema related variables
ENDPOINT_SCHEMA_URL  = "https://psrc-6y63j.ap-southeast-2.aws.confluent.cloud" #os.getenv('ENDPOINT_SCHEMA_URL',None)
SCHEMA_REGISTRY_API_KEY = "GFO5FB4SUXST46CE" #os.getenv('SCHEMA_REGISTRY_API_KEY',None)
SCHEMA_REGISTRY_API_SECRET ="eWWuKW74rc0P2mqI+JnzmxM5MTgk1jPxqO9tcllxsY4vq8Ft9Tf8es1y0OlA1uQ7" #os.getenv('SCHEMA_REGISTRY_API_SECRET',None)


def sasl_conf():

    sasl_conf = {'sasl.mechanism': SSL_MACHENISM,
                 # Set to SASL_SSL to enable TLS support.
                #  'security.protocol': 'SASL_PLAINTEXT'}
                'bootstrap.servers':BOOTSTRAP_SERVER,
                'security.protocol': SECURITY_PROTOCOL,
                'sasl.username': API_KEY,
                'sasl.password': API_SECRET_KEY
                }
    print(sasl_conf)
    return sasl_conf



def schema_config():
    return {'url':ENDPOINT_SCHEMA_URL,
    
    'basic.auth.user.info':f"{SCHEMA_REGISTRY_API_KEY}:{SCHEMA_REGISTRY_API_SECRET}"

    }

if __name__ == '__main__':
    sasl_conf()

