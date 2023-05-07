'''
1.	编程练习：实现Feistel加解密过程（平衡和非平衡两种），不限语言，
轮函数F可以参考现有方案，或自己设计。
2.	扩展练习：使用DES、SM4算法进行加解密操作，验证其加解密效果，验
证其扩散性质。
'''


# 平衡Feistel加密
def FeistelBalance(key, text='-1', ):
    if text == '-1':
        text = input('输入要加密的字符串(明文字符为8的整数倍):')
    if len(text) % 8 != 0:
        print("输入的字符不为8的整数倍\n")
        return 0

    if len(key) % 4 != 0:
        print("输入的密匙长度不为4的整数倍\n")
        return 0

    encodetext = ''
    # 每64bit(8位字符进行)加密
    for i in range(len(text) // 8):
        temptext = text[i * 8: i * 8 + 8]
        L = temptext[:4]
        R = temptext[4:]
        for j in key:
            tempR = R
            result = ''#圈函数
            for k in range(4):
                result += chr(ord(L[k]) ^ ord(tempR[k]) ^ (ord(j)+1))
            R = result
            L = tempR
        encodetext += R + L

    return encodetext


if __name__ == '__main__':
    text = input('输入要加密的字符串(明文字符为8的整数倍):')
    times = input('加密循环次数:')
    key = []
    for i in range(int(times)):
        temp = input('请输入第%d组加密时使用的密钥（4个字符）' % (i + 1))
        key += temp

    # 加密
    entext = FeistelBalance(key, text)
    print("明文", text, "加密后的结果是：\n", entext)
    print()

    # 解密
    key.reverse()
    unentext = FeistelBalance(key, entext)
    print("秘文", entext, "解密后的结果是：\n", unentext)
    print()
