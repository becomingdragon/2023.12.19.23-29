from lxml import etree
# xpath解析 1）本地文件 2）服务器响应的数据

# 解析本地文件  etree .parse("路径")
tree =etree .parse('爬虫_解析_xpath的基本使用.html')

# 路径查询 (1) //:查找所有子孙节点，不考虑层级关系
#         (2) /:找直接子节点
# li_list=tree.xpath('//body/ul/li/text()') # text()可以查看内容
# print(li_list)
# print(len(li_list))

# 谓词查询 //div[@id]
#        //div[@id="123"] 注意：是双引号
# 属性查询 //@class
# li_list=tree.xpath('//body/ul/li[@id="l3"]/text()')
# print(li_list)
# # 属性
# li_list=tree.xpath('//body/ul/li[@id="l3"]/@class')
# print(li_list)


# 模糊查询  //div[contains(@id,"he")]     id中包含"he"的
#          //div[starts-with(@id,"he")]   id以"he"开头的
# li_list=tree.xpath('//body/ul/li[contains(@id,"l")]/text()')
# print(li_list)
# li_list=tree.xpath('//body/ul/li[starts-with(@id,"l")]/text()')
# print(li_list)


# 逻辑运算 //div[@id="head" and @class ="s_down]
#        //title | //price
li_list=tree.xpath('//body/ul/li[@id="l3c" and @class="c3"]/text()')
print(li_list)

li_list=tree.xpath('//body/ul/li[@id="l3c"]/text() | //body/ul/li[@id="ck2"]/text()' )
print(li_list)