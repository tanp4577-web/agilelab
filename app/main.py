from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse

def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    if b == 0: raise ValueError("Cannot divide by zero.")
    return a / b

class WebCalculatorHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        
        parsed_url = urllib.parse.urlparse(self.path)
        params = urllib.parse.parse_qs(parsed_url.query)
        result_text = ""
        
        if 'op' in params and 'num1' in params and 'num2' in params:
            try:
                op = params['op'][0]
                n1 = float(params['num1'][0])
                n2 = float(params['num2'][0])
                if op == 'add': result_text = f"<h3 style='color:green;'>Result: {add(n1, n2)}</h3>"
                elif op == 'sub': result_text = f"<h3 style='color:green;'>Result: {subtract(n1, n2)}</h3>"
                elif op == 'mul': result_text = f"<h3 style='color:green;'>Result: {multiply(n1, n2)}</h3>"
                elif op == 'div': result_text = f"<h3 style='color:green;'>Result: {divide(n1, n2)}</h3>"
            except Exception as e:
                result_text = f"<h3 style='color:red;'>Error: {str(e)}</h3>"

        html = f"""
        <html>
        <head><title>All-in-One DevOps Calculator</title></head>
        <body style="font-family: Arial, sans-serif; text-align: center; margin-top: 50px; background-color: #f4f4f9;">
            <h2>--- DevOps Menu-Driven Web Calculator ---</h2>
            <form action="/" method="get" style="display: inline-block; text-align: left; padding: 25px; border: 2px solid #333; background: #fff; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
                <strong>Number 1:</strong><br>
                <input type="number" name="num1" step="any" required style="width: 100%; padding: 8px; margin: 8px 0;"><br>
                <strong>Number 2:</strong><br>
                <input type="number" name="num2" step="any" required style="width: 100%; padding: 8px; margin: 8px 0;"><br>
                <strong>Select Operation:</strong><br>
                <div style="margin: 10px 0;">
                    <input type="radio" name="op" value="add" checked> Addition (+)<br>
                    <input type="radio" name="op" value="sub"> Subtraction (-)<br>
                    <input type="radio" name="op" value="mul"> Multiplication (*)<br>
                    <input type="radio" name="op" value="div"> Division (/)<br>
                </div>
                <button type="submit" style="width: 100%; padding: 10px; background: #007bff; color: white; border: none; border-radius: 4px; cursor: pointer; font-size: 16px;">Calculate</button>
            </form>
            <br><br>
            {result_text}
        </body>
        </html>
        """
        self.wfile.write(bytes(html, "utf-8"))

if __name__ == "__main__":
    server = HTTPServer(('0.0.0.0', 80), WebCalculatorHandler)
    print("Serving application on port 80...")
    server.serve_forever()
