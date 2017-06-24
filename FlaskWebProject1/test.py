import json

print(json.dumps({"a":"a"}))
print(str({"a":"a"}))

data = {"loginSuccess": False,
             "loginFailedReason":"该邮箱不存在" }

print(json.dumps(data))        