# 最基本的提交方式


# 切换不同的仓库
```sh
git remote #显示已经储存的远程仓库
git remote -v #详细
git remote add pycode https://github.com/user/repo.git #添加仓库，别名为pycode
git remote rename pycode pycode1 #重命名为pycode1
git remote remove new-origin #删除仓库
git remote set-url pycode https://github.com/user/new-repo.git #设置仓库的url
git remote show pycode #显示远程仓库的详细信息
```

`git clone ` 