import urllib.parse
import http.client
import json


    # account 为API_ID
    # password 为API_KY
def main():
    host = "106.ihuyi.com"
    sms_send_uri = "/webservice/sms.php?method=Submit"
    params = urllib.parse.urlencode({'account':'C20770154','password':'49726d48421b06b7d0e0875ca0f3666d','content':'您的验证码是：147258。请不要把验证码泄露给其他人。', 'mobile': '18818037397', 'format':'json'})
    print(params)
    headers = {'Content-type':'application/x-www-form-urlencoded','Accept':'text/plain'}
    conn = http.client.HTTPConnection(host,port=80,timeout=30)
    conn.request('POST',sms_send_uri,params,headers)
    response = conn.getresponse()
    response_str = response.read()
    jsonstr = response_str.decode('utf-8')
    print(json.loads(jsonstr))
    conn.close()

if __name__ == '__main__':
    main()