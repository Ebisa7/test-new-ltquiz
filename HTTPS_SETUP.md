# HTTPS Setup for PWA Testing

## Why HTTPS is Required

Chrome and other browsers require HTTPS for PWA install prompts to work properly. Without HTTPS, you'll only see "Add to Home Screen" instead of the "Install" prompt.

## Local HTTPS Setup Options

### Option 1: Using Python with SSL (Recommended)

1. **Generate SSL certificate:**
   ```bash
   # Create a self-signed certificate
   openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes
   ```

2. **Run HTTPS server:**
   ```python
   # Create https_server.py
   import http.server
   import ssl
   import socketserver
   
   PORT = 8443
   
   class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
       def end_headers(self):
           self.send_header('Cross-Origin-Embedder-Policy', 'require-corp')
           self.send_header('Cross-Origin-Opener-Policy', 'same-origin')
           super().end_headers()
   
   with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
       httpd.socket = ssl.wrap_socket(httpd.socket, certfile='cert.pem', keyfile='key.pem', server_side=True)
       print(f"Server running at https://localhost:{PORT}")
       httpd.serve_forever()
   ```

3. **Run the server:**
   ```bash
   python https_server.py
   ```

4. **Access your app:**
   - Go to `https://localhost:8443`
   - Accept the security warning (self-signed certificate)
   - You should now see the "Install" prompt!

### Option 2: Using Node.js

1. **Install http-server globally:**
   ```bash
   npm install -g http-server
   ```

2. **Generate certificate:**
   ```bash
   openssl req -newkey rsa:2048 -new -nodes -x509 -days 3650 -keyout key.pem -out cert.pem
   ```

3. **Run HTTPS server:**
   ```bash
   http-server -S -C cert.pem -K key.pem -p 8443
   ```

### Option 3: Using Live Server (VS Code Extension)

1. **Install Live Server extension**
2. **Configure for HTTPS:**
   - Open VS Code settings
   - Search for "Live Server"
   - Enable "Use Local IP"
   - Set port to 8443

## Testing the Install Prompt

1. **Open Chrome DevTools**
2. **Go to Application tab**
3. **Check Manifest section:**
   - Should show "Installable" status
   - All icons should be valid
   - Service worker should be registered

4. **Test on mobile:**
   - Use Chrome DevTools device emulation
   - Or access from your phone using your computer's IP address
   - You should see the "Install" button in the top-right corner

## Troubleshooting

### Still seeing "Add to Home Screen" instead of "Install"?

1. **Check HTTPS:**
   - URL must start with `https://`
   - No mixed content warnings

2. **Check Manifest:**
   - Valid JSON format
   - All required fields present
   - Icons are accessible

3. **Check Service Worker:**
   - Must be registered successfully
   - No errors in console

4. **Check Browser:**
   - Use latest Chrome version
   - Clear browser cache
   - Try incognito mode

### Security Warnings

When using self-signed certificates:
- Click "Advanced" in the security warning
- Click "Proceed to localhost (unsafe)"
- This is normal for local development

## Production Deployment

For production, use a real SSL certificate from:
- Let's Encrypt (free)
- Your hosting provider
- Cloudflare (free SSL)

---

**Note:** The install prompt behavior may vary slightly between Chrome versions and operating systems. 