from django.db import models

# Create your models here.

# 宣告一個 Article 繼承 models.Model
class Article(models.Model):
    # 標題，字元欄位(單行)，最大長度128，標題為唯一
    title = models.CharField(max_length=128, unique=True)
    # 文章內容，文字欄位(多行)
    content = models.TextField()
    # 日期，新增文章時會自動加入當前時間
    pubDateTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # 在範本或管理者介面預設顯示的值
        return self.title
# 宣告一個 Comment 繼承 models.Model
class Comment(models.Model):
    # 留言所屬文章，以外來鍵關連到 Article Model
    # models.CASCADE 表示文章刪除時，留言一併刪除
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    # 留言內容，字元欄位(一行)，長度128
    content = models.CharField(max_length=128)
    # 日期，新增留言時會自動加入當前時間
    pubDateTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # 在範本或管理者介面預設顯示的值
        return self.article.title + '-' + str(self.id)
