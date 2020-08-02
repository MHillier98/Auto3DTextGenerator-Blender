# Auto 3D Text Generator - Blender

This Blender Addon can automatically create text objects of letters and numbers, convert them to meshes, and export them to .obj files.

Currently, I've hardcoded in the font settings, but I would like to add additional UI options in the future for these.

### UI

![UI](./screenshots/ui.png 'UI')

- **Empty Scene:** Deletes _everything_ in the scene so the export runs properly.
- **Generate Text:** Generates text objects (from [`string.ascii_uppercase`](https://docs.python.org/3/library/string.html#string.ascii_uppercase) and [`string.digits`](https://docs.python.org/3/library/string.html#string.digits)), then converts them to meshes.
- **Export all chars to .obj:** Exports all models to a hardcoded file path.

### Example Output

![UI](./screenshots/output.png 'UI')
