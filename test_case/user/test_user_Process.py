import pytest

from tools.api import request_tool
'''
自动生成 数字 20,80   #生成20到80之间的数字 例：56
自动生成 字符串 5 中文数字字母特殊字符 xuepl        #生成以xuepl开头加上长度2到5位包含中文数字字母特殊字符的字符串，例子：xuepl我1
自动生成 地址
自动生成 姓名
自动生成 手机号
自动生成 邮箱
自动生成 身份证号
'''

@pytest.mark.realname
def test_signup(pub_data):
    pub_data["phone"] = "自动生成 手机号"
    pub_data["userName"] = "自动生成 字符串 4 数字 hai"

    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '用户注册'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/signup"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = '''
    {
      "phone": "${phone}",
      "pwd": "string999",
      "rePwd": "string999",
      "userName": "${userName}"
}
    '''
    status_code = 200  # 响应状态码
    expect = "注册成功"  # 预期结果
    json_path = [{"cstId" : "$.data.cstId"}]
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,json_data=json_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title,json_path=json_path)

@pytest.mark.realname
def test_login(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '用户登录'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/login"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = '''
    {
      "pwd": "string999",
      "userName": "string999"
}
    '''
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,json_data=json_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title)

@pytest.mark.realname
def test_changepwd(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '修改密码'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/user/changepwd"  # 接口地址
    headers = {"token": "${token}"}
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = '''
     {
      "newPwd": "string999",
      "oldPwd": "string999",
      "reNewPwd": "string999",
      "userName": "string999"
}
    '''
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,json_data=json_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers = headers)
    print(r.request.body)

@pytest.mark.realname
def test_realname(pub_data):
    pub_data["email"] = "自动生成 邮箱"
    pub_data["certno"] = "自动生成 身份证号"
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '用户登录'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/cst/realname2"  # 接口地址
    # header = "${token}"
    headers = {"token": "${token}"}
    # json path，参数类型为列表 根据jsonpath提取响应正文中的数据
    # json path，参数类型为列表 根据jsonpath提取响应正文中的数据
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = '''
    {
      "cstId": "${cstId}",
      "customerInfo": {
        "birthday": "2000-01-01",
        "certno": "${certno}",
        "city": "上海市区",
        "cstName": "核力量",
        "email": "${email}",
        "province": "上海市",
        "sex": 0
  }
}
    '''
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,json_data=json_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers = headers)
