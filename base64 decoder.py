import base64

e_t = 'd3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrX2kyMDRoa2o2fQ=='
d_t = base64.b64decode(e_t).decode('utf-8')
print(d_t)


