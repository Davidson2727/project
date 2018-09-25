import requests

userdata = {"u_id":"0444234","u_name":"jasdfasdfasfde","u_pass":"12345","email":"address@email.com"}
resp = requests.get('http://ddysfunction.ihostfull.com/test.php', params=userdata)

print(resp.status_code)
print('end')

