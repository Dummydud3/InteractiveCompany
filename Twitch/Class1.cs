using BepInEx;
using UnityEngine;
using System;
using System.Net;
using WebSocketSharp;
using WebSocketSharp.Server;
using System.Collections;

[BepInPlugin("com.example.websocketplugin", "WebSocket Plugin", "1.0.0")]
public class WebSocketPlugin : BaseUnityPlugin
{
    WebSocketServer server;

    void Awake()
    {
        StartCoroutine(StartServerAfterDelay());
        Debug.Log("Started the delay thingy");
    }

    IEnumerator StartServerAfterDelay()
    {
        yield return new WaitForSeconds(5f); // Wait for 5 seconds before starting the server

        Debug.Log("So 5 seconds have gone by and everything");

        try
        {
            // Create a new websocket server
            server = new WebSocketServer(IPAddress.Parse("127.0.0.1"), 8081); // Changed port to 8081

            // Bind the event for when a client connected
            server.AddWebSocketService<WebSocketBehavior>("/websocket", () => new CustomWebSocketBehavior());

            server.Start();
            Debug.Log("WebSocket server started on port 8081");
        }
        catch (Exception ex)
        {
            Debug.LogError("Error starting WebSocket server: " + ex.Message);
        }
    }

    void OnDestroy()
    {
        if (server != null)
        {
            server.Stop();
            Debug.Log("WebSocket server stopped");
        }
    }

    public class CustomWebSocketBehavior : WebSocketBehavior
    {
        protected override void OnMessage(MessageEventArgs e)
        {
            Debug.Log("Message received: " + e.Data);
        }
    }
}
