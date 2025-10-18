"""Tool registration for ChillMCP server."""

from fastmcp import FastMCP

from chillmcp.state import ServerState


def register_all_tools(mcp: FastMCP, state: ServerState) -> None:
    """
    Register all tools with the MCP server.

    This function serves as the central hub for registering all tool modules.

    Args:
        mcp: FastMCP server instance
        state: Server state object
    """
    # Tool registration will be added here
    # from chillmcp.tools import basic, advanced
    # basic.register_basic_tools(mcp, state)
    # advanced.register_advanced_tools(mcp, state)
    pass
