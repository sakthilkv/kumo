from livereload import Server

server = Server()


server.watch('login.html')


server.serve(root='.')
