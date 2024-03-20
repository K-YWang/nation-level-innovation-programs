import subprocess

def convert_pdf_to_epub(pdf_path, epub_path):
    try:
        # 构建命令
        command = ['ebook-convert', pdf_path, epub_path]
        # 调用命令
        subprocess.run(command, check=True)
        print(f"Conversion successful: {epub_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error during conversion: {e}")

# 示例：将 'example.pdf' 转换为 'example.epub'
convert_pdf_to_epub('test1/use_in_test.pdf', 'test2/test.epub')




# export PATH=$PATH:/Applications/calibre.app/Contents/MacOS/ebook-convert