import random

from tools.api import request_tool


def test_changePriceByProdCode(pub_data,db):
    prodCodes = db.select_execute("select product_code from `t_prod_product` where status = '0' and product_code is not null")
    pub_data["prodCode"] = random.choice(prodCodes)[0]
    method = "POST"  # 请求方法，全部大写
    feature = "商品模块"  # allure报告中一级分类
    story = '产品'  # allure报告中二级分类
    title = "全字段正常流_1（根据产品编码批量修改商品价格）"  # allure报告中用例名字
    uri = "/product/changePriceByProdCode"  # 接口地址
    headers = {'Host': '192.168.1.151:8084', 'Connection': 'keep-alive', 'accept': 'application/json;charset=UTF-8', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36', 'token': 'eyJ0aW1lT3V0IjoxNTk0NjM3NDQ5MzY2LCJ1c2VySWQiOjkzLCJ1c2VyTmFtZSI6Inlhbmd5dW4xOSJ9', 'Origin': 'http://192.168.1.151:8084', 'Referer': 'http://192.168.1.151:8084/swagger-ui.html?urls.primaryName=product%20apis', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9',"token": "${token}"}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    data={'price': '1999', 'prodCode': '${prodCode}'}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,data=data)
    r.request.headers


def test_post_json(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '用户登录'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/login"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = '''
    {
  "pwd": "xuepl123",
  "userName": "xuepl123"
}
    '''
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,json_data=json_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title)

