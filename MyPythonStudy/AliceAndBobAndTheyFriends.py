# @Time: 2022/6/3 12:25
# @Author: 丨枫
# @File AliceAndBobAndTheyFriends.py
"""
密码学家 Rivest、Shamir、Adleman 于1977年4月撰写了一篇论文《数字签名与公钥密码学》
（On Digital Signatures and Public-Key Cryptosystems），并投稿至了一个期刊上，
不过很遗憾这篇论文被拒稿了。随后他们修改了论文，并将论文重新命名为《一种实现数字签名和公钥密码系统的方法》
（A Method of Obtaining Digital Signatures and Public-Key Cryptosystems），
最终于1978年2月成功发表于顶级期刊《ACM通信》（Communications of the ACM）。
在这篇论文中，三位密码学家嫌弃使用A、B两个字母代表角色太无聊，就用Alice和Bob来代替A和B。
"""


class CryptographyPeople:  # 定义一个密码城邦人物类型
    def __init__(self, name_cn, name_en, role, desc):
        self.name_cn = name_cn
        self.name_en = name_en
        self.role = role
        self.desc = desc


# 添加一个简易的密码城邦人物解析器
class SimpleCryptographyPeopleParser:
    def __init__(self, text) -> None:
        self.text = text

    def parse(self, desc):
        # 解析名字部分
        name_cn, name_en, rest = self.parse_name(desc)

        # 解析角色部分
        role, rest = self.parse_role(rest)

        # 解析描述不符
        desc = self.parse_desc(rest)

        # 创建密码城邦人物
        people = CryptographyPeople(name_cn, name_en, role, desc)

        return people

    def parse_name(self, text):
        # 解析名字部分
        index = text.find('是')
        name, rest = text[0:index], text[index + 1:]

        # 解析中英文名字
        start = name.find('（')
        end = name.find('）')
        name_cn = name[0:start]
        name_en = name[start + 1:end]

        return name_cn.strip(), name_en.strip(), rest

    def parse_role(self, text):
        index1 = text.find('。')
        index2 = text.find('，')

        index = 0
        if index1 > 0 and index2 > 0:
            index = min(index1, index2)
        else:
            index = max(index1, index2)

        role, rest = text[0:index], text[index + 1:len(text) - 1]

        # 去除冗余量词
        counts = ['一名', '一位', '一个']
        for count in counts:
            role = role.replace(count, '')
        return role.strip(), rest.strip()

    def parse_desc(self, name_cn, name_en, role, rest):
        desc = rest
        if desc:
            # 识别自我主语
            self_list = [name_cn, '他', '她']
            for self_item in self_list:
                desc = desc.replace(self_item, '我')
        else:
            # 补充默认描述
            desc = '很高兴认识你'


class CryptographyCity:
    def __init__(self):
        self.peoples = []

    def add(self, text):
        parser = SimpleCryptographyPeopleParser(text)
        people = parser.parse(text)
        self.peoples.append(people)

    def introduce(self):
        [self.say(people) for people in self.peoples]

    def say(self, people):
        info = f'{people.name_cn}({people.name_en}): 密码学家说我是一位{people.role}，{people.desc}。'
        print(info)


# 创建一个密码城邦，它包含 add 和 introduce 两个方法
if __name__ == '__main__':
    crypto_roles = [
        '爱丽丝（Alice）是信息发送者。',
        '与鲍伯（Bob）是信息接受者。通例上，爱丽丝希望把一条消息发送给鲍伯。',
        '卡罗尔或查利（Carol或Charlie）是通信中的第三位参加者。',
        '戴夫（Dave）是通信中的第四位参加者。',
        '伊夫（Eve）是一位偷听者（eavesdropper），但行为通常是被动的。她拥有偷听的技术，但不会中途篡改发送的消息。在量子密码学中，伊夫也可以指环境（environment）。'
    ]
    city = CryptographyCity()
    for crypto_role in crypto_roles:
        city.add(crypto_role)
    city.introduce()
