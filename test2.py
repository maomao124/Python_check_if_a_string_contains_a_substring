"""
 * Project name(项目名称)：Python检测字符串中是否包含某子串
 * Package(包名): 
 * File(文件名): test2
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/23 
 * Time(创建时间)： 20:02
 * Version(版本): 1.0
 * Description(描述)： index() 方法也可以用于检索是否包含指定的字符串，不同之处在于，当指定的字符串不存在时，index() 方法会抛出异常。

 index() 方法的语法格式如下：
str.index(sub[,start[,end]])
此格式中各参数的含义分别是：
str：表示原字符串；
sub：表示要检索的子字符串；
start：表示检索开始的起始位置，如果不指定，默认从头开始检索；
end：表示检索的结束位置，如果不指定，默认一直检索到结尾。
 """

if __name__ == '__main__':
    str1 = "1234567890123456789012345678901234567"
    print(str1.index("34"))
    # print(str1.index("35"))
    print(str1.index("345"))
    print(str1.index("67890"))
    print(str1.index("34", 6))
    print(str1.index("34", 13))
    # print(str1.index("34", 13, 15))

    print(str1.rindex("34"))
    # print(str1.rindex("35"))
    print(str1.rindex("345"))
    print(str1.rindex("67890"))
    print(str1.rindex("34", 6))
    print(str1.rindex("34", 13))
    # print(str1.rindex("34", 13, 15))

    input()
