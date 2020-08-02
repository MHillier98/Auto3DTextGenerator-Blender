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
    custom_chars = ['10', '11', '12']
    all_chars = list(string.ascii_uppercase) + \
        list(string.digits) + custom_chars

    chars_collection = bpy.data.collections.new("All Chars")
    bpy.context.scene.collection.children.link(chars_collection)

    for i in all_chars:
        char_name = "char-" + i
        font_curve = bpy.data.curves.new(type="FONT", name="font_curve: " + i)
        font_curve.body = i
        font_curve.extrude = 0.05
        font_curve.font = bpy.data.fonts.load('C:\\Windows\\Fonts\\GARA.ttf')

        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
        font_curve.align_x = 'CENTER'
        font_curve.align_y = 'CENTER'
        font_obj = bpy.data.objects.new(char_name, font_curve)

        bpy.data.collections['All Chars'].objects.link(font_obj)

        objectToSelect = bpy.data.objects[char_name]
        objectToSelect.select_set(True)
        bpy.context.view_layer.objects.active = objectToSelect
        bpy.ops.object.convert(target='MESH')


class TextGenerator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "3dtextgen.generate_text"
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
    bl_idname = "3dtextgen.remove_all"
    bl_label = "DELETE EVERYTHING!"

    def execute(self, context):
        clear_buttton(context)
        return {'FINISHED'}


def export_all_obj(exportFolder):
    objects = bpy.data.objects
    for object in objects:
        bpy.ops.object.select_all(action='DESELECT')
        object.select_set(state=True)
        exportName = exportFolder + object.name + '.obj'
        bpy.ops.export_scene.obj(filepath=exportName, use_selection=True)


class ExportAll(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "3dtextgen.export_all"
    bl_label = "Export all chars to .obj"

    def execute(self, context):
        export_all_obj('C:\\Users\\Matthew\\Desktop\\Blender\\test\\')
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
        row.scale_y = 1.5
        row.operator("3dtextgen.remove_all")

        layout.label(text="Text Generator")
        row = layout.row()
        row.scale_y = 1.5
        row.operator("3dtextgen.generate_text")

        layout.label(text="Export chars")
        row = layout.row()
        row.scale_y = 1.5
        row.operator("3dtextgen.export_all")


def register():
    bpy.utils.register_class(TextGenerator)
    bpy.utils.register_class(LayoutDemoPanel)
    bpy.utils.register_class(RemoveAll)
    bpy.utils.register_class(ExportAll)


def unregister():
    bpy.utils.unregister_class(LayoutDemoPanel)
    bpy.utils.unregister_class(TextGenerator)
    bpy.utils.unregister_class(RemoveAll)
    bpy.utils.unregister_class(ExportAll)


if __name__ == "__main__":
    register()
