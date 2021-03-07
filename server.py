import http.server
import socketserver
from http import HTTPStatus
import sqlite3

con = sqlite3.connect('messages.db')
cur = con.cursor()

# Create table
cur.execute('''CREATE TABLE IF NOT EXISTS temperature
               (date text, source text, symbol text, temp real, raw real)''')

# Insert a row of data
cur.execute("INSERT INTO temperature VALUES ('2021-03-07','vegetronix','F',57,2.14)")

# Save (commit) the changes
con.commit()

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        cur.execute("select temp, date, source from temperature")
        row = cur.fetchone()
        result = 'temp is: '+ str(row[0]) + ', date: '+ str(row[1])
        self.wfile.write(result.encode())

httpd = socketserver.TCPServer(('', 80), Handler, bind_and_activate=False)
httpd.allow_reuse_address = True
httpd.server_bind()
httpd.server_activate()
httpd.serve_forever()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()