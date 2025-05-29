#!/usr/bin/env python3
"""
Start script for QuickCaption demo.
Runs both the Flask API server and serves the demo HTML page.
"""

import subprocess
import threading
import time
import http.server
import socketserver
import os
import webbrowser

def start_api_server():
    """Start the Flask API server"""
    print("Starting API server on http://localhost:5000...")
    subprocess.run(["python", "api.py"])

def start_demo_server():
    """Start HTTP server for demo page"""
    # Change to docs directory
    os.chdir("docs")
    
    # Start simple HTTP server
    PORT = 8000
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Demo page server running on http://localhost:{PORT}")
        print(f"Open http://localhost:{PORT} in your browser to use the demo")
        httpd.serve_forever()

if __name__ == "__main__":
    print("=== QuickCaption Demo Startup ===")
    print("This will start both the API server and demo page.")
    print("Make sure you have installed dependencies with: pip install -r requirements.txt")
    print()
    
    # Start API server in background thread
    api_thread = threading.Thread(target=start_api_server, daemon=True)
    api_thread.start()
    
    # Wait a moment for API server to start
    time.sleep(3)
    
    # Start demo server (this will block)
    try:
        start_demo_server()
    except KeyboardInterrupt:
        print("\nShutting down demo...")