import pytest

from tools.api import request_tool
from tools.data import excel_tool
# json path，参数类型为列表 根据jsonpath提取响应正文中的数据
"""
def test_addProd(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "商品模块"  # allure报告中一级分类
    story = "产品"  # allure报告中二级分类
    title = "全字段正常流_1(增加产品)"  # allure报告中用例名字
    uri = "/product/addProd"  # 接口地址
    headers = {'Host': '192.168.1.151:8084', 'Connection': 'keep-alive', 'accept': '*/*', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36', 'token': 'eyJ0aW1lT3V0IjoxNTk0NjM1NTE1NDY2LCJ1c2VySWQiOjkzLCJ1c2VyTmFtZSI6Inlhbmd5dW4xOSJ9', 'Content-Type': 'application/json', 'Origin': 'http://192.168.1.151:8084', 'Referer': 'http://192.168.1.151:8084/swagger-ui.html?urls.primaryName=product%20apis', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9'}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    json_data='''{
  "brand": "xiaomi",
  "colors": [
    "red",
    "white"
  ],
  "price": 1000,
  "productCode": "puls6",
  "productName": "redmi",
  "sizes": [
    "125g","256g"
  ],
  "type": "数码"
}'''

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,json_data=json_data)
"""

def test_getSkuByProdCode(pub_data):
    method = "GET"  #请求方法，全部大写
    feature = "商品模块"  # allure报告中一级分类
    story = "产品"  # allure报告中二级分类
    title = "全字段正常流_1(校验生成商品)"  # allure报告中用例名字
    uri = "/product/getSkuByProdCode"  # 接口地址
    headers = {'Host': '192.168.1.151:8084', 'Connection': 'keep-alive', 'accept': 'application/json;charset=UTF-8', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36', 'token': 'eyJ0aW1lT3V0IjoxNTk0NjM1NTE1NDY2LCJ1c2VySWQiOjkzLCJ1c2VyTmFtZSI6Inlhbmd5dW4xOSJ9', 'Referer': 'http://192.168.1.151:8084/swagger-ui.html?urls.primaryName=product%20apis', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9',"token": "${token}"}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    params={'prodCode': 'puls6'}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,params=params)

def test_soldOut(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "商品模块"  # allure报告中一级分类
    story = '产品'  # allure报告中二级分类
    title = "全字段正常流_1（产品改为下架）"  # allure报告中用例名字
    uri = "/product/soldOut"  # 接口地址
    headers = {'Host': '192.168.1.151:8084', 'Connection': 'keep-alive', 'accept': 'application/json;charset=UTF-8', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36', 'token': 'eyJ0aW1lT3V0IjoxNTk0NjM1NTE1NDY2LCJ1c2VySWQiOjkzLCJ1c2VyTmFtZSI6Inlhbmd5dW4xOSJ9', 'Origin': 'http://192.168.1.151:8084', 'Referer': 'http://192.168.1.151:8084/swagger-ui.html?urls.primaryName=product%20apis', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9',"token": "${token}"}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    data={'productCode': 'puls6'}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,data=data)

def test_toPreSale(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "商品模块"  # allure报告中一级分类
    story = '产品'  # allure报告中二级分类
    title = "全字段正常流_1（产品改为预售）"  # allure报告中用例名字
    uri = "/product/toPreSale"  # 接口地址
    headers = {'Host': '192.168.1.151:8084', 'Connection': 'keep-alive', 'accept': 'application/json;charset=UTF-8', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36', 'token': 'eyJ0aW1lT3V0IjoxNTk0NjM3NDQ5MzY2LCJ1c2VySWQiOjkzLCJ1c2VyTmFtZSI6Inlhbmd5dW4xOSJ9', 'Origin': 'http://192.168.1.151:8084', 'Referer': 'http://192.168.1.151:8084/swagger-ui.html?urls.primaryName=product%20apis', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9',"token": "${token}"}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    data={'productCode': 'puls6'}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,data=data)

def test_changePriceByProdCode(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "商品模块"  # allure报告中一级分类
    story = '产品'  # allure报告中二级分类
    title = "全字段正常流_1（根据产品编码批量修改商品价格）"  # allure报告中用例名字
    uri = "/product/changePriceByProdCode"  # 接口地址
    headers = {'Host': '192.168.1.151:8084', 'Connection': 'keep-alive', 'accept': 'application/json;charset=UTF-8', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36', 'token': 'eyJ0aW1lT3V0IjoxNTk0NjM3NDQ5MzY2LCJ1c2VySWQiOjkzLCJ1c2VyTmFtZSI6Inlhbmd5dW4xOSJ9', 'Origin': 'http://192.168.1.151:8084', 'Referer': 'http://192.168.1.151:8084/swagger-ui.html?urls.primaryName=product%20apis', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9',"token": "${token}"}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    data={'price': '1999', 'prodCode': 'puls6'}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,data=data)

def test_getSkuByProdCode(pub_data):
    method = "GET"  #请求方法，全部大写
    feature = "商品模块"  # allure报告中一级分类
    story = "产品"  # allure报告中二级分类
    title = "全字段正常流_1(校验修改结果)"  # allure报告中用例名字
    uri = "/product/getSkuByProdCode"  # 接口地址
    headers = {'Host': '192.168.1.151:8084', 'Connection': 'keep-alive', 'accept': 'application/json;charset=UTF-8', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36', 'token': 'eyJ0aW1lT3V0IjoxNTk0NjM1NTE1NDY2LCJ1c2VySWQiOjkzLCJ1c2VyTmFtZSI6Inlhbmd5dW4xOSJ9', 'Referer': 'http://192.168.1.151:8084/swagger-ui.html?urls.primaryName=product%20apis', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9'}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    params={'prodCode': 'puls6'}
    header = {"toekn": "${token}"}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,params=params)

def test_changePrice(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "商品模块"  # allure报告中一级分类
    story = '商品'  # allure报告中二级分类
    title = "全字段正常流_1（修改商品价格）"  # allure报告中用例名字
    uri = "/product/changePrice"  # 接口地址
    headers = {'Host': '192.168.1.151:8084', 'Connection': 'keep-alive', 'accept': 'application/json;charset=UTF-8', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36', 'token': 'eyJ0aW1lT3V0IjoxNTk0NjM3NDQ5MzY2LCJ1c2VySWQiOjkzLCJ1c2VyTmFtZSI6Inlhbmd5dW4xOSJ9', 'Origin': 'http://192.168.1.151:8084', 'Referer': 'http://192.168.1.151:8084/swagger-ui.html?urls.primaryName=product%20apis', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9',"token": "${token}"}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    data={'SKU': 'puls6_red_125g', 'price': '999'}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,data=data)

def test_getSKU(pub_data):
    method = "GET"  #请求方法，全部大写
    feature = "商品模块"  # allure报告中一级分类
    story = '商品'  # allure报告中二级分类
    title = "全字段正常流_1（查询单个商品验证）"  # allure报告中用例名字
    uri = "/product/getSKU"  # 接口地址
    headers = {'Host': '192.168.1.151:8084', 'Connection': 'keep-alive', 'accept': 'application/json;charset=UTF-8', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36', 'token': 'eyJ0aW1lT3V0IjoxNTk0NjM3NDQ5MzY2LCJ1c2VySWQiOjkzLCJ1c2VyTmFtZSI6Inlhbmd5dW4xOSJ9', 'Referer': 'http://192.168.1.151:8084/swagger-ui.html?urls.primaryName=product%20apis', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9',"token": "${token}"}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    params={'SKU': 'puls6_red_125g'}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,params=params)

def test_fullSku(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "商品模块"  # allure报告中一级分类
    story = '商品'  # allure报告中二级分类
    title = "全字段正常流_1（全量调整单个商品库存）"  # allure报告中用例名字
    uri = "/product/fullSku"  # 接口地址
    headers = {'Host': '192.168.1.151:8084', 'Connection': 'keep-alive', 'accept': '*/*', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36', 'token': 'eyJ0aW1lT3V0IjoxNTk0NjM3NDQ5MzY2LCJ1c2VySWQiOjkzLCJ1c2VyTmFtZSI6Inlhbmd5dW4xOSJ9', 'Origin': 'http://192.168.1.151:8084', 'Referer': 'http://192.168.1.151:8084/swagger-ui.html?urls.primaryName=product%20apis', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9',"token": "${token}"}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    data={'qty': '10', 'skuCode': 'puls6_red_125g'}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,data=data)

def test_incrementSku(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "商品模块"  # allure报告中一级分类
    story = '商品'  # allure报告中二级分类
    title = "全字段正常流_1（增量调整单个商品库存）"  # allure报告中用例名字
    uri = "/product/incrementSku"  # 接口地址
    headers = {'Host': '192.168.1.151:8084', 'Connection': 'keep-alive', 'accept': '*/*', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36', 'token': 'eyJ0aW1lT3V0IjoxNTk0NjM3NDQ5MzY2LCJ1c2VySWQiOjkzLCJ1c2VyTmFtZSI6Inlhbmd5dW4xOSJ9', 'Origin': 'http://192.168.1.151:8084', 'Referer': 'http://192.168.1.151:8084/swagger-ui.html?urls.primaryName=product%20apis', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9',"token": "${token}"}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    data={'qty': '10', 'skuCode': 'puls6_red_125g'}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,data=data)

def test_getSkuRepertory(pub_data):
    method = "GET"  #请求方法，全部大写
    feature = "商品模块"  # allure报告中一级分类
    story = '商品'  # allure报告中二级分类
    title = "全字段正常流_1（查询单个商品验证）"  # allure报告中用例名字
    uri = "/product/getSkuRepertory"  # 接口地址
    headers = {'Host': '192.168.1.151:8084', 'Connection': 'keep-alive', 'accept': '*/*', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36', 'token': 'eyJ0aW1lT3V0IjoxNTk0NjM3NDQ5MzY2LCJ1c2VySWQiOjkzLCJ1c2VyTmFtZSI6Inlhbmd5dW4xOSJ9', 'Referer': 'http://192.168.1.151:8084/swagger-ui.html?urls.primaryName=product%20apis', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9',"token": "${token}"}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    params = {'SKU': 'puls6_red_125g'}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,params=params)

# 下载某产品的库存信息
def test_downProdRepertory(pub_data):
    method = "GET"  #请求方法，全部大写
    feature = "商品模块"  # allure报告中一级分类
    story = '商品'  # allure报告中二级分类
    title = "全字段正常流_1(下载某产品的库存信息)"  # allure报告中用例名字
    uri = "/product/downProdRepertory"  # 接口地址
    headers = {'Host': '192.168.1.151:8084', 'Connection': 'keep-alive', 'accept': '*/*', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36', 'token': 'eyJ0aW1lT3V0IjoxNTk0NzExNjMwOTAzLCJ1c2VySWQiOjI1NjEzLCJ1c2VyTmFtZSI6InN0cmluZzk5OSJ9', 'Referer': 'http://192.168.1.151:8084/swagger-ui.html?urls.primaryName=product%20apis', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9',"token": "${token}"}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    params={'pridCode': 'puls6'}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段

    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,params=params)
    with open("Repertory.xls","wb") as f:
        f.write(r.content)
        f.close()

sku = excel_tool.get_test_case("test_case/prod/sku.xls")
@pytest.mark.parametrize("sku_code,qty",sku[0],sku[1][0])
def test_uploaProdRepertory(pub_data,db,sku_code,qty):

    file_name = "./sku.xls" # 下载文件地址
    method = "POST"  #请求方法，全部大写
    feature = "库存模块"  # allure报告中一级分类
    story = '盘点库存'  # allure报告中二级分类
    title = "盘点库存"  # allure报告中用例名字
    uri = "/product/uploaProdRepertory"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    files = {"file":open(file_name,'rb')}
    headers={"token": "${token}"}
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,files=files,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=headers)
    result = db.select_execute("SELECT * FROM t_prod_repertory WHERE sku_code = '{}' AND qty = '{}'".format(sku_code,qty))
    print(result)
