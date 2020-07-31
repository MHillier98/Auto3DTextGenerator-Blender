import bpy
import os
import string

all_chars = list(string.ascii_letters) + list(string.digits)
# print(all_chars)

chars_collection = bpy.data.collections.new("All Chars")
bpy.context.scene.collection.children.link(chars_collection)

for i in all_chars:
    char_name = "char: " + i
    # print(char_name)
    font_curve = bpy.data.curves.new(type="FONT", name="font_curve: " + i)
    font_curve.body = i
    font_curve.extrude = 0.05
    font_curve.font = bpy.data.fonts.load('C:\Windows\Fonts\Georgia.ttf')
    font_curve.align_x = 'CENTER'
    font_curve.align_y = 'BOTTOM_BASELINE'
    font_obj = bpy.data.objects.new(char_name, font_curve)

    bpy.data.collections['All Chars'].objects.link(font_obj)

    objectToSelect = bpy.data.objects[char_name]
    objectToSelect.select_set(True)
    bpy.context.view_layer.objects.active = objectToSelect
    bpy.ops.object.convert(target='MESH')
