#!/usr/bin/env python3
"""
Test script for GitHub Pages compatibility.
Serves the demo page using Python's built-in HTTP server.
"""

import http.server
import socketserver
import os
import webbrowser
import time
import threading

def start_server():
    """Start HTTP server for testing GitHub Pages compatibility"""
    # Change to docs directory
    os.chdir("docs")
    
    PORT = 8080
    Handler = http.server.SimpleHTTPRequestHandler
    
    # Add CORS headers for local testing
    class CORSRequestHandler(Handler):
        def end_headers(self):
            self.send_header('Cross-Origin-Embedder-Policy', 'require-corp')
            self.send_header('Cross-Origin-Opener-Policy', 'same-origin')
            super().end_headers()
    
    with socketserver.TCPServer(("", PORT), CORSRequestHandler) as httpd:
        print(f"🌐 GitHub Pages Test Server running on http://localhost:{PORT}")
        print("📝 This simulates how the demo will work on GitHub Pages")
        print("🤖 The AI model will download and run entirely in your browser")
        print("⏱️  Model loading may take 30-60 seconds on first load")
        print()
        print("Press Ctrl+C to stop the server")
        
        # Auto-open browser after a short delay
        def open_browser():
            time.sleep(2)
            webbrowser.open(f"http://localhost:{PORT}")
        
        threading.Thread(target=open_browser, daemon=True).start()
        
        httpd.serve_forever()

if __name__ == "__main__":
    try:
        start_server()
    except KeyboardInterrupt:
        print("\n🛑 Server stopped")