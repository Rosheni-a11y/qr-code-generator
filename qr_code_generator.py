import qrcode

def generate_qr(data,filename='qr_code.png'):
  
#create QR code
  qr = qrcode.QRCode(
    version = 1,
    box_size=10,
    border=5
  )

  qr.add_data(data)
  qr.make(fit=True)

#Add data
  img = qr.make_image(fill_color='black',back_color='white')

#save
  img.save(filename)
  print(f" QR code saved as: {filename}")

if __name__ == "__main__":

  generate_qr('https://www.youtube.com/watch?v=dQw4w9WgXcQ','youtube_qr.png')

  generate_qr('Hello World!','hello_qr.png')

  wifi_data = 'WIFI:T:WPA;S:MyWiFi;P:password123;;'
  generate_qr(wifi_data,'wifi_qr.png')
 