import pyqrcode

info = """
Name: Udhav More
Designation: Software Engineer
Skills: Python, C#, Java, Go, Docker
"""


png_file = 'info.png'

print('Converting data to QR')
qrcode = pyqrcode.create(info)
qrcode.png(png_file, scale=4)
print(f'Checkout {png_file}')

