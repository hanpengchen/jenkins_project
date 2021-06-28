"""前置条件，环境中安装过 allure-pytest 包，网上下载allure并配置环境变量"""
"""使用allure报告，需要在pytest.ini配置文件的命令行加上 --alluredir report"""
"""pytest运行后生成report是json格式，需要在命令行输入  allure generate report/ -o report/html --clean 转化json格式为html"""


class TestLogin:
    def test_login01(self):
        assert 1

    def test_login02(self):
        assert 1


