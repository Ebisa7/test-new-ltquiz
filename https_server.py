#!/usr/bin/env python3
"""
HTTPS Server for PWA Testing
This script creates a local HTTPS server to test PWA install prompts.
"""

import http.server
import ssl
import socketserver
import os
import sys

PORT = 8443

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add PWA-friendly headers
        self.send_header('Cross-Origin-Embedder-Policy', 'require-corp')
        self.send_header('Cross-Origin-Opener-Policy', 'same-origin')
        self.send_header('Service-Worker-Allowed', '/')
        super().end_headers()

def generate_certificate():
    """Generate SSL certificate if it doesn't exist"""
    if not (os.path.exists('cert.pem') and os.path.exists('key.pem')):
        print("Generating SSL certificate...")
        os.system('openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes -subj "/C=US/ST=State/L=City/O=Organization/CN=localhost"')
        print("Certificate generated successfully!")

def main():
    print("Setting up HTTPS server for PWA testing...")
    
    # Generate certificate if needed
    generate_certificate()
    
    # Check if certificate files exist
    if not (os.path.exists('cert.pem') and os.path.exists('key.pem')):
        print("Error: Could not generate SSL certificate.")
        print("Please install OpenSSL and try again.")
        sys.exit(1)
    
    try:
        with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
            # Wrap socket with SSL using modern SSL context
            context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
            context.load_cert_chain(certfile='cert.pem', keyfile='key.pem')
            httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
            
            print(f"✅ HTTPS Server running at https://localhost:{PORT}")
            print("📱 Access this URL on your mobile device to test PWA install")
            print("🔒 Accept the security warning (self-signed certificate)")
            print("📋 Press Ctrl+C to stop the server")
            
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\n🛑 Server stopped by user")
    except Exception as e:
        print(f"❌ Error starting server: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 