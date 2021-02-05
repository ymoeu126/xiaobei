# 小北健康打卡
## **首先准备好一个github账号,注册链接[github](https://github.com/)**

# Github Actions说明
## 一、Fork此仓库
![](http://tu.yaohuo.me/imgs/2020/06/f059fe73afb4ef5f.png)
## 二、设置账号密码
![添加账号](https://i.loli.net/2021/02/05/KrHSRJk3xYAdGy5.png)
添加名为**XIAOBEI_USERNAME**、**XIAOBEI_PASSWORD**,**XIAOBEI_SCKEY**的变量  
值分别为**账号**、**密码**,**server酱sckey值**  
![](http://tu.yaohuo.me/imgs/2020/06/748bf9c0ca6143cd.png)

## 三、启用Action
1 点击**Action**，再点击**I understand my workflows, go ahead and enable them**  
2 修改任意文件后提交一次  
![](http://tu.yaohuo.me/imgs/2020/06/34ca160c972b9927.png)

## 四、查看运行结果
Actions > Cloud189Checkin > build  
能看到如下图所示，表示成功  
![](http://tu.yaohuo.me/imgs/2020/06/b9e596c99f3835e0.png)

此后，将会在每天10:00和22:00各签到一次  
若有需求，可以在[.github/workflows/run.yml]中自行修改 
