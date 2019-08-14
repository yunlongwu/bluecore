# *_*coding:utf-8 *_*
import json

ans_dict = {}

with open("/home/python/Desktop/bluecore/hrcode/p10/data.json","r",encoding='UTF-8') as f:
    thedata = f.read()
    ans_json = json.loads(thedata)
    print(ans_json)
    for each_key in ans_json:
        each_val = ans_json[each_key]
        if str(each_val).isdigit():
            ans_dict[each_key] = ans_json[each_key]
        elif isinstance(each_val,list):
            for item in each_val:
                if isinstance(item,dict):
                    for itme_key in item:
                        if str(item[itme_key]).isdigit():
                            ans_dict[itme_key] = item[itme_key]
        elif isinstance(each_val,dict):
            for each_val_key in each_val:
                each_val_val = each_val[each_val_key]
                if str(each_val_val).isdigit():
                    ans_dict[each_val_key] = each_val_val


newlis = sorted(ans_dict.items(),key=lambda x:x[1],reverse=True)
# ans_lis.sort(reverse=True)
with open("/home/python/Desktop/bluecore/hrcode/p10/p2.txt","w") as e:
    for line in newlis:
        e.write(str(line)+"\n")

print(newlis)