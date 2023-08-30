# PDF解密
import pikepdf
 
pdf = pikepdf.open("encrypt.pdf",  password='your_password')
pdf.save("decrypt.pdf")
pdf.close()