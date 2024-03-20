# 导入必要的库
from pdfminer.high_level import extract_text
import ebooklib
from ebooklib import epub
# 指定PDF文件路径
pdf_path = 'test1/use_in_test.pdf'

# 使用extract_text函数提取文本
text = extract_text(pdf_path)

# 打印提取的文本
# print(text)
print(type(text))

# 创建一个新的 EPUB 书籍
book = epub.EpubBook()

# 设置书籍的标识符、标题和语言
book.set_identifier('id123456')
book.set_title('Sample book')
book.set_language('en')

# 创建一个 EPUB 章节
c1 = epub.EpubHtml(title='Introduction', file_name='intro.xhtml', lang='en')
c1.content = '<h1>Introduction</h1><p>This is a test paragraph.</p>'

# 将章节添加到书籍中
book.add_item(c1)

# 定义书籍目录
book.toc = (epub.Link('intro.xhtml', 'Introduction', 'intro'),)

# 添加默认的 NCX 和封面
book.add_item(epub.EpubNcx())
book.add_item(epub.EpubNav())

# 定义书籍的封面
style = 'BODY {color: white;}'
nav_css = epub.EpubItem(uid="style_nav", file_name="style/nav.css", media_type="text/css", content=style)
book.add_item(nav_css)

# 设置书籍的封面
book.set_cover("image.jpg", open('test1/ppage.png', 'rb').read())

# 保存书籍
epub.write_epub('test1/test.epub', book, {})
