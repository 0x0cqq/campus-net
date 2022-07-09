from waitress import serve
import server

serve(server.app, listen='*:5000')