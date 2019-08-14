# *_*coding:utf-8 *_*
import re

class XML_FILE:
    def __init__(self):
        pass

    def add_XML(self,xml):
        self.XML = xml

    def add_SET(self,set)  :
        self.SET = set

class XML:
    def __init__(self,ver,enc):
        self.version = ver
        self.encoind = enc

class SET:
    def __init__(self):
        pass

    def add_l(self,l):
        self.l = l

    def add_d(self,d):
        self.d = d


class L:
    def __init__(self,count):
        self.count = count
        self.p_list = []
    def add_p(self,p):
        self.p_list.append(p)


class P:
    def __init__(self,name=None,age=None,x=None):
        self.name = name
        self.age = age
        self.x = x


class D:
    def __init__(self):
        self.el_list = []
    def add_el(self,el):
        self.el_list.append(el)


class EL:

    def __init__(self,key,val,text):
        self.key = key
        self.value = val
        self.text =text

    def add_p(self,p):
        self.p = p





with open("/home/python/Desktop/bluecore/hrcode/p11/data.xml","r",encoding="UTF-8") as f:
    lines = f.readlines()

xml_file = XML_FILE()
l = L(0)
set = SET()
d = D()
el = EL("0","0","0")

for each_line in lines:
    if re.findall("<?xml",each_line):
        tiqu = re.findall("version=(.*?) encoding=(.*?)\?",each_line)
        xml = XML(tiqu[0][0],tiqu[0][1])
        xml_file.XML = xml
    elif re.findall("<set>",each_line):
        set = SET()
        xml_file.add_SET(set)
    elif re.findall("<l",each_line):
        tiqu = re.findall("count=(.*?)>",each_line)
        l = L(tiqu[0])
        set.add_l(l)

    elif re.findall("<p name",each_line):
        tiqu = re.findall(r"name=(.*?) age=(.*?)/",each_line)
        p = P(tiqu[0][0],tiqu[0][1])
        l.add_p(p)
    elif re.findall("<d",each_line):
        d = D()
        set.add_d(d)

    elif re.findall("<el",each_line):
        line_index = lines.index(each_line)
        tiqu = re.findall(r"key=(.*?) value=(.*?)>",each_line)
        el = EL(tiqu[0][0],tiqu[0][1],lines[line_index+1])
        d.add_el(el)

    elif re.findall("<p x",each_line):
        tiqu = re.findall(r"p x=(.*?)/",each_line)
        p = P(x=tiqu[0])
        el.add_p(p)





print(xml_file.SET.l.p_list[0].name)






