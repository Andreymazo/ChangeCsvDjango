# import urllib3
#
# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# import certifi
#
# certifi.where()
# BASE_URL = 'http://176.192.70.122:90/fitnes_t_nfc_mobile/hs/nfc_mobile/v1'


# body = {
#     "Request_id": "e1477272-88d1-4acc-8e03-7008cdedc81e",
#     "ClubId": "59115d1e-9052-11eb-810c-6eae8b56243b",
#     "Method": "GetSpecialistList",
#     "Parameters": {
#         "ServiceId": ""
#     }
# }


# response = requests.post(f"{BASE_URL}", json=body)
# response = requests.get(f"{URL}")
# print(response.json())

# import urllib, urllib2, ssl
# import certifi
#
# request = urllib2.Request(url=url)
# kw = dict()
# if url.startswith('https://'):
#     certifi_context = ssl.create_default_context(cafile=certifi.where())
#     kw.update(context=certifi_context)
# urllib2.urlopen(request, **kw)
# ####################################################
# from http.client import HTTPSConnection
# from base64 import b64encode
#
#
# # Authorization token: we need to base 64 encode it
# # and then decode it to acsii as python 3 stores it as a byte string
# def basic_auth(username, password):
#     token = b64encode(f"{username}:{password}".encode('utf-8')).decode("ascii")
#     return f'Basic {token}'

# # URL =  'www.google.com'
# # www.google.com

# #
# # This sets up the https connection
# c = HTTPSConnection(f"{URL}")
# # then connect
# headers = {'Authorization': basic_auth(username, password)}
# c.request('GET', '/', headers=headers)
# # get the response back
# res = c.getresponse()


# at this point you could check the status etc
# this gets the page text
# data = res.read()
##########################################
import requests
# import certifi
# import urllib3
#
# http = urllib3.PoolManager(
#     cert_reqs="CERT_REQUIRED",
#     ca_certs=certifi.where()
# )

# http.request("GET", "https://httpbin.org/")
# session = requests.Session()
# session.auth = (username, password)
# auth = session.post('http://test.fitnesskit-admin.ru')
# response = session.get('http://test.fitnesskit-admin.ru/team/get/1/')
###################################################
from requests.auth import HTTPBasicAuth

# res = requests.post(URL, auth=HTTPBasicAuth(f'{username}', f'{password}'))
# print(res)


# URL = 'https://test.fitnesskit-admin.ru/team/get_employees'


# URL = "https://google.com"

params = {'username': "FitnessKit",
          'password': "vY0xodyg"}
# import urllib3
#
# urllib3.request(
#     "GET",
#     f"{URL}",
#     headers={"Accept-Encoding": "zstd"}
# )

# import ssl
#
# from urllib3 import PoolManager
# from urllib3.util import create_urllib3_context
#
# ctx = create_urllib3_context()
# ctx.load_default_certs()
# ctx.options |= ssl.OP_ENABLE_MIDDLEBOX_COMPAT


# import urllib.request
# urllib.request.urlopen(f"{URL})
from uuid import uuid4

# pool.request("GET", f"{URL}")


import requests
from requests.auth import HTTPBasicAuth
from django.core.management import BaseCommand

username = "FitnessKit"
password = "vY0xodyg"
# URL = 'https://test.fitnesskit-admin.ru/team/get/1/'
URL='http://176.192.70.122:90/fitnes_t_nfc_mobile/hs/nfc_mobile/v1'
# body={
# "Request_id": f"{rand_token1}",
# "ClubId": f"{rand_token2}",
# "Method": "GetSpecialistList",
# "Parameters": {
# "ServiceId": ""
# }
# }
##############################
# response = requests.get(URL, auth=HTTPBasicAuth(username, password))#, verify=False
###########################
import requests
from requests.auth import HTTPBasicAuth
import certifi


auth = HTTPBasicAuth('username', 'password')
# body = {}

r = requests.post(url=URL, auth=auth, verify='/etc/ssl/certs')#/usr/lib/python3.6/site-packages/certifi/cacert.pem#data=body,



class Command(BaseCommand):

    def handle(self, *args, **options):
        print(r)
        # print(response)#params=body
        # print(response.headers)
        # print(response.status_code)
        # print(response.url)



        # print(requests.post(URL, auth=HTTPBasicAuth(f'{username}', f'{password}'), verify=False))
        # print(session.get('http://test.fitnesskit-admin.ru/team/get/1/', verify=False))
        # print(requests.get(f"{URL}"))
        # with PoolManager(ssl_context=ctx) as pool:
        #     print(pool.request("GET", f"{URL}"))
        # print(urllib.request.urlopen(f"{URL}"))
        # print(requests.get(URL, verify=False,
        #                    params=params))  # auth=(f'{username}', f'{password}'))) #verify=False).text)
        # print(res.read())
# import requests

# r = requests.get('https://my.website.com/rest/path', auth=('myusername', 'mybasicpass'))
# print(r.text)
