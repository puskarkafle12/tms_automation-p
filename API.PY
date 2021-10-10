import requests
import datetime
url = 'https://tms35.nepsetms.com.np/tmsapi/rtApi/ws/stockQuote/2888'
# header: {channel: "@data", transaction: "marketwatch", tnxCode: null}

# url = 'https://tms49.nepsetms.com.np/tmsapi/metadata/serverTime'
headers = {}
headers={'X-XSRF-TOKEN': 'd0291ecb-c6d3-4a49-b803-ab67fea1c8e2'
}

result = requests.get(url, headers=headers)
print(result.cookies)
# print(result.content.decode())
# tmstime=result.content.decode().split()[1].replace('","data":null}', '')[:15]
# tms_time = datetime.datetime.strptime(tmstime,"%H:%M:%S.%f")
# print('tms time',tms_time)
# print(datetime.datetime.today())

# print(tms_time-datetime.datetime.today())

# https://tms49.nepsetms.com.np/tmsapi/metadata/serverTime