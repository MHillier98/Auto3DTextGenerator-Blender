import bpy
import os
import string

bl_info = {
    "name": "3D Text Generator",
    "author": "Matthew Hillier",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Add > Mesh > New Object",
    "description": "Generates 3D models from text",
    "warning": "",
    "doc_url": "",
    "category": "Add Mesh",
}

def main(context):
    all_chars = list(string.ascii_letters) + list(string.digits)

    chars_collection = bpy.data.collections.new("All Chars")
    bpy.context.scene.collection.children.link(chars_collection)

    for i in all_chars:
        char_name = "char: " + i
        # print(char_name)
        font_curve = bpy.data.curves.new(type="FONT", name="font_curve: " + i)
        font_curve.body = i
        font_curve.extrude = 0.05
        font_curve.font = bpy.data.fonts.load('C:\\Windows\\Fonts\\Georgia.ttf')
        font_curve.align_x = 'CENTER'
        font_curve.align_y = 'BOTTOM_BASELINE'
        font_obj = bpy.data.objects.new(char_name, font_curve)

        bpy.data.collections['All Chars'].objects.link(font_obj)

        objectToSelect = bpy.data.objects[char_name]
        objectToSelect.select_set(True)
        bpy.context.view_layer.objects.active = objectToSelect
        bpy.ops.object.convert(target='MESH')

class TextGenerator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.text_generator"
    bl_label = "3D Text Generator"

    def execute(self, context):
        main(context)
        return {'FINISHED'}


class LayoutDemoPanel(bpy.types.Panel):
    """Creates a Panel in the scene context of the properties editor"""
    bl_label = "Layout Demo"
    bl_idname = "SCENE_PT_layout"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "scene"

    def draw(self, context):
        layout = self.layout

        scene = context.scene

        # Big render button
        layout.label(text="Big Button:")
        row = layout.row()
        row.scale_y = 2.0
        row.operator("object.text_generator")


def register():
    bpy.utils.register_class(TextGenerator)
    bpy.utils.register_class(LayoutDemoPanel)


def unregister():
    bpy.utils.unregister_class(LayoutDemoPanel)
    bpy.utils.unregister_class(TextGenerator)


if __name__ == "__main__":
    register()
