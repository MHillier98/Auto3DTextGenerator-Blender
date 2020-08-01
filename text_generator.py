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


def generate_buttton(context):
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
    bl_idname = "mhillier.generate_text"
    bl_label = "Generate Text"

    def execute(self, context):
        generate_buttton(context)
        return {'FINISHED'}




def clear_buttton(context):
    bpy.ops.object.select_all()
    bpy.ops.object.select_all()
    bpy.ops.object.delete(use_global=False)
    for c in bpy.data.collections:
        bpy.data.collections.remove(c)




class RemoveAll(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "mhillier.remove_all"
    bl_label = "Delete EVERYTHING!"

    def execute(self, context):
        clear_buttton(context)
        return {'FINISHED'}





class LayoutDemoPanel(bpy.types.Panel):
    """Creates a Panel in the scene context of the properties editor"""
    bl_label = "3D Text Generator"
    bl_idname = "SCENE_PT_layout"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "scene"

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        layout.label(text="Empty Scene")
        row = layout.row()
        row.scale_y = 2.0
        row.operator("mhillier.remove_all")

        layout.label(text="Text Generator")
        row = layout.row()
        row.scale_y = 2.0
        row.operator("mhillier.generate_text")


def register():
    bpy.utils.register_class(TextGenerator)
    bpy.utils.register_class(LayoutDemoPanel)
    bpy.utils.register_class(RemoveAll)


def unregister():
    bpy.utils.unregister_class(LayoutDemoPanel)
    bpy.utils.unregister_class(TextGenerator)
    bpy.utils.unregister_class(RemoveAll)


if __name__ == "__main__":
    register()
