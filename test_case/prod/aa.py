from tools.data import excel_tool
sku = excel_tool.get_test_case("test_case/prod/sku.xls")
print(sku)
print(sku[0][0])
print(sku[1][0][0])