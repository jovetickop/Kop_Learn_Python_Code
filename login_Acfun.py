#模拟登陆Acfun
import requests
from bs4 import BeautifulSoup

def login():
    header = {
        'Accept':'*/*',
        'Accept-Encoding':'gzip, deflate',
        'Connection':'keep-alive',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
 
    }
    session = requests.session();
    # res = session.get('http://s.hub.hust.edu.cn/hub.jsp',headers = header).content
    # ln = BeautifulSoup(res).find('input',  attrs = {'name':'ln'})['value']

    login_data = {
        'username':'13545160791',
        'password':'1121271124kop'
        }
    session.post('http://www.acfun.tv/login.aspx', data = login_data, headers = header)
    
    res = session.get('http://www.acfun.tv')
    print(res.text)

if __name__ == '__main__':
    login();
