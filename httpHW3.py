import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 3030)
print("Starting up on %s", server_address)
s.bind(server_address)
s.listen(1)

while True:
    print ("Waiting for connection")
    host, clientAddress = s.accept()
    response_data = host.recv(10000)
    response = response_data.decode('utf-8')
    list_split_by_space = response.split(' ')
    print(list_split_by_space[0])
        
    ##This is the root folder html
    if(list_split_by_space[0]=='GET' and list_split_by_space[1] == '/'):
        host.sendall(bytes("HTTP/1.1 200 OK \r\nContent-Type: text/html; charset=UTF-8\r\nX-Content-Type-Options: nosniff\r\n\r\n"
        +"<!DOCTYPE html>"
            "<head>"
        "<title>Aritra Paul</title>"
       + "<link rel=\"stylesheet\" type=\"text/css\" href=\"style.css\"/>"
    '</head>'
    '<body>'
        '<div id = "menu_bar">'
            '<h1 class = "title">CSE 312: Aritra Paul'
             '</h1>'
            '<p class = "title">This is a default template for all the homeworks for CSE 312.</p>'
        '</div>'
        '<div>'
            '<table class = "title" style="width:100%">'
                '<tr>'
                  '<th>Pages</th>'
                  '<th>Descriptions</th>'
                '</tr>'
                '<tr>'
                  '<td>About</td>'
                  '<td>Click this link to learn more about me.</td>'
                '</tr>'
              '</table>'
        '</div>'

        '<div id="js_Button">'
        '</br>'
            '<h2>Javascript Buttons</h2>'
            '<button type="button" onclick="changeBackground(\'red\');">Change to Red</button>'
            '<button type="button" onclick="changeBackground(\'blue\');">Change to Blue</button>'
            '<button type="button" onclick="changeBackground(\'white\');">Change to White</button>'
        '</div>'
        '<script src="script.js"></script>'
    "</body>", "utf-8"))
    #This is the /style.css directory
    elif(list_split_by_space[1] == '/style.css'):
        host.sendall(bytes("HTTP/1.1 200 OK \r\nContent-Type: text/css; char-set=UTF-8\r\n\r\n"
        +"body{"
            'background-color: antiquewhite;'
            '}'

'table, th, td {'
    'border: 1px solid black;'
    'border-collapse: collapse;'
  '}'

'th, td {'
    'padding: 15px;'
  '}'

'h1.title{'
    'text-align: center;'
'}'

'p.title{'
    'text-align: center;'
'}'

'table.title{'
    'text-align: center;'
"}", "utf-8"))
    ##This is the /javascript directory
    elif(list_split_by_space[1] == '/script.js'):
        host.sendall(bytes("HTTP/1.1 200 OK \r\nContent-Type: application/javascript; char-set=UTF-8 \r\n\r\n"
        +'function changeBackground(color){'
    'document.body.style.background =color;'
'}', "utf-8"))
    ##Everything else that is not in our directory
    else:
        host.sendall(bytes("HTTP/1.1 404 Sorry this part of the site doesn't exist \r\n Content-Type: text/plain \r\n Content-Length:120\r\n\r\n", "utf-8"))

s.close()
# while True:
#     client, address = s.accept()
#     print(f"Connection from {address} has been established!")
#     client.send(bytes("Hello World!", "utf-8"))