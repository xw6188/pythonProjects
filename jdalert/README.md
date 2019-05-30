使用JD API入口编写一个命令行工具：jdalert JID, JID, ... 

打印京东网站上相应的产品价格并发送email给xw6188@163.com
API入口：http://p.3.cn/prices/mgets?skuIds=JID&type=1， 
商品ID这么获取: http://item.jd.com/18315090316.html, 
返回的结果是[{"op":"1599.00","m":"2599.00","id":"J_18315090316","p":"1269.00"}] 
"p"是价格

要点：API服务接口，Jason数据格式parsing，命令行处理（单个或多个变量）

要求结果：可运行命令行及其运行结果
cd D:\PythonProjects\jdalert-master
python jdalert.py 18315090316 5089253