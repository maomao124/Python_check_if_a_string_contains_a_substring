"""
 * Project name(项目名称)：Python检测字符串中是否包含某子串
 * Package(包名): 
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/23 
 * Time(创建时间)： 19:58
 * Version(版本): 1.0
 * Description(描述)： find() 方法用于检索字符串中是否包含目标字符串，如果包含，则返回第一次出现该字符串的索引；反之，则返回 -1。
 find() 方法
str.find(sub[,start[,end]])
此格式中各参数的含义如下：
str：表示原字符串；
sub：表示要检索的目标字符串；
start：表示开始检索的起始位置。如果不指定，则默认从头开始检索；
end：表示结束检索的结束位置。如果不指定，则默认一直检索到结尾。
 """

if __name__ == '__main__':
    str1 = "1234567890123456789012345678901234567"
    print(str1.find("34"))
    print(str1.find("35"))
    print(str1.find("345"))
    print(str1.find("67890"))
    print(str1.find("34", 6))
    print(str1.find("34", 13))
    print(str1.find("34", 13, 15))

    print(str1.rfind("34"))
    print(str1.rfind("35"))
    print(str1.rfind("345"))
    print(str1.rfind("67890"))
    print(str1.rfind("34", 6))
    print(str1.rfind("34", 13))
    print(str1.rfind("34", 13, 15))

    input()
