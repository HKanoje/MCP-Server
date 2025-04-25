from mcp.server.fastmcp import FastMCP
import os 

mcp = FastMCP("AI Sticky Notes")

NOTES_FILE = os.path.join(os.path.dirname(__file__), "notes.txt")

def ensure_file():
    if not os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "w") as f:
            f.write("")

@mcp.tool()
def add_note(message: str) -> str:
    """"
    Append a new note to the sticky notes file.

    Args:
        message (str): The note to be added.
    Returns:
        str: Confirmation message indicating the note has been saved.
    """
    ensure_file()
    with open(NOTES_FILE, "a") as f:
        f.write(message + "\n")
    return f"Note saved!!"

@mcp.tool()
def read_notes() -> str:
    """
    Read and return all notes from the sticky notes file.

    Returns:
        str: All notes as a single string separated by line breaks.
        If no notes are found, return a default message.
    """
    ensure_file()
    with open(NOTES_FILE, "r") as f:
        content = f.read().strip()
    return content or "No notes found. Please add a note first."

@mcp.resource("notes://latest")
def get_latest_note() -> str:
    """
    Get the latest note from the sticky notes file.

    Returns:
        str: The latest note. If no notes are found, return a default message.
    """
    ensure_file()
    with open(NOTES_FILE, "r") as f:
        lines = f.readlines()
    return lines[-1].strip() if lines else "No notes found. Please add a note first."

@mcp.prompt()
def note_summary_promt() -> str:
    """
    Generate a summary of the notes.

    Returns:
        str: A prompt for summarizing the notes.
    """

    ensure_file()
    with open(NOTES_FILE, "r") as f:
        content = f.read().strip()
    if not content:
        return "No notes found. Please add a note first."
    return f"Summarize the current notes:{content}"