


# eklenecekler liste
"""
1) sıcaklık ve led kontrol kısmı
2) pompa çalıştırma ve açık-kapalı durumu
3) zaman ve saat durumu

 buraya eksik gördüklerini yaz yusuf ekliyeyim
 


"""
      
      







def web_page():
    
    
    
    
    if led.value() == 1:
        gpio_state="ACIK"
    else:
        gpio_state="KAPALI"
    html = """<html><head>
<title>SİSTEM ÖRNEĞİ</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="icon" href="data:,">
  <style>html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
  h1{color: #0F3376; padding: 2vh;}
  p{font-size: 1.5rem;}.button{display: inline-block; background-color: #e7bd3b; border: none; 
  border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
  .button2{background-color: #4286f4;}</style>
   <h1><SİSTEM</h1> 
  <p>SOILLES TECH: <strong>""" + """</strong>
</p><p><a href="/?led=on">
<button class="button">kapali</button></a></p>
  <p><a href="/?led=off">
  <button class="button button2">aktif</button></a></p>
  <h3>DHT ve LDR KISMI </h3>
  <p>
    <i class="fas fa-thermometer-half" style="color:#059e8a;"></i> 
    <span class="dht-labels">Temperature:</span> 
    <span>"""+"""</span>
    <sup class="units">&deg;C</sup>
  </p>
  <p>
    <i class="fas fa-tint" style="color:#00add6;"></i> 
    <span class="dht-labels">NEM DURUMU (burasi opsiyonel)</span>  
    <span>"""+"""</span>
    <sup class="units">%</sup>
  <p>
  <p>
    
    <i class="fas fa-tint" style="color:#00add6;"></i> 
    <span class="dht-labels">LDR DEGER</span>  
    <span>"""+"""</span>
    <sup class="units">%</sup>
  </p>
  </p> 
  
  
  </body>
  </head>
"""
  
  
    return html


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('',80))
s.listen(5)

while True:
  conn, addr = s.accept()
  print('Got a connection from %s' % str(addr))
  request = conn.recv(1024)
  request = str(request)
  print('Content = %s' % request)
  led_on = request.find('/?led=on')
  led_off = request.find('/?led=off')
  if led_on == 6:
    print('LED ON')
    led.value(1)
  if led_off == 6:
    print('LED OFF')
    led.value(0)
  response = web_page()
  conn.send('HTTP/1.1 200 OK\n')
  conn.send('Content-Type: text/html\n')
  conn.send('Connection: close\n\n')
  conn.sendall(response)
  conn.close()


