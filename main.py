from fastmcp import FastMCP

# Create MCP server (NO transport here)
mcp = FastMCP(
    name="Onyx MCP Server"
)

# Register a tool
@mcp.tool()
def greet(name: str) -> str:
    """Greet a user by name"""
    return f"Hello {name}, response from MCP server!"

# Run MCP server over HTTP
if __name__ == "__main__":
    mcp.run_http(
        host="127.0.0.1",
        port=8000
    )
