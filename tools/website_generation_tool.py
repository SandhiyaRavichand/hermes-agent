import os
from uuid import uuid4

from tools.registry import registry

WEBSITE_SCHEMA = {
    "type": "object",
    "properties": {
        "prompt": {
            "type": "string",
            "description": "Website description"
        }
    },
    "required": ["prompt"]
}

def generate_website(prompt: str):

    project_id = str(uuid4())[:8]

    project_dir = f"/tmp/projects/{project_id}"

    os.makedirs(project_dir, exist_ok=True)

    file_path = f"{project_dir}/index.html"

    html = f"""
    <!DOCTYPE html>
    <html>
    <body>
        <h1>{prompt}</h1>
    </body>
    </html>
    """

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)

    return {
        "project_id": project_id,
        "file_path": file_path
    }

registry.register(
    name="generate_website",
    toolset="website",
    schema=WEBSITE_SCHEMA,
    handler=lambda args, **kw: generate_website(
        prompt=args["prompt"]
    ),
    emoji="🌐",
)
