import requests
import time
# slow
# while True:
#     st = time.time()
#     # httpbin.org, keep-alive 해줌
#     requests.get("http://35.170.225.136")
#     print(time.time() - st)
#     time.sleep(0.5)
# fast
s = requests.Session()
a = requests.adapters.HTTPAdapter(max_retries=3,
                                  pool_connections=4,
                                  pool_maxsize=4,
                                  )
s.mount('http://', a)
while True:
    st = time.time()
    s.get("http://35.170.225.136")
    print(time.time() - st)
    time.sleep(1)
s.close()